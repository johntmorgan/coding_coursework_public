#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 18:10:36 2022

@author: johnmorgan
"""

def find_max_subarray(A):
    best_left_index = -1
    best_right_index = -1
    best_sub_value = 0
    tail_index = -1
    tail_sum = 0
    for i in range(len(A)):
        if A[i] > 0:
            if A[i] > best_sub_value:
                best_left_index = i
                best_right_index = i + 1
                best_sub_value = A[i]
                tail_sum = A[i]
                tail_index = i
            else:
                if tail_sum + A[i] > best_sub_value:
                    best_sub_value = tail_sum + A[i]
                    best_left_index = tail_index
                    best_right_index = i + 1
                    tail_sum += A[i]
                elif A[i] > tail_sum:
                    tail_index = i
                    tail_sum = A[i]
        else:
            tail_sum += A[i]
    return best_left_index, best_right_index, best_sub_value

# A1 = [13, -3, -25, 20]
# print(find_max_subarray(A1))
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(find_max_subarray(A))

# This is right, but it sure ain't  linear time.
# Nested loops is O(n^2)
# We are basically doing all the comparisons

# def find_max_subarray_working(A):
#     best_left_index = -1
#     best_right_index = -1
#     best_sub_value = min(A)
#     for i in range(len(A)):
#         best_sub_test_sum = 0
#         best_left_test_index = 0
#         for j in range(best_left_index, i + 1):
#             sub_sum = 0
#             for elem in range(j, i + 1):
#                 sub_sum += A[elem]
#             if sub_sum > best_sub_test_sum:
#                 best_sub_test_sum = sub_sum
#                 best_left_test_index = j
#         if best_sub_test_sum > best_sub_value:
#             best_sub_value = best_sub_test_sum
#             best_left_index = best_left_test_index
#             best_right_index = i
#     return best_left_index, best_right_index, best_sub_value