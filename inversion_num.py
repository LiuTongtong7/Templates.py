#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/9/29 15:35
#


# Merge Sort
def inversion_num_by_mergesort(arr):
    n = len(arr)
    a, b = arr, [0] * n
    width = 1
    ans = 0
    while width < n:
        for start in range(0, n, width * 2):
            left, middle, right = start, min(start + width, n), min(start + width * 2, n)
            l, r = left, middle
            for i in range(left, right):
                if l < middle and (r >= right or a[l] <= a[r]):
                    b[i] = a[l]
                    l += 1
                else:
                    ans += middle - l
                    b[i] = a[r]
                    r += 1
        a, b = b, a
        width *= 2
    if a is not arr:
        arr[:] = a[:]
    return ans


def inversion_num_by_mergesort2(arr):

    def helper(arr, buf, left, right):
        if left >= right:
            return 0
        middle = (left + right) >> 1
        ans = helper(arr, buf, left, middle)
        ans += helper(arr, buf, middle + 1, right)
        l, r = left, middle + 1
        for i in range(left, right + 1):
            if l <= middle and (r > right or arr[l] <= arr[r]):
                buf[i] = arr[l]
                l += 1
            else:
                ans += middle - l + 1
                buf[i] = arr[r]
                r += 1
        arr[left: right + 1] = buf[left: right + 1]
        return ans

    n = len(arr)
    buf = [0] * n
    return helper(arr, buf, 0, n - 1)


# Fenwick Tree
class FenwickTree(object):

    def __init__(self, num):
        self.num = num
        self.tree = [0] * (self.num + 1)

    def update(self, idx, add_val):
        while idx <= self.num:
            self.tree[idx] += add_val
            idx += (idx & -idx)

    def query_prefix(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= (idx & -idx)
        return sum


def inversion_num_by_fenwick(arr):  # arr都要是正数
    maxv = max(arr)
    ft = FenwickTree(maxv)
    ans = 0
    for i, val in enumerate(arr):
        ft.update(val, 1)
        ans += i + 1 - ft.query_prefix(val)
    return ans


def inversion_num_by_fenwick2(arr):  # 离散化
    
    def discretize(arr):
        pos_val = sorted(list(enumerate(arr)), key=lambda x: x[1])
        discretized_arr = [0] * len(arr)
        idx = 1
        discretized_arr[pos_val[0][0]] = idx
        for i in range(1, len(arr)):
            if pos_val[i][1] > pos_val[i - 1][1]:
                idx += 1
            discretized_arr[pos_val[i][0]] = idx
        return discretized_arr

    return inversion_num_by_fenwick(discretize(arr))


if __name__ == '__main__':
    arr = [3, 5, 7, 2, 3, 5, 1, 3, 2, 6, 7, 2, 4]
    ans = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                ans += 1
    print(ans)
    print(inversion_num_by_mergesort([3, 5, 7, 2, 3, 5, 1, 3, 2, 6, 7, 2, 4]))
    print(inversion_num_by_mergesort2([3, 5, 7, 2, 3, 5, 1, 3, 2, 6, 7, 2, 4]))
    print(inversion_num_by_fenwick([x * 100 for x in [3, 5, 7, 2, 3, 5, 1, 3, 2, 6, 7, 2, 4]]))
    print(inversion_num_by_fenwick2([x * 100 for x in [3, 5, 7, 2, 3, 5, 1, 3, 2, 6, 7, 2, 4]]))
