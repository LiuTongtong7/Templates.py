#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/8/12 15:21
#


class OrderedSet(object):
    m_lst = list()
    m_set = set()
    m_key = None

    def __init__(self, lst=None, key=None):
        self.m_key = key
        if lst is not None:
            self.m_set = set(lst)
            self.m_lst = sorted(self.m_set, key=self.m_key)

    def __contains__(self, val):
        return val in self.m_set

    def front(self):
        return self.m_lst[0] if len(self.m_lst) > 0 else None

    def back(self):
        return self.m_lst[-1] if len(self.m_lst) > 0 else None

    def pop_front(self):
        if len(self.m_lst) > 0:
            val = self.m_lst.pop(0)
            self.m_set.remove(val)
            return val
        else:
            return None

    def pop_back(self):
        if len(self.m_lst) > 0:
            val = self.m_lst.pop(-1)
            self.m_set.remove(val)
            return val
        else:
            return None

    def __bsearch(self, val):
        val_key = self.m_key(val) if self.m_key is not None else val
        left, right = 0, len(self.m_lst) - 1
        while left < right:
            middle = (left + right) >> 1
            middle_key = self.m_key(self.m_lst[middle]) if self.m_key is not None else self.m_lst[middle]
            if middle_key <= val_key:
                left = middle + 1
            else:
                right = middle
        return left

    def insert(self, val):
        if val not in self.m_set:
            self.m_set.add(val)
            pos = self.__bsearch(val)
            self.m_lst.insert(pos, val)


if __name__ == '__main__':
    data = [(2,3), (1,5), (0,4), (1,1)]
    # test __init__
    print(OrderedSet(data).m_lst)
    print(OrderedSet(data, key=lambda x: (x[0], -x[1])).m_lst)

    # test __contains__
    ordered_set = OrderedSet(data)
    print((1,5) in ordered_set)
    print((3,3) in ordered_set)

    # test front, back
    print(ordered_set.front())
    print(ordered_set.back())

    # test pop_front, pop_back
    print(ordered_set.pop_front())
    print(ordered_set.m_lst)
    print(ordered_set.pop_back())
    print(ordered_set.m_lst)

    # test insert
    ordered_set = OrderedSet(key=lambda x: (x[0], -x[1]))
    for d in data:
        ordered_set.insert(d)
    print(ordered_set.m_lst)
