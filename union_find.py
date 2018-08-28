#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/8/12 15:21
#


class UnionFind(object):

    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.size = [1] * n

    def find(self, p):
        while self.id[p] != p:
            # self.size[self.id[p]] -= 1
            self.id[p] = self.id[self.id[p]]
            # self.size[self.id[p]] += 1
            p = self.id[p]
        return p

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root != q_root:
            if self.size[p_root] < self.size[q_root]:
                self.id[p_root] = q_root
                self.size[q_root] += self.size[p_root]
            else:
                self.id[q_root] = p_root
                self.size[p_root] += self.size[q_root]
            self.count -= 1


if __name__ == '__main__':
    n = 20
    uf = UnionFind(n)
    uf.union(8, 9)
    print(uf.count)
    uf.union(7, 9)
    print(uf.count)
    uf.union(7, 8)
    print(uf.count)
