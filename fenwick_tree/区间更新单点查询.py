#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/9/16 12:57
#


class FenwickTree(object):

    def __init__(self, arr):
        self.num = len(arr)
        self.tree = [0] * (self.num + 1)
        prev_val = 0
        for idx, val in enumerate(arr):
            self._update(idx, val - prev_val)  # 原始数据变为差分数组，tree保存差分数组前缀和（即原数的一部分）
            prev_val = val

    def _update(self, idx, add_val):
        idx += 1
        while idx <= self.num:
            self.tree[idx] += add_val
            idx += (idx & -idx)

    def update_interval(self, left, right, add_val):
        self._update(left, add_val)
        self._update(right + 1, -add_val)

    def update(self, idx, add_val):
        self.update_interval(idx, idx, add_val)

    def query(self, idx):
        idx += 1
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= (idx & -idx)
        return sum


if __name__ == '__main__':
    a = [-54, 97, 62, 37, -15, 13, 73, 36, -1, -28]
    ft = FenwickTree(a)
    # print(ft.tree)

    print(ft.query(8), a[8])

    ft.update_interval(7, 10, 2)
    print(ft.query(8), a[8] + 2)
