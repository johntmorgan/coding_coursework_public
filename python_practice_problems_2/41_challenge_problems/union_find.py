#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:29:54 2023

@author: johnmorgan
"""

class UnionFind:
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        row_ct = len(grid)
        col_ct = len(grid[0])
        for i in range(row_ct):
            for j in range(col_ct):
                if grid[i][j] == 1:
                    self.parent.append(i * row_ct + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)
    
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
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1
    
    def get_count(self):
        return self.count
    
uf = UnionFind([[1, 0], [0, 1]])