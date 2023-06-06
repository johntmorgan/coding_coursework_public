#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 18:06:34 2023

@author: johnmorgan
"""

def can_partition_array(nums):
    if len(nums) == 0:
        return True
    num_sum = sum(nums)
    if num_sum % 2 != 0:
        return False
    half_sum = num_sum // 2
    matrix = [[0 for i in range(len(nums) + 1)] for j in range(half_sum + 1)]
    for i in range(len(nums) + 1):
        matrix[0][i] = 1
    for j in range(1, half_sum + 1):
        matrix[j][0] = 0
    for i in range(1, half_sum + 1):
        for j in range(1, len(nums) + 1):
            if nums[j - 1] > i:
                matrix[i][j] = matrix[i][j - 1]
            else:
                matrix[i][j] = matrix[i][j - 1] or matrix[i - nums[j - 1]][j - 1]
    return bool(matrix[half_sum][len(nums)])

nums = [1,2,3,4]
print(can_partition_array(nums))

nums = [3,1,1,2,2,1]
print(can_partition_array(nums))

nums = [9,1,1,2,2,1]
print(can_partition_array(nums))

def can_partition_array(nums):
    if len(nums) == 0:
        return True
    t_sum = sum(nums)
    # If odd total, can't possibly split
    if t_sum % 2 != 0:
        return False
    # Can you add some combo up to 1/2 the sum?
    s_sum = t_sum // 2
    matrix = [[0 for i in range(len(nums) + 1)] for j in range(s_sum + 1)]
    # You can always sum to 0, take no values
    for i in range(0, len(nums) + 1):
        matrix[0][i] = 1
    # If you take zero values it never sums to anything > 0
    for i in range(1, s_sum + 1):
        matrix[i][0] = 0
    # Building up from this baseline
    for i in range(1, s_sum + 1):
        for j in range(1, len(nums) + 1):
            # If the number added is greater than the sum at this level, it never helps
            # See if you can already get without that number
            if nums[j - 1] > i:
                matrix[i][j] = matrix[i][j - 1]
            # If the number added is less than or equal to sum
            # Then it can either help or not help
            # No help: see above
            # Help: The value at sum minus this number (so vertically up) may be used instead
            else:
                matrix[i][j] = matrix[i - nums[j - 1]][j - 1] or matrix[i][j - 1]
    print(matrix)
    return bool(matrix[s_sum][len(nums)])