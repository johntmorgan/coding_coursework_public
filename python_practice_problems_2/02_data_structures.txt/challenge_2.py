#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:07:39 2023

@author: johnmorgan
"""

# def merge_lists(lst1, lst2):
#     merge = []
#     while len(lst1) > 0 or len(lst2) > 0:
#         if len(lst1) == 0:
#             merge.append(lst2.pop(0))
#         elif len(lst2) == 0:
#             merge.append(lst1.pop(0))
#         else:
#             if lst1[0] < lst2[0]:
#                 merge.append(lst1.pop(0))
#             else:
#                 merge.append(lst2.pop(0))
#     return merge

# list1 = [1,3,4,5]  
# list2 = [2,6,7,8]

# merged_list = merge_lists(list1, list2)
# print(merged_list)

def merge_lists_no_destroy(lst1, lst2):
    merge = []
    len1, len2 = len(lst1), len(lst2)
    lst1_idx, lst2_idx = 0, 0
    for _ in range(len1 + len2):
        if lst1_idx == len1:
            merge.extend(lst2[lst2_idx:])
            break
        elif lst2_idx == len2:
            merge.extend(lst1[lst1_idx:])
            break
        else:
            if lst1[lst1_idx] < lst2[lst2_idx]:
                merge.append(lst1[lst1_idx])
                lst1_idx += 1
            else:
                merge.append(lst2[lst2_idx])
                lst2_idx += 1
    return merge

list1 = [1,3,4,5]  
list2 = [2,6,7,8]

merged_list = merge_lists_no_destroy(list1, list2)
print(merged_list)
print(list1)
print(list2)