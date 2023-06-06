#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:17:51 2023

@author: johnmorgan
"""

def find_sum_of_three(arr, target):
    arr.sort()
    for index_1 in range(len(arr)):
        left, right = 0, len(arr) - 1
        while left < right:
            if left == index_1:
                left += 1
            elif right == index_1:
                right -= 1
            else:
                curr_sum = arr[index_1] + arr[left] + arr[right]
                if curr_sum == target:
                    return True
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
    return False

arr = [3,7,1,2,8,4,5]
target = 100
print(find_sum_of_three(arr, target))

arr = [1, 4, 10]
target = 9
