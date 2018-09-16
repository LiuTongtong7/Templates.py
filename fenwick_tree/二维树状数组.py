#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/9/16 12:34
#


class FenwickTree2D(object):

    def __init__(self, arr):
        self.rows, self.cols = len(arr), len(arr[0])
        self.tree = [[0 for _ in range(self.cols + 1)] for _ in range(self.rows + 1)]
        for x in range(self.rows):
            for y in range(self.cols):
                self.update(x, y, arr[x][y])

    def update(self, x, y, add_val):
        x += 1
        y += 1
        while x <= self.rows:
            tmp_y = y
            while tmp_y <= self.cols:
                self.tree[x][tmp_y] += add_val
                tmp_y += (tmp_y & -tmp_y)
            x += (x & -x)

    def query_prefix(self, x, y):
        x += 1
        y += 1
        sum = 0
        while x > 0:
            tmp_y = y
            while tmp_y > 0:
                sum += self.tree[x][tmp_y]
                tmp_y -= (tmp_y & -tmp_y)
            x -= (x & -x)
        return sum

    def query_interval(self, x1, x2, y1, y2):
        return self.query_prefix(x2, y2) + self.query_prefix(x1 - 1, y1 - 1) - self.query_prefix(x1 - 1, y2) - self.query_prefix(x2, y1 - 1)


if __name__ == '__main__':
    arr = [[1, 2, 3, 4], 
           [5, 6, 7, 8], 
           [9, 0, 5, 2]]
    ft = FenwickTree2D(arr)
    print(ft.query_interval(1, 2, 0, 2), 32)

    ft.update(0, 0, 5)
    print(ft.query_interval(1, 2, 0, 2), 32)
    print(ft.query_interval(0, 2, 0, 0), 20)
