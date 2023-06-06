#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:16:10 2023

@author: johnmorgan
"""

# Top row, sum to zero
# Left col, no items used
# Still can't really picture what is going on here - lousy prednisone
# Redo with unscrambled brain

# O(n*s) space
# O(n*s) time

def can_partition_array(nums):
    num_sum = sum(nums)
    if num_sum % 2 != 0:
        return False
    target = num_sum // 2
    matrix = [[0 for _ in range(len(nums) + 1)] for _ in range(target + 1)]
    for index in range(len(matrix[0])):
        matrix[0][index] = 1
    for index in range(1, len(matrix)):
        matrix[index][0] = 0
    for i in range(1, target + 1):
        for j in range(1, len(nums) + 1):
            if nums[j - 1] > i:
                matrix[i][j] = matrix[i][j - 1]
            else:
                matrix[i][j] = matrix[i - nums[j - 1]] or matrix[i][j - 1]
    return bool(matrix[target][len(nums)])

nums = [3,1,1,2,2,1]
print(can_partition_array(nums))

