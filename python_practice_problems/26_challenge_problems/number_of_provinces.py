#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:19:38 2023

@author: johnmorgan
"""

class UnionFind():
    def __init__(self, cities):
        self.rank = [1] * cities
        self.count = cities
        self.parent = []
        for i in range(cities):
            self.parent.append(i)
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[x] < self.rank[y]:
                self.parent[px] = self.parent[py]
                self.rank[py] += self.rank[px]
            else:
                self.parent[py] = self.parent[px]
                self.rank[px] = self.rank[py]
            self.count -= 1
        
def find_connected_cities(matrix):
    uf = UnionFind(len(matrix))
    for ri, row in enumerate(matrix):
        for ci, col in enumerate(row):
            if matrix[ri][ci] == 1 and ri != ci:
                uf.union(ri, ci)
    return uf.count