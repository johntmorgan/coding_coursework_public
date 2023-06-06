#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:25:18 2023

@author: johnmorgan
"""

def get_k_sum_subsets(set_of_integers, target_sum):
    subsets = [[]]
    for elem in set_of_integers:
        if elem <= target_sum:
            for index in range(len(subsets)):
                subsets.append(subsets[index] + [elem])
    result = []
    for subset in subsets:
        sub_sum = 0
        for elem in subset:
            sub_sum += elem
        if sub_sum == target_sum:
            result.append(subset)
    return result


nums = [8,13,3,22,17,39,87,45,36]
target = 47

print(get_k_sum_subsets(nums, target))