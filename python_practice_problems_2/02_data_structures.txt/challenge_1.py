#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:07:02 2023

@author: johnmorgan
"""

def remove_even(lst):
    pass
    # return [item for item in lst if item % 2 != 0]
    
    # odd_list = []
    # for i in lst:
    #     if i % 2 != 0:
    #         odd_list.append(i)
    # return odd_list

    # odd_list = []
    # for i in lst:
    #     if i % 2 != 0:
    #         odd_list += [i]
    # return odd_list

def remove_even(lst):
    return [item for item in lst if item % 2 != 0]

my_list = [1,2,4,5,10,6,3]
odd_list = remove_even(my_list)
print(odd_list)