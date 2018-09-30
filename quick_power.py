#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by liutongtong on 2018/9/30 15:00
#


# 快速幂，效率不如 val ** n
def quick_pow(val, n, mod=None):
    if mod is None:
        res = 1
        base = val
        while n > 0:
            if n & 1:
                res *= base
            base *= base
            n >>= 1
        return res
    else:
        res = 1
        base = val % mod
        while n > 0:
            if n & 1:
                res = (res * base) % mod
            base = (base * base) % mod
            n >>= 1
        return res


# 矩阵快速幂
def quick_pow_matrix(matrix, n, mod=None):

    def multiply(m1, m2, mod=None):
        r = [[0, 0], [0, 0]]
        if mod is None:
            for i in range(2):
                for j in range(2):
                    r[i][j] = m1[i][0] * m2[0][j] + m1[i][1] * m2[1][j]
        else:
            for i in range(2):
                for j in range(2):
                    r[i][j] = (m1[i][0] * m2[0][j] + m1[i][1] * m2[1][j]) % mod
        return r

    res = [[1, 0], [0, 1]]
    base = matrix
    while n > 0:
        if n & 1:
            res = multiply(res, base, mod=mod)
        base = multiply(base, base, mod=mod)
        n >>= 1
    return res


# 用于求递推公式 f(n) = a*f(n-1) + b*f(n-2)
# [f(n), f(n-1)] = [[a, b], [1, 0]]^(n-2) [f(2), f(1)]
def recurse(a, b, f1, f2, n, mod=None):
    if n <= 2:
        res = f2 if n == 2 else f1
        if mod is not None:
            res %= mod
        return res

    coef = quick_pow_matrix([[a, b], [1, 0]], n - 2, mod=mod)
    res = coef[0][0] * f2 + coef[0][1] * f1
    if mod is not None:
        res %= mod
    return res


if __name__ == '__main__':
    import timeit, time
    print(quick_pow(2, 127), 2 ** 127)
    print(timeit.timeit('quick_pow(2, 127); quick_pow(3, 127)', number=1, globals=globals()))
    print(timeit.timeit('2 ** 127; 3 ** 127', number=1, globals=globals()))
    
    # 斐波拉契数
    start = time.time()
    f1, f2 = 1, 1
    mod = int(1e9 + 7)
    for _ in range(3, 1001):
        f1, f2 = f2, (f1 + f2) % mod
    print(f2, time.time() - start)

    start = time.time()
    print(recurse(1, 1, 1, 1, 1000, mod=mod), time.time() - start)


