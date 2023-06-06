#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:01:51 2023

@author: johnmorgan
"""

from min_heap import *
from max_heap import *
from collections import defaultdict

def median_sliding_window(nums, k):
    output = []
    outgoing_num = defaultdict(int)
    small_heap = max_heap()
    large_heap = min_heap()
    for i in range(0, k):
        small_heap.insert(nums[i])
    for i in range(0, k // 2):
        large_heap.insert(small_heap.pop())
    i = k
    while True:
        if k % 2 == 0:
            output.append((small_heap.get_max() + large_heap.get_min()) / 2.0)
        else:
            output.append(float(small_heap.get_max()))
        if i >= len(nums):
            break
        out_num = nums[i - k]
        in_num = nums[i]
        outgoing_num[out_num] += 1
        balance = 0
        if out_num <= small_heap.get_max():
            balance -= 1
        else:
            balance += 1
        if small_heap and in_num < small_heap.get_max():
            small_heap.insert(in_num)
            balance += 1
        else:
            large_heap.insert(in_num)
            balance -= 1
        if balance < 0:
            small_heap.insert(large_heap.pop())
        elif balance > 0:
            large_heap.insert(small_heap.pop())
        while small_heap.get_max() in outgoing_num and outgoing_num[small_heap.get_max()] > 0:
            small_heap.pop()
            outgoing_num[small_heap.get_max()] -= 1
        while large_heap.get_min() in outgoing_num and outgoing_num[large_heap.get_min()] > 0:
            large_heap.pop()
            outgoing_num[large_heap.get_min()] -= 1
        i += 1    
    return output

# Copied
# Review again

# from heapq import *

# def median_sliding_window(nums, k):
#     medians = []
#     outgoing_num = {}
#     small_list = []
#     large_list = []
#     for i in range(0, k):
#         heappush(small_list, -1 * nums[i])
#     for i in range(0, k//2):
#         element = heappop(small_list)
#         heappush(large_list, -1 * element)
#     i = k
#     while True:
#         if (k & 1) == 1:
#             medians.append(float(small_list[0] * -1))
#         else:
#             medians.append((float(small_list[0] * -1) + float(large_list[0])) * 0.5)
#         if i >= len(nums):
#             break
#         out_num = nums[i - k]
#         in_num = nums[i]
#         i += 1
#         balance = 0
#         if out_num <= (small_list[0] * -1):
#             balance -= 1
#         else:
#             balance += 1
#         if out_num in outgoing_num:
#             outgoing_num[out_num] = outgoing_num[out_num] + 1
#         else:
#             outgoing_num[out_num] = 1
#         if small_list and in_num <= (small_list[0] * -1):
#             balance += 1
#             heappush(small_list, in_num * -1)
#         else:
#             balance -= 1
#             heappush(large_list, in_num)
#         if balance < 0:
#             heappush(small_list, (-1 * large_list[0]))
#             heappop(large_list)
#         elif balance > 0:
#             heappush(large_list, (-1 * small_list[0]))
#             heappop(small_list)
#         while (small_list[0] * -1) in outgoing_num and (outgoing_num[(small_list[0] * -1)] > 0):
#             outgoing_num[small_list[0] * -1] = outgoing_num[small_list[0] * -1] - 1
#             heappop(small_list)
#         while large_list and large_list[0] in outgoing_num and (outgoing_num[large_list[0]] > 0):
#             outgoing_num[large_list[0]] = outgoing_num[large_list[0]] - 1
#             heappop(large_list)
#     return medians


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(median_sliding_window(nums, k))