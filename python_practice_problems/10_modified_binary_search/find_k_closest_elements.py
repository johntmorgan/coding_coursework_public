#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:16:04 2023

@author: johnmorgan
"""

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
    if (nums[mid] <= num and mid < len(nums) - 1) or mid == 0:
        left = mid
        right = mid + 1
    else:
        left = mid - 1
        right = mid
    while right - left + 1 < k:
        if left == 0:
            right += 1
        if right == len(nums) - 1:
            left -= 1
        else:
            lclose = nums[left - 1]
            rclose = nums[right + 1]
            if abs(num - lclose) <= abs(num - rclose):
                left -= 1
            else:
                right += 1
    return nums[left:right + 1]
    

nums = [1,2,3,4,5]
k = 4
num = 3
print(find_closest_elements(nums, k, num))

nums = [1,2,3,4,5]
k = 4
num = -1
print(find_closest_elements(nums, k, num))

nums = [1, 2, 3, 4, 5, 6, 7]
k = 5 
num = 7
print(find_closest_elements(nums, k, num))

nums = [-10, -6, -4, -3]
k = 2 
num = 5
print(find_closest_elements(nums, k, num))