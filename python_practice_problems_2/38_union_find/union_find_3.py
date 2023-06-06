#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:28:18 2023

@author: johnmorgan
"""

class UnionFind:
    # Initialise the 1D array
    def __init__(self, N):
        self.parent = []
        self.rank = rank = [0] * (N + 1)
        for i in range(N + 1):
            self.parent.append(i)

    def find(self, x):
        print("\tUpdated array after finding the parent of",
              x, ":",  self.parent)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # returns false if both vertices have the same parent, otherwise, updates the parent and rank lists by making a connection based on the passed edge
    # true will be returned if no cycle exits in the graph
    def union(self, v1, v2):
        #finds the root parents of both v1 and v2
        p1, p2 = self.find(v1), self.find(v2)
        #if both parents are the same, a cycle exists and v1,v2 is the redundant edge
        if p1 == p2:
            return False
        #updates the parent and rank lists otherwise 
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] = self.rank[p1] + self.rank[p2]
            
        else:
            self.parent[p1] = p2
            self.rank[p2] = self.rank[p2] + self.rank[p1]
            
        print("\tUpdated array after connecting cells :", self.parent)
        
        return True


    # Mapping 2D array to 1D array to perform union find operations
    def find_index(self, x, y, col):
        # +1 because starting from index 0
        return x * col + (y + 1)