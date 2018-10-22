#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by liutongtong on 2018/9/15 12:28
#


class SegmentTreeNode(object):

    def __init__(self, l, r):
        self.left_bound, self.right_bound = l, r
        self.left_child, self.right_child = None, None
        self.index = -1


class SegmentTree(object):

    def __init__(self, arr):

        def build(arr, left, right):
            if left > right:
                return None
            elif left == right:
                node = SegmentTreeNode(left, right)
                return node
            else:
                node = SegmentTreeNode(left, right)
                mid = (left + right) >> 1
                node.left_child = build(arr, left, mid)
                node.right_child = build(arr, mid + 1, right)
                return node

        def discretize(arr):
            arr = sorted(list(set(arr)))
            for i in range(len(arr) - 1, 0, -1):
                if arr[i] - arr[i - 1] > 1:
                    arr.append(arr[i] - 1)
            return sorted(arr)

        self.arr = discretize(arr)
        self.root = build(self.arr, 0, len(self.arr) - 1)

    def get_discretized_index(self, val):
        if val < self.arr[0] or val > self.arr[-1]:
            return -1
        l, r = 0, len(self.arr)
        while l < r:
            mid = (l + r) >> 1
            if self.arr[mid] < val:
                l = mid + 1
            else:
                r = mid
        return l

    @staticmethod
    def push_down(parent):
        if parent.index >= 0:
            parent.left_child.index = parent.index
            parent.right_child.index = parent.index
            parent.index = -1

    def query(self, left, right):

        def query_helper(node, left, right):
            if node.left_bound > right or node.right_bound < left:
                return set()
            if left <= node.left_bound and node.right_bound <= right:
                if node.left_bound == node.right_bound:
                    return {node.index} if node.index >= 0 else set()
                if node.index >= 0:  # 该区间内只有一种海报
                    return {node.index}

            self.push_down(node)
            mid = (node.left_bound + node.right_bound) >> 1
            if right <= mid:
                return query_helper(node.left_child, left, right)
            elif left > mid:
                return query_helper(node.right_child, left, right)
            else:
                left_res = query_helper(node.left_child, left, mid)
                right_res = query_helper(node.right_child, mid + 1, right)
                return left_res | right_res

        return query_helper(self.root, left, right)

    def update(self, pos, index):

        def update_helper(node, pos, index):
            if node.left_bound > pos or node.right_bound < pos:
                return
            elif node.left_bound == node.right_bound:
                node.index = index
            else:
                self.push_down(node)
                mid = (node.left_bound + node.right_bound) >> 1
                if pos <= mid:
                    update_helper(node.left_child, pos, index)
                else:
                    update_helper(node.right_child, pos, index)

        update_helper(self.root, pos, index)

    def update_interval(self, left, right, index):

        def update_interval_helper(node, left, right, index):
            if node.left_bound > right or node.right_bound < left:
                return
            elif left <= node.left_bound and node.right_bound <= right:
                node.index = index
            else:
                self.push_down(node)
                update_interval_helper(node.left_child, left, right, index)
                update_interval_helper(node.right_child, left, right, index)

        update_interval_helper(self.root, left, right, index)

    # For Debug
    def print_leaves(self):

        def get_leaves(node):
            if node is None:
                return []
            elif node.left_bound == node.right_bound:
                return [node.index]
            else:
                self.push_down(node)
                leaves = []
                leaves.extend(get_leaves(node.left_child))
                leaves.extend(get_leaves(node.right_child))
                return leaves

        print(self.arr)
        print(get_leaves(self.root))


if __name__ == '__main__':
    # poj 2528
    intervals = [[1, 4], [2, 6], [8, 10], [3, 4], [8, 13]]
    st = SegmentTree([x for i in intervals for x in i])
    for i, (l, r) in enumerate(intervals):
        l = st.get_discretized_index(l)
        r = st.get_discretized_index(r)
        st.update_interval(l, r, i)
    print(st.query(0, len(st.arr) - 1))
    st.print_leaves()
