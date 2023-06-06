#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 7 11:15:42 2022

@author: johnmorgan
"""

# Assuming a SORTED array (doesn't work unsorted)
# Rather than going through each item sequentially (linear time)
# You start in the middle and cut in half each time (log time - log base 2 time)

def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:
      mid = (low + high) // 2
      guess = list[mid]
      if guess == item:
          return mid
      elif guess < item:
          low = mid + 1
      else: # guess > item
          high = mid - 1

print(binary_search(list(range(1,101)), 47))

simple_list = [1, 3, 5, 7, 9]
print (binary_search(simple_list, 3))
print (binary_search(simple_list, 8))

# 1.1
# log2(n) steps
# How many steps for 128 length?
# Math.log(128, 2) = 7

import math
print (math.log(128, 2))
print (math.log(128) / math.log(2))

# 1.2
# Specify base with second param as default is base e
# While in Ruby it's base 10... fun fun
print (math.log(128))
print (math.log(128, 10))

# Double length = 8 steps
print (math.log(256, 2))
