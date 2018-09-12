#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/9/13 00:38
#


def check_bigragh(num_v, graph):
    color = [0] * (num_v + 1)

    def dfs(v, c):
        color[v] = c
        for t in graph.get(v, []):
            if color[t] == c or (color[t] == 0 and dfs(t, -c) == False):
                return False
        return True

    for v in range(1, num_v + 1):
        if color[v] == 0:
            if dfs(v, 1) == False:
                return []
    return ([v for v in range(1, num_v + 1) if color[v] > 0], 
            [v for v in range(1, num_v + 1) if color[v] < 0])


def hungarian_dfs(left_v, right_v, graph):
    num_v = len(left_v) + len(right_v)
    matching = [0] * (num_v + 1)

    def dfs(u, visited):
        for v in graph.get(u, []):
            if not visited[v]:
                visited[v] = True
                if matching[v] == 0 or dfs(matching[v], visited):
                    matching[v], matching[u] = u, v
                    return True
        return False

    ans = 0
    for v in left_v:
        if matching[v] == 0:
            visited = [False] * (num_v + 1)
            if dfs(v, visited):
                ans += 1
    return ans, matching


def hungarian_bfs(left_v, right_v, graph):
    num_v = len(left_v) + len(right_v)
    matching = [0] * (num_v + 1)
    ans = 0
    visited = [False] * (num_v + 1)
    
    prev = [0] * (num_v + 1)
    queue = []

    for i in left_v:
        if matching[i] == 0:
            if len(queue) > 0:
                del queue[:]
            prev[i] = 0  # i为路径起点
            queue.append(i)
            found = False  # 是否找到增广路径
            while len(queue) > 0 and not found:
                u = queue.pop(0)
                for v in graph.get(u, []):
                    if visited[v] != i:
                        visited[v] = i
                        if matching[v] == 0:
                            found = True
                            d, e = u, v
                            while d > 0:
                                matching[d], matching[e], d, e = e, d, prev[d], matching[d]
                            break
                        else:
                            prev[matching[v]] = u
                            queue.append(matching[v])
            if matching[i] > 0:
                ans += 1
    return ans, matching


if __name__ == '__main__':
    graph = {
        1: [5, 7],
        2: [5],
        3: [5, 6],
        4: [7, 8],
        5: [1, 2, 3],
        6: [3],
        7: [1, 4],
        8: [4]
    }
    vertex_split = check_bigragh(8, graph)
    print(vertex_split)
    if vertex_split:
        left_v, right_v = vertex_split
        print(hungarian_dfs(left_v, right_v, graph))
        print(hungarian_bfs(left_v, right_v, graph))
