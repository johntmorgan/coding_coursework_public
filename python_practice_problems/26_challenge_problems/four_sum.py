#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:02:54 2023

@author: johnmorgan
"""

def four_sum(arr, target):
    pairs = {}
    for i, num in enumerate(arr):
        for ci, cnum in enumerate(arr):
            if i != ci:
                two_sum = num + cnum
                if two_sum in pairs and (i, ci) not in pairs[two_sum] and \
                    (ci, i) not in pairs[two_sum]:
                    pairs[two_sum] += [(ci, i)]
                elif two_sum not in pairs:
                    pairs[two_sum] = [(i, ci)]
    result = []
    for two_sum in pairs:
        if target - two_sum in pairs:
            complement = target - two_sum
            for pair1 in pairs[complement]:
                for pair2 in pairs[two_sum]:
                    if pair2[0] not in pair1 and pair2[1] not in pair1:
                        sort_append = [arr[pair1[0]], arr[pair1[1]],
                                       arr[pair2[0]], arr[pair2[1]]]
                        sort_append.sort()
                        if sort_append not in result:
                            result.append(sort_append)
    result.sort()
    return result
                    

# arr = [1,2,-1,0,-2,2]
# target = 0
# print(four_sum(arr, target))

arr = [0, 0, 0, 0]
target = 0
print(four_sum(arr, target))
