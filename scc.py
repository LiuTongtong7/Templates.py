#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by liutongtong on 2018/9/5 01:03
#


def tarjan(num_v, graph):  # graph为邻接表，用{v0: [v1, v2, ...]}表示
    dfn, low = [0] * (num_v + 1), [0] * (num_v + 1)
    dfn_index = 0
    scc, scc_count = [0] * (num_v + 1), 0
    stack = []
    instack = [False] * (num_v + 1)

    def dfs(v):
        # nonlocal dfn, low, dfn_index, scc, scc_count, stack, instack
        nonlocal dfn_index, scc_count

        dfn_index += 1
        dfn[v], low[v] = dfn_index, dfn_index
        instack[v] = True
        stack.append(v)

        for t in graph.get(v, []):
            if not dfn[t]:
                dfs(t)
                low[v] = min(low[v], low[t])
            elif instack[t]:
                low[v] = min(low[v], dfn[t])
        if dfn[v] == low[v]:
            tmp = 0
            scc_count += 1
            while tmp != v:
                tmp = stack.pop()
                scc[tmp] = scc_count
                instack[tmp] = False

    for i in range(1, num_v + 1):
        if not dfn[i]:
            dfs(i)

    return scc_count, scc


def kosaraju(num_v, graph):
    graph_r = {}
    for s in graph:
        for t in graph[s]:
            graph_r.setdefault(t, []).append(s)

    scc, scc_count = [0] * (num_v + 1), 0
    stack = []
    visited = [False] * (num_v + 1)

    def dfs(v):
        visited[v] = True
        for t in graph.get(v, []):
            if not visited[t]:
                dfs(t)
        stack.append(v)

    def dfs_r(v):
        scc[v] = scc_count
        for t in graph_r.get(v, []):
            if not scc[t]:
                dfs_r(t)

    for i in range(1, num_v + 1):
        if not visited[i]:
            dfs(i)
    
    while len(stack) > 0:
        v = stack.pop()
        if not scc[v]:
            scc_count += 1
            dfs_r(v)
    
    return scc_count, scc


if __name__ == '__main__':
    graph = {
        1: [2, 3],
        2: [4],
        3: [4, 5],
        4: [1, 6],
        5: [6],
        6: []
    }
    print(tarjan(6, graph))
    print(kosaraju(6, graph))

    graph = {
        1: [2, 5], 
        2: [3, 4], 
        3: [], 
        4: [1, 3],
        5: [6, 7],
        6: [4],
        7: [8],
        8: [5, 9],
        9: []
    }
    print(tarjan(9, graph))
    print(kosaraju(9, graph))
