#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:25:46 2023

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

def shortest_bridge(grid):
    ugrid = UnionFind(grid)
    row_len = len(grid[0])
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if grid[row_index][col_index] == 1:
                val = row_index * row_len + col_index
                if row_index > 0:
                    if grid[row_index - 1][col_index] == 1:
                        ugrid.union(val, val - row_len)
                if row_index < len(grid) - 1:
                    if grid[row_index + 1][col_index] == 1:
                        ugrid.union(val, val + row_len)
                if col_index > 0:
                    if grid[row_index][col_index - 1] == 1:
                        ugrid.union(val, val - 1)
                if col_index < row_len - 1:
                    if grid[row_index][col_index + 1] == 1:
                        ugrid.union(val, val + 1)
    par_val = -1
    index = 0
    while par_val < 0:
        par_val = ugrid.parent[index]
        if par_val < 0:
            index += 1
    squares_added = 0
    while ugrid.get_count() > 1:
        island = []
        for index in range(len(ugrid.parent)):
            if ugrid.parent[index] == par_val:
                island.append(index)
        island_squares = []
        for island_sq in island:
            row_index = island_sq // row_len
            col_index = island_sq - row_index * row_len
            island_squares.append([row_index, col_index])
        for isq in island_squares:
            ri, ci = isq[0], isq[1]
            val = ri * row_len + ci
            if ri > 0:
                if grid[ri - 1][ci] == 0:
                    grid[ri - 1][ci] = 1
                    ugrid.parent[val - row_len] = ugrid.parent[val]
                    ugrid.union(val, val - row_len)
                    if ri - 1 > 0 and grid[ri - 2][ci] == 1:
                        ugrid.union(val - row_len, val - (2 * row_len))
                    if ci > 0 and grid [ri - 1][ci - 1] == 1:
                        ugrid.union(val - row_len, val - row_len - 1)
                    if ci < (row_len - 1) and grid[ri - 1][ci + 1] == 1:
                        ugrid.union(val - row_len, val - row_len + 1)
            if ri < len(grid) - 1:
                if grid[ri + 1][ci] == 0:
                    grid[ri + 1][ci] = 1
                    ugrid.parent[val + row_len] = ugrid.parent[val]
                    ugrid.union(val, val + row_len)
                    if ri + 1 < len(grid) - 1 and grid[ri + 2][ci] == 1:
                        ugrid.union(val + row_len, val + (2 * row_len))
                    if ci > 0 and grid [ri + 1][ci - 1] == 1:
                        ugrid.union(val + row_len, val + row_len - 1)
                    if ci < (row_len - 1) and grid[ri + 1][ci + 1] == 1:
                        ugrid.union(val + row_len, val + row_len + 1)
            if ci > 0:
                if grid[ri][ci - 1] == 0:
                    grid[ri][ci - 1] = 1
                    ugrid.parent[val - 1] = ugrid.parent[val]
                    ugrid.union(val, val - 1)
                    if ci - 1 > 0 and grid[ri][ci - 2] == 1:
                        ugrid.union(val - 1, val - 2)
                    if ri > 0 and grid [ri - 1][ci - 1] == 1:
                        ugrid.union(val - 1, val - 1 - row_len)
                    if ri < (len(grid) - 1) and grid[ri + 1][ci - 1] == 1:
                        ugrid.union(val - 1, val + row_len - 1)
            if ci < (row_len - 1):
                if grid[ri][ci + 1] == 0:
                    grid[ri][ci + 1] = 1
                    ugrid.parent[val + 1] = ugrid.parent[val]
                    ugrid.union(val, val + 1)
                    if ci + 1 < row_len - 1 and grid[ri][ci + 2] == 1:
                        ugrid.union(val + 1, val + 2)
                    if ri > 0 and grid [ri - 1][ci + 1] == 1:
                        ugrid.union(val + 1, val + 1 - row_len)
                    if ri < (len(grid) - 1) and grid[ri + 1][ci + 1] == 1:
                        ugrid.union(val + 1, val + row_len + 1)
        squares_added += 1
    return squares_added
            
    # find all neighbors to those squares that are 0
    # convert those squares to 1
    # merge those squares with all neighbors that are 1
    # increment # squares added
    # test if ugrid.get_count == 1 now
    # return 


# grid = [[0,1,1],[1,0,1],[1,0,1]]
# print(shortest_bridge(grid))

# grid = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
# print(shortest_bridge(grid))

grid = [[1, 0, 0], [1, 0, 0], [0, 0, 1]]
print(shortest_bridge(grid))