#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/9/6 00:38
#


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


######################## 单次查询 ########################
def lca(root, p, q):
    if root == None or root.val in (p, q):
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    return root if left and right else left or right


###################### 离线批量查询 ######################
class UnionFind(object):

    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.size = [1] * n

    def find(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]
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


def tarjan_lca(num_v, graph, root, num_q, query):
    uf = UnionFind(num_v + 1)
    ancestor = [0] * (num_v + 1)
    visited = [False] * (num_v + 1)
    ans = [0] * num_q

    def lca(v):
        ancestor[v] = v
        for t in graph.get(v, []):
            if not visited[t]:
                lca(t)
                uf.union(v, t)
                ancestor[uf.find(v)] = v  # uf.find(v)不一定是v，这里是为了确保v为根的子树的组选为v
        visited[v] = True
        for t, idx in query.get(v, []):
            if visited[t]:
                ans[idx] = ancestor[uf.find(t)]

    lca(root)
    return ans


###################### 在线批量查询 ######################







if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(8)
    root.right = TreeNode(3)
    print(lca(root, 5, 6).val)

    num_v = 8
    graph = {
        1: [2, 3],
        2: [4, 5],
        4: [6, 7],
        5: [8]
    }
    root = 1

    num_q = 4
    query = {}
    for i, q in enumerate([(3, 5), (5, 6), (2, 7), (6, 7)]):
        query.setdefault(q[0], []).append((q[1], i))
        query.setdefault(q[1], []).append((q[0], i))
    print(tarjan_lca(num_v, graph, root, num_q, query))
