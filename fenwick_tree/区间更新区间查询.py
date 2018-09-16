#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/9/16 13:07
#


class FenwickTree(object):

    def __init__(self, arr):
        self.num = len(arr)
        self.tree1 = [0] * (self.num + 1)  # 对应的原始数组为差分数组
        self.tree2 = [0] * (self.num + 1)  # 对应的原始数组为差分数组*下标
        prev_val = 0
        for idx, val in enumerate(arr):
            self._update(idx, val - prev_val)  # 原始数据变为差分数组，tree保存差分数组前缀和（即原数的一部分）
            prev_val = val

    def _update(self, idx, add_val):
        idx += 1
        add_val1, add_val2 = add_val, add_val * idx
        while idx <= self.num:
            self.tree1[idx] += add_val1
            self.tree2[idx] += add_val2
            idx += (idx & -idx)

    def update_interval(self, left, right, add_val):
        self._update(left, add_val)
        self._update(right + 1, -add_val)

    def update(self, idx, add_val):
        self.update_interval(idx, idx, add_val)

    def query_prefix(self, idx):
        idx += 1
        tmp_idx = idx
        res1, res2 = 0, 0
        while idx > 0:
            res1 += self.tree1[idx]
            res2 += self.tree2[idx]
            idx -= (idx & -idx)
        return (tmp_idx + 1) * res1 - res2

    def query_interval(self, left, right):
        return self.query_prefix(right) - self.query_prefix(left - 1)

    def query(self, idx):
        return self.query_prefix(idx) - self.query_prefix(idx - 1)


if __name__ == '__main__':
    a = [-54, 97, 62, 37, -15, 13, 73, 36, -1, -28]
    ft = FenwickTree(a)

    print(ft.query_interval(4, 9), sum(a[4:10]))

    ft.update(7, 10)
    print(ft.query_interval(4, 9), sum(a[4:10]) + 10)

    ft.update_interval(4, 8, 5)
    print(ft.query_interval(4, 9), sum(a[4:10]) + 10 + 5 * 5)

    ft.update_interval(6, 9, 4)
    print(ft.query_interval(4, 9), sum(a[4:10]) + 10 + 5 * 5 + 4 * 4)

    ft.update(8, 1)
    print(ft.query_interval(4, 9), sum(a[4:10]) + 10 + 5 * 5 + 4 * 4 + 1)
