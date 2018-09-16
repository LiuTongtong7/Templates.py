#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/9/15 17:46
#


class FenwickTree(object):

    def __init__(self, arr):
        self.num = len(arr)
        self.tree = [0] * (self.num + 1)
        for idx, val in enumerate(arr):
            self.update(idx, val)

    def update(self, idx, add_val):
        idx += 1
        while idx <= self.num:
            self.tree[idx] += add_val
            idx += (idx & -idx)

    def query_prefix(self, idx):
        idx += 1
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= (idx & -idx)
        return sum

    def query_interval(self, left, right):
        return self.query_prefix(right) - self.query_prefix(left - 1)

    # def query(self, idx):
    #     return self.query_interval(idx) - self.query_interval(idx - 1)

    def query(self, idx):
        idx += 1
        sum = self.tree[idx]
        if idx > 0:
            z = idx - (idx & -idx)
            idx -= 1
            while idx != z:
                sum -= self.tree[idx]
                idx -= (idx & -idx)
        return sum


if __name__ == '__main__':
    a = [-54, 97, 62, 37, -15, 13, 73, 36, -1, -28]
    ft = FenwickTree(a)

    print(ft.query_interval(4, 9), sum(a[4:10]))

    ft.update(7, 10)
    print(ft.query_interval(4, 9), sum(a[4:10]) + 10)

    ft.update(8, 1)
    print(ft.query_interval(4, 9), sum(a[4:10]) + 10 + 1)
