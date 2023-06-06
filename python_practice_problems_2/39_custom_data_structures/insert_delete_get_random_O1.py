#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:52:24 2023

@author: johnmorgan
"""

import random

# All functions O(1) average - O(n) worst case insert, space reallocated
# O(n) space

class RandomSet():
    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val):
        if val in self.map:
            return False
        else:
            self.map[val] = len(self.arr)
            self.arr.append(val)
            return True

    def delete(self, val):
        if not val in self.map:
            return False
        else:
            loc = self.map[val]
            last = len(self.arr) - 1
            swap_key = self.arr[last]
            self.arr[last], self.arr[loc] = self.arr[loc], self.arr[last]
            self.map[swap_key] = loc
            self.map.pop()
            del self.map[val]
            return True

    def get_random(self):
        if len(self.arr) > 0:   
            # Can also use choice(self.arr) - sol'n notes - JM
            return self.arr[random.randint(0, len(self.arr) - 1)]
        else:
            return False
    

rs = RandomSet()
print(rs.delete(25))
print(rs.insert(50))
print(rs.get_random())