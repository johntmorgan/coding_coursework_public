#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:23:28 2023

@author: johnmorgan
"""

class UnionFind:
    def __init__(self, grid):
        n = len(grid) * len(grid[0])
        self.rank = [1] * n
        self.parent = []
        self.count = 0
        len_row = len(grid[0])
        for ri, row in enumerate(grid):
            for ci, col in enumerate(row):
                val = ri * len_row + ci
                if grid[ri][ci] == 1:
                    self.parent.append(val)
                    self.count += 1
                else:
                    self.parent.append(-1)
    
    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find_parent(x), self.find_parent(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = self.parent[py]
                self.rank[py] += self.rank[px]
            else:
                self.parent[py] = self.parent[px]
                self.rank[px] += self.rank[py]
            self.count -= 1

    def no_decrement_union(self, x, y):
        px, py = self.find_parent(x), self.find_parent(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = self.parent[py]
                self.rank[py] += self.rank[px]
            else:
                self.parent[py] = self.parent[px]
                self.rank[px] += self.rank[py]

    def get_count(self):
        return self.count
    
def shortest_bridge(grid):
    uf = UnionFind(grid)
    len_row = len(grid[0])
    for ri, row in enumerate(grid):
        for ci, col in enumerate(row):
            val = ri * len_row + ci
            if grid[ri][ci] == 1:
                if ri > 0 and grid[ri - 1][ci] == 1:
                    uf.union(val, val - len_row)
                if ri < len(grid) - 1 and grid[ri + 1][ci] == 1:
                    uf.union(val, val + len_row)                   
                if ci > 0 and grid[ri][ci - 1] == 1:
                    uf.union(val, val - 1)
                if ci < len_row - 1 and grid[ri][ci + 1] == 1:
                    uf.union(val, val + 1)
    parents = []
    for index, val in enumerate(uf.parent):
        if uf.parent[index] != -1 :
            curr_parent = uf.find_parent(val)
            if curr_parent not in parents:
                parents.append(curr_parent)
    start = parents[0]
    target = parents[1]
    min_flipped = 0
    while uf.get_count() > 1:
        seeds = []
        for ri, row in enumerate(grid):
            for ci, col in enumerate(row):
                val = ri * len_row + ci
                for index, parent in enumerate(uf.parent):
                    if parent == start and index not in seeds:
                        seeds.append(index)
        targets = []
        for ri, row in enumerate(grid):
            for ci, col in enumerate(row):
                val = ri * len_row + ci
                for index, parent in enumerate(uf.parent):
                    if parent == target and index not in targets:
                        targets.append(index)
        for ri, row in enumerate(grid):
            for ci, col in enumerate(row):
                val = ri * len_row + ci
                if val in seeds:
                    if ri > 0 and grid[ri - 1][ci] == 0:
                        grid[ri - 1][ci] = 1
                        uf.parent[val - len_row] = val - len_row
                        uf.no_decrement_union(val, val - len_row)
                    if ri < len(grid) - 1 and grid[ri + 1][ci] == 0:
                        grid[ri + 1][ci] = 1
                        uf.parent[val + len_row] = val + len_row
                        uf.no_decrement_union(val, val + len_row)                   
                    if ci > 0 and grid[ri][ci - 1] == 0:
                        grid[ri][ci - 1] = 1
                        uf.parent[val - 1] = val - 1
                        uf.no_decrement_union(val, val - 1)
                    if ci < len_row - 1 and grid[ri][ci + 1] == 0:
                        grid[ri][ci + 1] = 1
                        uf.parent[val + 1] = val + 1
                        uf.no_decrement_union(val, val + 1)
        for ri, row in enumerate(grid):
            for ci, col in enumerate(row):
                val = ri * len_row + ci
                if val in targets:
                    if ri > 0 and grid[ri - 1][ci] == 1:
                        uf.union(val, val - len_row)
                    if ri < len(grid) - 1 and grid[ri + 1][ci] == 1:
                        uf.union(val, val + len_row)                   
                    if ci > 0 and grid[ri][ci - 1] == 1:
                        uf.union(val, val - 1)
                    if ci < len_row - 1 and grid[ri][ci + 1] == 1:
                        uf.union(val, val + 1)
        min_flipped += 1
    return min_flipped
    

grid = [[0,1,1],[1,0,1],[1,0,1]]
print(shortest_bridge(grid))

grid = [[1, 0, 0], [1, 0, 0], [0, 0, 1]]
print(shortest_bridge(grid))

grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
print(shortest_bridge(grid))