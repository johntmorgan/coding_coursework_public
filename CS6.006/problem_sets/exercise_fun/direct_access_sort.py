#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:54:26 2022

@author: johnmorgan
"""

def direct_access_sort_key(A):
    "Sort A assuming items have distinct non-negative keys"
    u = 1 + max([x.key for x in A]) # O(n) find maximum key
    D = [None] * u # O(u) direct access array
    for x in A: # O(n) insert items
        D[x.key] = x
    i = 0
    for key in range(u): # O(u) read out items in order
        if D[key] is not None:
            A[i] = D[key]
            i += 1

def direct_access_sort_int(A):
    "Sort A assuming items have distinct non-negative keys"
    u = 1 + max([x for x in A]) # O(n) find maximum key
    D = [None] * u # O(u) direct access array
    for x in A: # O(n) insert items
        D[x] = x
    i = 0
    for key in range(u): # O(u) read out items in order
        if D[key] is not None:
            A[i] = D[key]
            i += 1

array = [2, 4, 5, 3, 1]
print(array)
direct_access_sort_int(array)
print(array)


def counting_sort(A):
    "Sort A assuming items have non-negative keys"
    u = 1 + max([x.key for x in A])
    D = [[] for i in range(u)]
    for x in A:
        D[x.key].append(x)
    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i += 1

def counting_sort_int(A):
    "Sort A assuming items have non-negative keys"
    u = 1 + max([x for x in A])
    D = [[] for i in range(u)]
    for x in A:
        D[x].append(x)
    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i += 1

array = [2, 4, 5, 3, 3, 1]
print(array)
counting_sort_int(array)
print(array)

def radix_sort(A):
    "Sort A assuming items have non-negative keys"
    n = len(A)
    u = 1 + max([x.key for x in A]) # O(n) find maximum key
    c = 1 + (u.bit_length() // n.bit_length())
    class Obj: pass
    D = [Obj() for a in A]
    for i in range(n): # O(nc) make digit tuples
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c): # O(c) make digit tuple
            high, low = divmod(high, n)
            D[i].digits.append(low)
    for i in range(c): # O(nc) sort each digit
        for j in range(n): # O(n) assign key i to tuples
            D[j].key = D[j].digits[i]
        counting_sort(D) # O(n) sort on digit i
    for i in range(n): # O(n) output to A
        A[i] = D[i].item
        
def radix_sort_int(A):
    "Sort A assuming items have non-negative keys"
    n = len(A)
    u = 1 + max([x for x in A]) # O(n) find maximum key
    c = 1 + (u.bit_length() // n.bit_length())
    class Obj: pass
    D = [Obj() for a in A]
    for i in range(n): # O(nc) make digit tuples
        D[i].digits = []
        D[i].item = A[i]
        high = A[i]
        # Can substitute modbase for n
        for j in range(c): # O(c) make digit tuple
            high, low = divmod(high, n)
            # Appends in reverse order from actual digits
            D[i].digits.append(low)
    for i in range(c): # O(nc) sort each digit
        for j in range(n): # O(n) assign key i to tuples
            D[j].key = D[j].digits[i]
        counting_sort(D) # O(n) sort on digit i
    for i in range(n): # O(n) output to A
        A[i] = D[i].item
        
array = [329, 457, 657, 839, 436, 720, 355]
print(array)
radix_sort_int(array)
print(array)

print(divmod(755, 10))
