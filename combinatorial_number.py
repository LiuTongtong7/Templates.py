#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/10/11 00:41
#


import math


class Combinatorial_number(object):

    def __init__(self, maxn=int(1e6)):
        self.primes = self.get_prime_numbers(maxn)

    @staticmethod
    def get_prime_numbers(maxn):
        flag = [False] * (maxn + 1)
        primes = [2]
        for i in range(3, int(math.sqrt(maxn)) + 1, 2):
            if not flag[i]:
                primes.append(i)
                for j in range(i * i, maxn + 1, i):
                    flag[j] = True
        for i in range(int(math.sqrt(maxn)) + 1, maxn + 1, 2):
            if not flag[i]:
                primes.append(i)
        return primes

    def cal_comb(self, n, m, mod=int(1e9+7)):

        def cal_exp(v, p):
            res, base = 0, p
            while v >= base:
                res += v // base
                base *= p
            return res

        res, i = 1, 0
        while i < len(self.primes) and self.primes[i] <= n:
            exponent = cal_exp(n, self.primes[i]) - cal_exp(m, self.primes[i]) - cal_exp(n - m, self.primes[i])
            res = (res * (self.primes[i] ** exponent)) % mod
            i += 1
        return res

    @staticmethod
    def _cal_comb(n, m, mod=int(1e9+7)):
        res = 1
        i, j = n, 1
        m = min(m, n - m)
        while j <= m:
            res = res * i // j
            i -= 1
            j += 1
        return res % mod


if __name__ == '__main__':
    obj = Combinatorial_number()
    
    import timeit
    print(timeit.timeit('obj.cal_comb(100000, 50000)', number=1, globals=globals()))
    print(timeit.timeit('obj._cal_comb(100000, 50000)', number=1, globals=globals()))
