#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:02:05 2023

@author: johnmorgan
"""

# Review - still need just a hair more practice - slightly sloppy recreating
# basic UF pattern

class UnionFind:
    def __init__(self, cities):
        self.rank = [0] * cities
        self.count = cities
        self.parent = []
        for i in range(cities):
            self.parent.append(i)
            
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1
            
def find_connected_cities(matrix):
    uf = UnionFind(len(matrix))
    for r_index, row in enumerate(matrix):
        for c_index in range(len(row)):
            if matrix[r_index][c_index] == 1 and r_index != c_index:
                uf.union(r_index, c_index)
    return uf.count


matrix = [[1,1,0],[1,1,0],[0,0,1]]
print(find_connected_cities(matrix))