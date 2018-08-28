#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# Created by liutongtong on 2018/8/12 15:21
#


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(1, n - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap //= 2
    return arr


def merge_sort(arr):
    n = len(arr)
    a, b = arr, [0] * n
    width = 1
    while width < n:
        for start in range(0, n, width * 2):
            left, middle, right = start, min(start + width, n), min(start + width * 2, n)
            l, r = left, middle
            for i in range(left, right):
                if l < middle and (r >= right or a[l] <= a[r]):
                    b[i] = a[l]
                    l += 1
                else:
                    b[i] = a[r]
                    r += 1
        a, b = b, a
        width *= 2
    return arr


def merge_sort2(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        l, r = 0, 0
        result = list()
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        result += left[l:]
        result += right[r:]
        return result

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


def quick_sort(arr):
    range_stack = list()
    range_stack.append([0, len(arr) - 1])
    while range_stack:
        left, right = range_stack.pop()
        if left >= right:
            continue
        pivot = arr[right]
        l, r = left, right
        while l < r:
            while arr[l] < pivot and l < r:
                l += 1
            while arr[r] >= pivot and l < r:
                r -= 1
            arr[l], arr[r] = arr[r], arr[l]
        arr[l], arr[right] = arr[right], arr[l]
        range_stack.append([left, l - 1])
        range_stack.append([l + 1, right])
    return arr


def quick_sort2(arr):
    def qsort(arr, left, right):
        if left >= right:
            return arr
        pivot = arr[right]
        l, r = left, right
        while l < r:
            while arr[l] < pivot and l < r:
                l += 1
            while arr[r] >= pivot and l < r:
                r -= 1
            arr[l], arr[r] = arr[r], arr[l]
        arr[l], arr[right] = arr[right], arr[l]
        qsort(arr, left, l - 1)
        qsort(arr, l + 1, right)
        return arr

    return qsort(arr, 0, len(arr) - 1)


def heap_sort(arr):
    def max_heapify(arr, left, right):
        parent = left
        child = left * 2 + 1
        while child <= right:
            if child + 1 <= right and arr[child] < arr[child + 1]:
                child += 1
            if arr[parent] > arr[child]:
                break
            else:
                arr[parent], arr[child] = arr[child], arr[parent]
                parent, child = child, child * 2 + 1

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n - 1)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i - 1)
    return arr


def counting_sort(arr):
    if len(arr) <= 0:
        return arr

    n = len(arr)
    minv, maxv = min(arr), max(arr)
    b = [0] * n
    c = [0] * (maxv - minv + 1)
    for i in range(n):
        c[arr[i] - minv] += 1
    for i in range(1, len(c)):
        c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        val = arr[i]
        b[c[val - minv] - 1] = val
        c[val - minv] -= 1
    return b


def radix_sort(arr, radix=10):
    if len(arr) <= 0:
        return arr

    import math
    max_bit = int(math.ceil(math.log(max(arr) + 1, radix)))
    mask = 1
    for i in range(1, max_bit + 1):
        bucket = [[] for _ in range(radix)]
        for val in arr:
            bucket[(val // mask) % radix].append(val)
        del arr[:]
        for b in bucket:
            arr.extend(b)
        mask *= radix
    return arr


if __name__ == '__main__':
    arr = [4,6,2,7,8,1,5,3,9]
    # print(bubble_sort(arr))
    # print(selection_sort(arr))
    # print(insertion_sort(arr))
    # print(shell_sort(arr))
    # print(merge_sort(arr))
    # print(merge_sort2(arr))
    # print(quick_sort(arr))
    # print(quick_sort2(arr))
    # print(heap_sort(arr))
    # print(counting_sort(arr))
    print(radix_sort(arr))
