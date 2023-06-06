#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:10:50 2023

@author: johnmorgan
"""

def four_sum(arr, target):
    result = []
    pairs = {}
    for index, num in enumerate(arr):
        for c_index, c_num in enumerate(arr):
            if index != c_index:
                two_sum = num + c_num
                if two_sum in pairs:
                    if (index, c_index) not in pairs[two_sum] and \
                        (c_index, index) not in pairs[two_sum]:
                        pairs[two_sum] += [(index, c_index)]
                else:
                    pairs[two_sum] = [(index, c_index)]
    four_sums = {}
    for two_sum in pairs.keys():
        if target - two_sum in four_sums.keys() or target == two_sum:
            complement = target - two_sum
            for pair1 in pairs[complement]:
                for pair2 in pairs[two_sum]:
                    if pair2[0] not in pair1 and pair2[1] not in pair1:
                        sort_append = [arr[pair1[0]], arr[pair1[1]],
                                       arr[pair2[0]], arr[pair2[1]]]
                        sort_append.sort()
                        if sort_append not in result:
                            result.append(sort_append)
        else:
            four_sums[two_sum] = target
    result.sort()
    return result

# arr = [1,2,-1,0,-2,2]
# target = 0
# print(four_sum(arr, target))

arr = [0, 0, 0, 0]
target = 0
print(four_sum(arr, target))