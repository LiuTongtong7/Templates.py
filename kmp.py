#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/8/21 00:54
#


# Implement of KMP algorithm
def match_string(query, pattern):
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
    ans = []
    match = -1
    for i in range(len(query)):
        while match >= 0 and query[i] != pattern[match + 1]:
            match = prefix[match]
        if query[i] == pattern[match + 1]:
            match += 1
        if match == len(pattern) - 1:
            ans.append(i - match)
            match = prefix[match]
    return ans


def match_pattern(query, pattern):
    if len(pattern) <= 0:
        return 0

    # 如果只有大写或小写字母，下面的char2index和char_count可以简化，这样设计是为了能处理更多字符
    # 每个char在s中第一次出现的index
    def get_char2index(s):
        char2index = {}
        for i, ch in enumerate(s):
            if ch not in char2index:
                char2index[ch] = i
        return char2index

    # 统计每个char在s[:n]中出现的次数
    # 通过char_count[n2][ch]-char_count[n1][ch]可以得到ch在pattern[n1+1 ... n2]中出现的次数
    def get_char_count(s):
        import copy
        char_count = [{}]
        for i, ch in enumerate(s):
            char_count.append(copy.deepcopy(char_count[i]))
            char_count[i+1].setdefault(ch, 0)
            char_count[i+1][ch] += 1
        return char_count

    char2index = get_char2index(pattern)
    pattern_char_count = get_char_count(pattern)
    query_char_count = get_char_count(query)

    # s[pos-l ... pos-1]已经跟pattern[0 ... l-1]匹配了，判断s[pos]与pattern[l]是否匹配
    def is_match(s, char_count, pos, l):
        if char2index[pattern[l]] < l:
            return s[pos] == s[pos - l + char2index[pattern[l]]]
        else:
            return char_count[pos].get(s[pos], 0) - char_count[pos - l].get(s[pos], 0) == 0

    def compute_prefix(pattern):
        prefix = [-1] * len(pattern)
        last_match = -1
        for i in range(1, len(pattern)):
            while last_match >= 0 and not is_match(pattern, pattern_char_count, i, last_match + 1):
                last_match = prefix[last_match]
            if is_match(pattern, pattern_char_count, i, last_match + 1):
                last_match += 1
            prefix[i] = last_match
        return prefix

    prefix = compute_prefix(pattern)
    ans = []
    match = -1
    for i in range(len(query)):
        while match >= 0 and not is_match(query, query_char_count, i, match + 1):
            match = prefix[match]
        if is_match(query, query_char_count, i, match + 1):
            match += 1
        if match == len(pattern) - 1:
            ans.append(i - match)
            match = prefix[match]
    return ans


if __name__ == '__main__':
    print(match_string('abcbcdcbd', 'cb'))
    print(match_pattern('abcbcd', 'xyx'))
