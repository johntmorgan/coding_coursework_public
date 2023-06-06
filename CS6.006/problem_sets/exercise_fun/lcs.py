#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:02:58 2022

@author: johnmorgan
"""

# longest common subsequence, copied
def lcs(A, B):
    a, b = len(A), len(B)
    x = [[0] * (b + 1) for _ in range(a + 1)]
    for i in reversed(range(a)):
        for j in reversed(range(b)):
            if A[i] == B[j]:
                x[i][j] = x[i + 1][j + 1] + 1
            else:
                x[i][j] = max(x[i + 1][j], x[i][j + 1])
    return x[0][0]

# print(lcs("hieroglyphology", "michaelangelo"))

# longest increasing subsequence, copied
def lis(A):
    a = len(A)
    x = [1] * a
    for i in reversed(range(a)):
        for j in range(i, a):
            if A[j] > A[i]:
                x[i] = max(x[i], 1 + x[j])
    return max(x)

# print(lis("carbohydrate"))

# max_subarray_sum suffix version, copied
def max_subarray_sum(A):
    x = [None for _ in A]
    x[0] = A[0]
    for k in range(1, len(A)):
        x[k] = max(A[k], A[k] + x[k - 1])
    print(x)
    return max(x)

# A = [-9, 1, -5, 4, 3, -6, 7, 8, -2]
# print(max_subarray_sum(A))

def max_subarray_sum_prefix(A):
    last_idx = len(A) - 1
    x = [None for _ in A]
    x[last_idx] = A[last_idx]
    for k in reversed(range(last_idx)):
        x[k] = max(A[k], A[k] + x[k + 1])
    return max(x)

# A = [-9, 1, -5, 4, 3, -6, 7, 8, -2]
# print(max_subarray_sum_prefix(A))

       