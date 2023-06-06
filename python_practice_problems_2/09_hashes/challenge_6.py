#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:38:15 2023

@author: johnmorgan
"""

# O(n^2) with list

def find_sub_zero(my_list):
    sum_list = []
    for elem in my_list:
        if elem == 0:
            return True
        for index in range(len(sum_list)):
            new_sum = sum_list[index] + elem
            if new_sum == 0:
                return True
            else:
                sum_list[index] = new_sum
        sum_list.append(elem)
    return False

# O(n) with dict 
# Review this

def find_sub_zero(my_list):
    sum_dict = dict()
    total_sum = 0
    for elem in my_list:
        total_sum += elem
        # If sum_dict.get total_sum is zero, there has been a set of numbers adding to 0
        if elem is 0 or total_sum is 0 or sum_dict.get(total_sum) is not None:
            return True
        sum_dict[total_sum] = elem
    return False


zero_sub = [6, 4, -7, 3, 12, 9]
print(find_sub_zero(zero_sub))
no_zero = [-7, 4, 6, 3, 12, 9]
print(find_sub_zero(no_zero))