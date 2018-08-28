#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/8/21 00:54
#


# Implement of KMP algorithm
def match_string(target, pattern):
    if len(pattern) <= 0:
        return 0

    def compute_prefix(pattern):
        prefix = [-1] * len(pattern)
        last_match = -1
        for i in range(1, len(pattern)):
            while last_match >= 0 and pattern[i] != pattern[last_match + 1]: 
                last_match = prefix[last_match]
            if pattern[i] == pattern[last_match + 1]:
                last_match += 1
            prefix[i] = last_match
        return prefix

    prefix = compute_prefix(pattern)
    match = -1
    for i in range(len(target)):
        while match >= 0 and target[i] != pattern[match + 1]:
            match = prefix[match]
        if target[i] == pattern[match + 1]:
            match += 1
        if match == len(pattern) - 1:
            return i - match
    return -1
