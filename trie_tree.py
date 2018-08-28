#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/8/19 23:37
#


import collections


class TrieTreeNode(object):

    def __init__(self):
        self.children = collections.defaultdict(TrieTreeNode)
        self.count = 0  # 记录以此节点结尾的单词数


class TrieTree(object):

    def __init__(self):
        self.root = TrieTreeNode()

    def insert(self, word):
        curr = self.root
        for letter in word:
            curr = curr.children[letter]
        curr.count += 1

    def __search_prefix(self, word):
        curr = self.root
        for letter in word:
            curr = curr.children.get(letter)
            if curr is None:
                break
        return curr

    def search(self, word):
        node = self.__search_prefix(word)
        return node is not None and node.count > 0

    def startsWith(self, prefix):
        node = self.__search_prefix(prefix)
        return node is not None


if __name__ == '__main__':
    tt = TrieTree()
    tt.insert('word')
    print(tt.search('word'))
    print(tt.startsWith('wo'))
    print(tt.startsWith('wod'))
