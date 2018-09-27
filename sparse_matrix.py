#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/9/13 00:38
#


class SparseMatrix(object):
    
    def __init__(self, row, col, data=None):
        self.row, self.col = row, col
        if data is not None:
            self.data = sorted(data)
            self.cal_rpos()
        else:
            self.data = []
        
    def cal_rpos(self):
        self.rpos = [0] * (self.row + 1)
        r, di = 0, 1
        while r < self.row:
            while di < len(self.data) and self.data[di][0] == r:
                di += 1
            r += 1
            self.rpos[r] = di

    def print(self):
        for r in range(self.row):
            row_data = [0] * (self.col)
            for di in range(self.rpos[r], self.rpos[r + 1]):
                row_data[self.data[di][1]] = self.data[di][2]
            print(' '.join(map(lambda v: '{:3d}'.format(v), row_data)))


def multiply(a, b):
    if a.col != b.row:
        return None

    res = SparseMatrix(a.row, b.col)
    for r in range(a.row):
        row_data = [0] * b.col
        for ai in range(a.rpos[r], a.rpos[r + 1]):
            k = a.data[ai][1]
            for bi in range(b.rpos[k], b.rpos[k + 1]):
                c = b.data[bi][1]
                row_data[c] += a.data[ai][2] * b.data[bi][2]
        for c in range(b.col):
            if row_data[c]:
                res.data.append([r, c, row_data[c]])
    res.cal_rpos()
    return res


def plus(a, b):
    if a.row != b.row or a.col != b.col:
        return None

    res = SparseMatrix(a.row, a.col)
    ai, bi = 0, 0
    while ai < len(a.data) and bi < len(b.data):
        if a.data[ai][0] == b.data[bi][0] and a.data[ai][1] == b.data[bi][1]:
            if a.data[ai][2] + b.data[bi][2]:
                res.data.append([a.data[ai][0], a.data[ai][1], a.data[ai][2] + b.data[bi][2]])
            ai += 1
            bi += 1
        elif a.data[ai][0] < b.data[bi][0] or (a.data[ai][0] == b.data[bi][0] and a.data[ai][1] < b.data[bi][1]):
            res.data.append([a.data[ai][0], a.data[ai][1], a.data[ai][2]])
            ai += 1
        else:
            res.data.append([b.data[bi][0], b.data[bi][1], b.data[bi][2]])
            bi += 1
    while ai < len(a.data):
        res.data.append([a.data[ai][0], a.data[ai][1], a.data[ai][2]])
        ai += 1
    while bi < len(b.data):
        res.data.append([b.data[bi][0], b.data[bi][1], b.data[bi][2]])
        bi += 1
    res.cal_rpos()
    return res


def multiply_constant(a, c):
    for d in a.data:
        d[2] *= c
    return a


if __name__ == '__main__':
    a = SparseMatrix(2, 2, [[0, 1, 1], [1, 0, 1], [1, 1, 1]])
    b = SparseMatrix(2, 2, [[0, 1, 1], [1, 0, 1]])
    c = SparseMatrix(2, 2, [[0, 0, 1], [1, 1, 1]])
    # a.print(), b.print(), c.print()

    r = plus(multiply_constant(multiply(a, b), 2), multiply_constant(c, 3))
    r.print()
