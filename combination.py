#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/8/26 18:37
#

import copy
import itertools


class Combination(object):

    # 迭代
    def combine(self, nums, k):
        # n = len(nums)
        # combs = [(0, [])]
        # for end_idx in range(n - k, n):
        #     new_combs = []
        #     for begin_idx, c in combs:
        #         for i in range(begin_idx, end_idx + 1):
        #             new_combs.append((i + 1, c + [nums[i]]))                    
        #     combs = new_combs
        # return [c for i, c in combs]

        n = len(nums)
        combs = [(0, [])]
        for end_idx in range(n - k, n):
            combs = [(i + 1, c + [nums[i]]) 
                     for begin_idx, c in combs 
                     for i in range(begin_idx, end_idx + 1)]
        return [c for i, c in combs]

    # 递归
    def combine2(self, nums, k):
        # if k == 0:
        #     return [[]]
        # n = len(nums)
        # combs = []
        # for i in range(n - k + 1):
        #     for c in self.combine2(nums[i+1:], k - 1):
        #         combs.append([nums[i]] + c)
        # return combs

        if k == 0:
            return [[]]
        n = len(nums)
        return [[nums[i]] + c
                for i in range(n - k + 1) 
                for c in self.combine2(nums[i+1:], k - 1)]

    # 将nums分为等大小的k份, 要求len(nums) % k == 0
    def combine_whole(self, nums, k):

        def dfs(nums, pos, temp, combs):
            if pos >= len(nums):
                combs.append(copy.deepcopy(temp))
                return

            n, k = len(nums), len(temp)
            n1 = n // k
            for i in range(k):
                if len(temp[i]) == n1:
                    continue
                temp[i].append(nums[pos])
                dfs(nums, pos + 1, temp, combs)
                temp[i].pop(-1)

        combs = []
        temp = [[] for _ in range(k)]
        dfs(nums, 0, temp, combs)
        return combs


# 使用库函数
def combine(nums, k):
    return list(itertools.combinations(nums, k))


if __name__ == '__main__':
    obj = Combination()
    nums, k = list(range(6)), 3
    print(obj.combine(nums, k))
    print(obj.combine2(nums, k))
    print(combine(nums, k))
    print(len(obj.combine_whole(nums, k)))
