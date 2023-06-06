#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:41:06 2023

@author: johnmorgan
"""

# Note average O(1) for insert, but O(n) worst_case when space reallocated

import random

class RandomSet():
    def __init__(self):
        self.arr = []
        self.hmap = {}
    
    def insert(self, val):
        if val in self.hmap:
            return False
        else:
            self.hmap[val] = len(self.arr)
            self.arr.append(val)
            return True
    
    def delete(self, val):
        if not val in self.hmap:
            return False
        else:
            loc = self.hmap[val]
            end = len(self.arr) - 1
            swap_key = self.arr[end]
            self.arr[loc], self.arr[end] = self.arr[end], self.arr[loc]
            self.hmap[swap_key] = loc
            self.arr.pop()
            del self.hmap[val]
            return True
    
    def get_random(self):
        # return choice(self.store)
        if len(self.arr) == 0:
            return False
        return self.arr[random.randint(0, len(self.arr) - 1)]