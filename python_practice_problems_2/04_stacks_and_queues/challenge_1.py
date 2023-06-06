#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:12:41 2023

@author: johnmorgan
"""

from Queue import MyQueue

# Time complexity is O(n)

def find_bin(number):
    result = []
    queue = MyQueue()
    queue.enqueue("1")
    for _ in range(number):
        new_str = queue.dequeue()
        result += [new_str]
        queue.enqueue(new_str + "0")
        queue.enqueue(new_str + "1")
    return result

print(find_bin(3))
print(find_bin(5))
print(find_bin(7))