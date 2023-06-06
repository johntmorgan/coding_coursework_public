#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:15:25 2023

@author: johnmorgan
"""

# O(n^2), nested loop

def find_pair(my_list):
    dict1 = {}
    for elem in my_list:
        for elem2 in my_list:
            if elem != elem2:
                esum = elem + elem2
                if esum not in dict1:
                    dict1[esum] = (elem, elem2)
                elif dict1[esum] == (elem2, elem):
                    pass
                else:
                    output = [[elem, elem2], [dict1[esum][0], dict1[esum][1]]]
                    output.sort()
                    return output
    return "Not found"

my_list = [3, 4, 7, 1, 12, 9]
print(find_pair(my_list))