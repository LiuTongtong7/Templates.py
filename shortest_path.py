#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by liutongtong on 2018/8/31 23:23
#

import copy


def floyd(edge, inf=0x3F3F3F3F):  # 邻接矩阵，可达为边的权重，不可达为inf
    num_v = len(edge)
    cost = copy.deepcopy(edge)
    path = [[-1 for _ in range(num_v)] for _ in range(num_v)]
    for s in range(num_v):
        for t in range(num_v):
            if cost[s][t] < inf:
                path[s][t] = t

    for k in range(num_v):
        for i in range(num_v):
            for j in range(num_v):
                if cost[i][j] > cost[i][k] + cost[k][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]
                    path[i][j] = path[i][k]

    return cost, path


def print_path(path, source, target):
    if path[source][target] < 0:
        return []

    ans = [source]
    while path[source][target] != target:
        ans.append(path[source][target])
        source = path[source][target]
    ans.append(target)
    return ans


def dijkstra(edge, source, inf=0x3F3F3F3F):
    num_v = len(edge)
    dist = [inf] * num_v  # source到各点的最短路径长度
    prev = [-1] * num_v   # source到各点的最短路径的前驱
    visited = [False] * num_v  # 各点是否找到了最短路径
    dist[source] = 0
    
    for i in range(num_v):
        v, min_d = -1, inf
        for j in range(num_v):
            if not visited[j] and dist[j] < min_d:
                v, min_d = j, dist[j]
        visited[v] = True

        for j in range(num_v):
            if not visited[j] and dist[v] + edge[v][j] < dist[j]:
                dist[j] = dist[v] + edge[v][j]
                prev[j] = v
    return dist, prev


def print_path2(prev, source, target):
    ans = [target]
    while prev[target] != source:
        ans.append(prev[target])
        target = prev[target]
    ans.append(source)
    return ans[::-1]


if __name__ == '__main__':
    num_v = 5
    inf = 0x3F3F3F3F
    edge = [[inf for _ in range(num_v)] for _ in range(num_v)]
    edge[0][1] = 10
    edge[0][3] = 30
    edge[0][4] = 100
    edge[1][2] = 50
    edge[2][4] = 10
    edge[3][2] = 20
    edge[3][4] = 60

    cost, path = floyd(edge)
    print(print_path(path, 0, 4))

    dist, prev = dijkstra(edge, 0)
    print(print_path2(prev, 0, 4))
