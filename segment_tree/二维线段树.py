#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by liutongtong on 2018/8/18 16:37
#


class SegmentTreeNode(object):

    def __init__(self, x1, x2, y1, y2):
        self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2
        self.children = [None] * 4
        self.sum = 0
        self.add = 0  # 用于区间更新的延迟标记

    def area(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1)


class SegmentTree(object):

    def __init__(self, arr):

        def build(arr, x1, x2, y1, y2):
            if x1 > x2 or y1 > y2:
                return None
            elif x1 == x2 and y1 == y2:
                node = SegmentTreeNode(x1, x2, y1, y2)
                node.sum = arr[x1][y1]
                return node
            else:
                node = SegmentTreeNode(x1, x2, y1, y2)
                mid_x = (x1 + x2) >> 1
                mid_y = (y1 + y2) >> 1
                node.children[0] = build(arr, x1, mid_x, y1, mid_y)
                node.children[1] = build(arr, mid_x + 1, x2, y1, mid_y)
                node.children[2] = build(arr, x1, mid_x, mid_y + 1, y2)
                node.children[3] = build(arr, mid_x + 1, x2, mid_y + 1, y2)
                self.push_up(node, node.children)
                return node

        rows, cols = len(arr), len(arr[0])
        self.root = build(arr, 0, rows - 1, 0, cols - 1)

    @staticmethod
    def push_up(parent, children):
        parent.sum = 0
        for child in children:
            if child is not None:
                parent.sum += child.sum
        return parent

    @staticmethod
    def push_down(parent):
        if parent.add > 0:
            for child in parent.children:
                if child is not None:
                    child.sum += parent.add * child.area()
                    child.add += parent.add
            parent.add = 0

    def query(self, x1, x2, y1, y2):

        def query_helper(node, x1, x2, y1, y2):
            if node is None or node.x1 > x2 or node.x2 < x1 or node.y1 > y2 or node.y2 < y1:
                return 0
            elif x1 <= node.x1 and node.x2 <= x2 and y1 <= node.y1 and node.y2 <= y2:
                return node.sum
            else:
                self.push_down(node)
                res = 0
                for child in node.children:
                    res += query_helper(child, x1, x2, y1, y2)
                return res

        return query_helper(self.root, x1, x2, y1, y2)

    def update(self, x, y, add_val):

        def update_helper(node, x, y, add_val):
            if node is None or node.x1 > x or node.x2 < x or node.y1 > y or node.y2 < y:
                return
            elif node.x1 == node.x2 and node.y1 == node.y2:
                node.sum += add_val
            else:
                self.push_down(node)
                mid_x = (node.x1 + node.x2) >> 1
                mid_y = (node.y1 + node.y2) >> 1
                child_index = (int(y > mid_y) << 1) | int(x > mid_x)
                update_helper(node.children[child_index], x, y, add_val)
                self.push_up(node, node.children)

        update_helper(self.root, x, y, add_val)

    def update_interval(self, x1, x2, y1, y2, add_val):

        def update_interval_helper(node, x1, x2, y1, y2, add_val):
            if node is None or node.x1 > x2 or node.x2 < x1 or node.y1 > y2 or node.y2 < y1:
                return
            elif x1 <= node.x1 and node.x2 <= x2 and y1 <= node.y1 and node.y2 <= y2:
                node.sum += add_val * node.area()
                node.add += add_val
            else:
                self.push_down(node)
                for child in node.children:
                    update_interval_helper(child, x1, x2, y1, y2, add_val)
                self.push_up(node, node.children)

        update_interval_helper(self.root, x1, x2, y1, y2, add_val)

    def print_leaves(self, rows, cols):

        def get_leaves(node):
            if node is None:
                return
            elif node.x1 == node.x2 and node.y1 == node.y2:
                arr[node.x1][node.y1] = node.sum
            else:
                self.push_down(node)
                for child in node.children:
                    get_leaves(child)

        arr = [[0 for _ in range(cols)] for _ in range(rows)]
        get_leaves(self.root)
        print(arr)


if __name__ == '__main__':
    arr = [[1, 2, 3, 4], 
           [5, 6, 7, 8], 
           [9, 0, 5, 2]]
    st = SegmentTree(arr)
    print(st.query(1, 2, 0, 2), 32)
    # st.print_leaves(3, 4)

    st.update_interval(0, 1, 1, 2, 3)
    print(st.query(1, 2, 0, 2), 38)

    st.update(0, 0, 5)
    print(st.query(1, 2, 0, 2), 38)
    print(st.query(0, 2, 0, 0), 20)
