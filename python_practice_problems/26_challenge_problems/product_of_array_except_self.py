#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:09:17 2023

@author: johnmorgan
"""

# Review

def product(arr):
    res = [1] * len(arr)
    prefix_product = 1
    for i in range(len(arr)):
        res[i] *= prefix_product
        prefix_product *= arr[i]
    suffix_product = 1
    for i in range(len(arr) - 1, -1, -1):
        res[i] *= suffix_product
        suffix_product *= arr[i]
    return res
                

arr = [0,-1,2,-3,4,-2]
print(product(arr))

arr = [5,3,-1,6,4]
print(product(arr))


# Review

# def product(arr):
#     res = [1] * len(arr)
#     for i in range(1, len(arr)):
#         res[i] = res[i - 1] * arr[i - 1]
#     suffix_product = 1
#     for i in range(len(arr) - 1, -1, -1):
#         res[i] *= suffix_product
#         suffix_product *= arr[i]
#     return res


# O(n^2)

# def product(arr):
#     res = [1] * len(arr)
#     for index, num in enumerate(arr):
#         for res_index in range(len(arr)):
#             if res_index != index:
#                 res[res_index] *= num
#     return res


