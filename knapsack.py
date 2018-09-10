#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/9/8 12:46
#


# 01背包问题 - 添加一个物品
def _zero_one_knapsack(dp, knapsack_size, weight, value):
    for w in range(knapsack_size, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)


# 01背包问题
def zero_one_knapsack(knapsack_size, items):  # items格式: [(weight, value), ...]
    dp = [0] * (knapsack_size + 1)
    for weight, value in items:
        _zero_one_knapsack(dp, knapsack_size, weight, value)
    return dp[-1]


# 01背包问题的优化
# def zero_one_knapsack_(knapsack_size, items):
#     dp = [0] * (knapsack_size + 1)
#     cumsum_weight = [w for w, v in items]
#     for i in range(len(cumsum_weight) - 2, -1, -1):
#         cumsum_weight[i] += cumsum_weight[i + 1]
#     for i, (weight, value) in enumerate(items):
#         for w in range(knapsack_size, max(weight, knapsack_size - cumsum_weight[i]) - 1, -1):
#             dp[w] = max(dp[w], dp[w - weight] + value)
#     return dp[-1]


# 完全背包问题 - 添加一个物品
def _complete_knapsack(dp, knapsack_size, weight, value):
    for w in range(weight, knapsack_size + 1):
        dp[w] = max(dp[w], dp[w - weight] + value)


# 完全背包问题
def complete_knapsack(knapsack_size, items):
    INF = 0x3F3F3F3F
    DELTA = 1e-6

    # 过滤掉weight更大、value更小的物品
    max_values = [0] * (knapsack_size + 1)
    for weight, value in items:
        if weight <= knapsack_size:
            max_values[weight] = max(max_values[weight], value)
    for i in range(1, knapsack_size + 1):
        # DELTA是为了相同value的情况下，选择weight更小的，DELTA的值需要保证 DELTA * len(items) < 1
        max_values[i] = max(max_values[i], max_values[i - 1] + DELTA)

    filter_items = []
    for weight, value in items:
        if weight <= knapsack_size and value == max_values[weight]:
            filter_items.append((weight, value))
            max_values[weight] = INF  # 防止有完全相同的物品

    dp = [0] * (knapsack_size + 1)
    for weight, value in items:
        _complete_knapsack(dp, knapsack_size, weight, value)
    return dp[-1]


# 多重背包问题（转化为01背包问题，注意二进制的拆分方法）
def multiple_knapsack_by01(knapsack_size, items):  # items格式: [(num, weight, value), ...]
    dp = [0] * (knapsack_size + 1)
    for num, weight, value in items:
        if num * weight >= knapsack_size:
            _complete_knapsack(dp, knapsack_size, weight, value)
        k = 1
        while k < num:
            _zero_one_knapsack(dp, knapsack_size, k * weight, k * value)
            num -= k
            k *= 2
        _zero_one_knapsack(dp, knapsack_size, num * weight, num * value)
    return dp[-1]


def _multiple_knapsack(dp, knapsack_size, num, weight, value):
    # 背包容量 W=q*weight+r
    for r in range(weight):
        queue1, queue2 = [], []  # 主队列，辅助队列（单调队列）
        W, q = r, 0
        while W <= knapsack_size:
            if len(queue1) >= num:
                if queue1[0] == queue2[0]:
                    queue2.pop(0)
                queue1.pop(0)
            tmp = dp[W] - q * value
            queue1.append(tmp)
            while len(queue2) > 0 and queue2[-1] < tmp:
                queue2.pop(-1)
            queue2.append(tmp)
            dp[W] = queue2[0] + q * value

            q += 1
            W += weight


# 多重背包问题
def multiple_knapsack(knapsack_size, items):  # items格式: [(num, weight, value), ...]
    dp = [0] * (knapsack_size + 1)
    for num, weight, value in items:
        if num == 1:
            _zero_one_knapsack(dp, knapsack_size, weight, value)
        elif num * weight >= knapsack_size:
            _complete_knapsack(dp, knapsack_size, weight, value)
        else:
            _multiple_knapsack(dp, knapsack_size, num, weight, value)
    return dp[-1]
    

if __name__ == '__main__':
    pass
