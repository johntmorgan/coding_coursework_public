#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:28:11 2023

@author: johnmorgan
"""

class UnionFind:
    def __init__(self, n):
        triangles = n * 4
        self.parent = []
        self.rank = [1] * triangles
        self.components = triangles
        for i in range(triangles):
            self.parent.append(i)
            
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        else:
            self.components -= 1
            if self.rank[p1] < self.rank[p2]:
                self.parent[p1] = self.parent[p2]
                self.rank[p1] += self.rank[p2]
            else:
                self.parent[p2] = self.parent[p1]
                self.rank[p2] += self.rank[p1]
                