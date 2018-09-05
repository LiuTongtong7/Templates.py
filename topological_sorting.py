#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by liutongtong on 2018/9/5 10:54
#


def topological_sort(num_v, graph):  # graph为邻接表，用{v0: [v1, v2, ...]}表示
    indegree = [0] * (num_v + 1)
    for s in graph:
        for t in graph[s]:
            indegree[t] += 1
    
    queue = []  # 维护一个入度为0的队列
    for v in range(1, num_v + 1):
        if indegree[v] == 0:
            queue.append(v)

    ans = []
    while len(queue) > 0:
        v = queue.pop(0)
        ans.append(v)

        for i in graph.get(v, []):
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    return ans if len(ans) == num_v else []  # 排序结果不全，说明图中有环路


def topological_sort_dfs(num_v, graph):
    stack = []
    visited = [False] * (num_v + 1)

    def dfs(v):
        # nonlocal graph, stack, visited
        visited[v] = True
        for i in graph.get(v, []):
            if not visited[i]:
                dfs(i)
        stack.append(v)

    for i in range(1, num_v + 1):
        if not visited[i]:
            dfs(i)

    return stack[::-1]


if __name__ == '__main__':
    graph = {
        3: [4],
        4: [2],
        5: [1, 2],
        6: [1, 3],
    }
    print(topological_sort(6, graph))
    print(topological_sort_dfs(6, graph))
