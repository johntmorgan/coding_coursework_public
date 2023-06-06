#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:45:08 2023

@author: johnmorgan
"""

# O(logn + k) (plus I did an O(klogk) sort at the end - JM)
# O(1) space, don't count output array

def find_closest_elements(nums, k, num):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == num:
            break
        elif nums[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    if nums[mid] == mid:
        left = mid - 1
        right = mid
    else:
        left = mid
        right = mid + 1
    result = []
    while k > 0:
        if right > len(nums) - 1 or abs(nums[left] - num) <= abs(nums[right] - num):
            result.append(nums[left])
            left -= 1
        else:
            result.append(nums[right])
            right += 1
        k -= 1
    result.sort()
    return result


nums = [1,2,3,4,5]
k = 4
num = 3
print(find_closest_elements(nums, k, num))

nums = [1,2,4,5,6]
k = 4
num = 3
print(find_closest_elements(nums, k, num))