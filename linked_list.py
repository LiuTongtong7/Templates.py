#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by liutongtong on 2018/9/26 01:06
#


class ListNode(object):
    val = None
    prev, next = None, None

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)


class DoubleLinkedList(object):
    head, tail = None, None
    count = 0

    def __init__(self):
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def size(self):
        return self.count

    def append(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.count += 1

    def appendleft(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        self.count += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.count -= 1
        return node

    def pop(self):
        return self.remove(self.tail.prev) if self.count > 0 else None

    def popleft(self):
        return self.remove(self.head.next) if self.count > 0 else None

    def print(self):
        res = str(self.head.val) + ' '
        node = self.head.next
        while node != self.tail:
            res += str(node.val) + ' '
            node = node.next
        res += str(self.tail.val)
        print(res)


if __name__ == '__main__':
    dll = DoubleLinkedList()
    for i in range(1, 5):
        dll.append(ListNode(i))
    node = ListNode(5)
    dll.appendleft(node)
    for i in range(6, 10):
        dll.appendleft(ListNode(i))
    dll.print()
    for _ in range(1, 4):
        print(dll.pop())
    for _ in range(1, 4):
        print(dll.popleft())
    print(dll.remove(node))
    dll.print()
