#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:59:25 2023

@author: johnmorgan
"""

from heapq import *
from min_heap import *
from max_heap import *

# Can't figure out balancing while addled by predisone
# Zero course explanation of how to balance - good job guys
# Review (redo) later

# Tip: You may use some of the code templates provided
# in the support files

def median_sliding_window(nums, k):
    medians = []
    maxh = []
    minh = []
    for index in range(k):
        heappush(maxh, -nums[index])
    for index in range(k // 2):
        heappush(minh, -heappop(maxh))
    if k % 2 == 0:
        medians.append((minh[0] + -maxh[0]) / 2)
    else:
        medians.append(-maxh[0])
    count = 0
    balance = 0
    while count < len(nums) - k:
        index = count + k
        print("initial")
        print(minh)
        print(maxh)
        if nums[index] < -maxh[0]:
            heappush(maxh, -nums[index])
        else:
            heappush(minh, nums[index])
        print("push on")
        print(minh)
        print(maxh)
        if nums[index - k] == -maxh[0]:
            heappop(maxh)
        elif nums[index - k] == minh[0]:
            heappop(minh)
        elif nums[index - k] > minh[0]:
            heappush(minh, -heappop(maxh))
        else:
            heappush(maxh, -heappop(minh))
        print("removed rebalanced")
        print(minh)
        print(maxh)
        if k % 2 == 0:
            medians.append((minh[0] + -maxh[0]) / 2)
        else:
            medians.append(-maxh[0])
        count += 1
    return medians

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(median_sliding_window(nums, k))