#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:29:18 2023

@author: johnmorgan
"""

class UnionFind:
    # Constructor
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1]*n
        
    # Function to find which subset a particular element belongs.
    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
            i = self.parents[i]
        return i
    
    # Function to join two subsets into a single subset.
    def union(self, x, y):
        root_x, root_y = map(self.find, (x, y))
        if root_x == root_y:
            return
        small, big = sorted([root_x, root_y], key=lambda z: self.sizes[z])
        self.parents[small] = big
        self.sizes[big] += self.sizes[small]