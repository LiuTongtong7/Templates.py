#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by liutongtong on 2018/8/18 10:01
#


class SegmentTreeNode(object):

    def __init__(self, l, r):
        self.left_bound, self.right_bound = l, r
        self.left_child, self.right_child = None, None
        self.total_sum, self.max_sum = 0, 0
        self.prefix_sum, self.suffix_sum = 0, 0


class SegmentTree(object):

    def __init__(self, arr):

        def build(arr, left, right):
            if left > right:
                return None
            elif left == right:
                node = SegmentTreeNode(left, right)
                node.total_sum = arr[left]
                node.max_sum = arr[left]
                node.prefix_sum = arr[left]
                node.suffix_sum = arr[left]
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
        if left_child is None:
            left_child = SegmentTreeNode(0, 0)
        if right_child is None:
            right_child = SegmentTreeNode(0, 0)
        parent.total_sum = left_child.total_sum + right_child.total_sum
        parent.max_sum = max(max(left_child.max_sum, right_child.max_sum),
                             left_child.suffix_sum + right_child.prefix_sum)
        parent.prefix_sum = max(left_child.prefix_sum, left_child.total_sum + right_child.prefix_sum)
        parent.suffix_sum = max(right_child.suffix_sum, right_child.total_sum + left_child.suffix_sum)
        return parent

    def query(self, left, right):

        def query_helper(node, left, right):
            if node.left_bound > right or node.right_bound < left:
                return None
            elif left <= node.left_bound and node.right_bound <= right:
                return node
            else:
                left_res = query_helper(node.left_child, left, right)
                right_res = query_helper(node.right_child, left, right)
                res = SegmentTreeNode(left, right)
                return self.push_up(res, left_res, right_res)

        return query_helper(self.root, left, right).max_sum

    def update(self, pos, val):

        def update_helper(node, pos, val):
            if node.left_bound == node.right_bound:
                node.total_sum, node.max_sum = val, val
                node.prefix_sum, node.suffix_sum = val, val
            else:
                mid = (node.left_bound + node.right_bound) >> 1
                if pos <= mid:
                    update_helper(node.left_child, pos, val)
                else:
                    update_helper(node.right_child, pos, val)
                self.push_up(node, node.left_child, node.right_child)

        update_helper(self.root, pos, val)


if __name__ == '__main__':
    a = [-54, 97, 62, 37, -15, 13, 73, 36, -1, -28]
    st = SegmentTree(a)
    print(st.query(5, 9), sum(a[5:8]))
