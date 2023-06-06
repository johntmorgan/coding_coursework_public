#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:48:02 2023

@author: johnmorgan
"""

# O(n) time complexity, auxiliary lists

def rearrange(lst):
    neg_lst, pos_lst = [],[]
    for elem in lst:
        if elem >= 0:
            pos_lst += [elem]
        else:
            neg_lst += [elem]
    return(neg_lst + pos_lst)

# Swap with leftmost positive element O(n)

# Pythonic, also O(n), loops over twice

def rearrange(lst):
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

input_list = [10,-1,20,4,5,-9,-6]
print(rearrange(input_list))