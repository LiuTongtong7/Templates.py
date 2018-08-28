#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/8/26 18:37
#

import itertools


class Permutation(object):

    # 字典序排列（递归）
    def permute(self, nums):
        # perms = []
        # for i, n in enumerate(nums):
        #     for p in self.permute(nums[:i] + nums[i+1:]):
        #         perms.append([n] + p)
        # return perms or [[]]

        if len(nums) == 0:
            return [[]]
        return [[n] + p 
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])]

    # 非字典序排列（迭代）
    def permute2(self, nums):
        # perms = [[]]
        # for n in nums:
        #     new_perms = []
        #     for p in perms:
        #         for i in range(len(p) + 1):
        #             new_perms.append(p[:i] + [n] + p[i:])
        #     perms = new_perms
        # return perms

        perms = [[]]
        for n in nums:
            perms = [p[:i] + [n] + p[i:]
                     for p in perms
                     for i in range(len(p) + 1)]
        return perms

    # 非字典序排列（迭代）
    def permute_unique(self, nums):
        # perms = [[]]
        # for n in nums:
        #     new_perms = []
        #     for p in perms:
        #         maxi = len(p) - 1 if n not in p else p.index(n)
        #         for i in range(maxi + 1):
        #             new_perms.append(p[:i] + [n] + p[i:])
        #     perms = new_perms
        # return perms

        perms = [[]]
        for n in nums:
            perms = [p[:i] + [n] + p[i:]
                     for p in perms
                     for i in xrange((p + [n]).index(n) + 1)]
        return perms

    def next_permutation(self, nums):
        i = len(nums) - 1
        # 寻找最右的升序对，如果不存在(i==0)，则整个序列为降序
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1
        if i > 0:
            j = i + 1
            while j < len(nums):
                if nums[j] <= nums[i-1]:
                    break
                j += 1
            j -= 1 # nums[j]是大于nums[i-1]的最小的数
            nums[i-1], nums[j] = nums[j], nums[i-1]
        # 将nums[i:]倒序
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
        return nums


# 使用库函数
def permute(nums):
    return list(itertools.permutations(nums))


if __name__ == '__main__':
    obj = Permutation()
    nums = list(range(4))
    print(obj.permute(nums))
    print(obj.permute2(nums))
    print(obj.next_permutation([2,3,4,1]))
    print(permute(nums))
