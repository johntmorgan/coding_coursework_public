#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:20:42 2023

@author: johnmorgan
"""

# Naive: three nested loops
# Each nested loop starts at index one greater than parent loop
# O(n^3)

# Good solution
# Sort array: O(nlogn)
# Nested loop: n * O(n) -> O(n^2)
# Space complexity depends on sort
# Python sort O(n) space complexity

def find_sum_of_three(nums, target):
    nums.sort()
    low, high = 1, len(nums) - 1
    curr = 0
    while curr < len(nums):
        while low < high:
            curr_sum = nums[curr] + nums[low] + nums[high]
            if curr_sum == target:
                return True
            elif curr_sum < target:
                low += 1
            else:
                high -= 1
        curr += 1
        low = curr + 1
        high = len(nums) - 1
    return False
    

nums, target = [1,-1,0] , -1
print(find_sum_of_three(nums, target))
nums, target = [3,7,1,2,8,4,5] , 10
print(find_sum_of_three(nums, target))
nums, target = [3,7,1,2,8,4,5] , 20
print(find_sum_of_three(nums, target))
nums, target = [3,7,1,2,8,4,5] , 21
print(find_sum_of_three(nums, target))
nums, target = [-1,2,1,-4,5,-3] , -8
print(find_sum_of_three(nums, target))
nums, target = [-1,2,1,-4,5,-3] , 0
print(find_sum_of_three(nums, target))
nums, target = [-1,2,1,-4,5,-3] , 7
print(find_sum_of_three(nums, target))