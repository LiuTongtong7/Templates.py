#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by liutongtong on 2018/8/18 10:01
#


class SegmentTreeNode(object):

    def __init__(self, l, r):
        self.l, self.r = l, r
        self.left_child, self.right_child = None, None
        self.sum = 0
        self.add = 0  # 用于区间更新的延迟标记


class SegmentTree(object):

    def __init__(self, arr):

        def build(arr, left, right):
            if left > right:
                return None
            elif left == right:
                node = SegmentTreeNode(left, right)
                node.sum = arr[left]
                return node
            else:
                node = SegmentTreeNode(left, right)
                mid = (left + right) >> 1
                node.left_child = build(arr, left, mid)
                node.right_child = build(arr, mid + 1, right)
                self.push_up(node, node.left_child, node.right_child)
                return node

        self.root = build(arr, 0, len(arr) - 1)

    @staticmethod
    def push_up(parent, left_child, right_child):
        parent.sum = left_child.sum + right_child.sum
        return parent

    @staticmethod
    def push_down(parent):
        if parent.add > 0:
            parent.left_child.add += parent.add
            parent.right_child.add += parent.add
            mid = (parent.l + parent.r) >> 1
            parent.left_child.sum += parent.add * (mid - parent.l + 1)
            parent.right_child.sum += parent.add * (parent.r - mid)
            parent.add = 0

    def query(self, left, right):

        def query_helper(node, left, right):
            if node.l > right or node.r < left:
                return None
            elif left <= node.l and node.r <= right:
                return node
            else:
                self.push_down(node)
                mid = (node.l + node.r) >> 1
                if right <= mid:
                    return query_helper(node.left_child, left, right)
                elif left > mid:
                    return query_helper(node.right_child, left, right)
                else:
                    left_res = query_helper(node.left_child, left, mid)
                    right_res = query_helper(node.right_child, mid + 1, right)
                    res = SegmentTreeNode(left, right)
                    return self.push_up(res, left_res, right_res)

        return query_helper(self.root, left, right).sum

    def update(self, pos, add_val):

        def update_helper(node, pos, add_val):
            if node.l > pos or node.r < pos:
                return
            if node.l == node.r:
                node.sum += add_val
            else:
                self.push_down(node)
                mid = (node.l + node.r) >> 1
                if pos <= mid:
                    update_helper(node.left_child, pos, add_val)
                else:
                    update_helper(node.right_child, pos, add_val)
                self.push_up(node, node.left_child, node.right_child)

        update_helper(self.root, pos, add_val)

    def update_interval(self, left, right, add_val):

        def update_interval_helper(node, left, right, add_val):
            if node.l > right or node.r < left:
                return
            elif left <= node.l and node.r <= right:
                node.sum += add_val * (node.r - node.l + 1)
                node.add += add_val
            else:
                self.push_down(node)
                mid = (node.l + node.r) >> 1
                update_interval_helper(node.left_child, left, right, add_val)
                update_interval_helper(node.right_child, left, right, add_val)
                self.push_up(node, node.left_child, node.right_child)

        update_interval_helper(self.root, left, right, add_val)

    def print_leaves(self):

        def get_leaves(node):
            if node is None:
                return []
            elif node.left_child is None and node.right_child is None:
                return [node.sum]
            else:
                self.push_down(node)
                leaves = []
                leaves.extend(get_leaves(node.left_child))
                leaves.extend(get_leaves(node.right_child))
                return leaves

        print(get_leaves(self.root))


if __name__ == '__main__':
    a = [-54, 97, 62, 37, -15, 13, 73, 36, -1, -28]
    st = SegmentTree(a)

    print(st.query(4, 9), sum(a[4:10]))
    st.print_leaves()

    st.update(7, 10)
    print(st.query(4, 9), sum(a[4:10]) + 10)
    st.print_leaves()

    st.update_interval(4, 8, 5)
    print(st.query(4, 9), sum(a[4:10]) + 10 + 5 * 5)
    st.print_leaves()

    st.update_interval(6, 9, 4)
    print(st.query(4, 9), sum(a[4:10]) + 10 + 5 * 5 + 4 * 4)
    st.print_leaves()

    st.update(8, 1)
    print(st.query(4, 9), sum(a[4:10]) + 10 + 5 * 5 + 4 * 4 + 1)
    st.print_leaves()
