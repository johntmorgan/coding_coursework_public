#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:39:47 2023

@author: johnmorgan
"""

class UnionFind:
    def __init__(self, grid):
        self.num_islands = 0
        self.parent = []
        self.rank = []
        row_count = len(grid) # number of rows
        col_count = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.num_islands += 1
                    self.parent.append(i * col_count + j)
                else:
                    self.parent.append(-1)
                self.rank.append(0)
                
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return
        else:
            self.num_islands -= 1
            if self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1
            else:
                self.parent[parent_x] = parent_y
                self.rank[parent_y] += 1
                
    def get_count(self):
        return self.num_islands