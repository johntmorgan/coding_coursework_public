#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:09:20 2023

@author: johnmorgan
"""
# Can also do O(n) loop ofc

# O(logn)
# Slow on this, review

def find_floor(lst, low, high, x):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if lst[mid] == x:
            return lst[mid - 1]
        elif mid == len(lst) - 1 and lst[mid] < x:
            return lst[mid]
        elif lst[mid] < x and lst[mid + 1] >= x:
            return lst[mid]
        elif lst[mid] > x:
            return find_floor(lst, low, mid - 1, x)
        else:
            return find_floor(lst, mid + 1, high, x)


def find_ceiling(lst, low, high, x):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if lst[mid] == x:
            return lst[mid + 1]
        elif mid == 0 and lst[mid] > x:
            return lst[mid]
        elif lst[mid] > x and lst[mid - 1] <= x:
            return lst[mid]
        elif lst[mid] > x:
            return find_ceiling(lst, low, mid - 1, x)
        else:
            return find_ceiling(lst, mid + 1, high, x)

def find_floor_ceiling(lst, x):
    # DO NOT MODIFY THIS FUNCTION #

    """
    Calls the find_floor and find_ceiling functions and returns their results
    :param lst: List of integers
    :param x: An integer
    :return: Returns the floor of an integer x, otherwise -1
    """
    return find_floor(lst, 0, len(lst) - 1, x), find_ceiling(lst, 0, len(lst) - 1, x)


lst = [1, 2, 3, 5, 7]
x = 3
print(find_floor_ceiling(lst, x))

lst = [1, 2, 3, 5, 7]
x = 4
print(find_floor_ceiling(lst, x))

lst = [0, 1, 2, 5]
x = 6
print(find_floor_ceiling(lst, x))