#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:34:27 2023

@author: johnmorgan
"""

from island_union_find import UnionFind

def num_islands(grid):
    uf = UnionFind(grid)
    row_length = len(grid[0])
    for i in range(len(grid)):
        for j in range(row_length):
            if grid[i][j] == "1":
                if i > 0 and grid[i - 1][j] == "1":
                    uf.union(i * row_length + j, (i - 1) * row_length + j)
                if i < len(grid) - 1 and grid[i + 1][j] == "1":
                    uf.union(i * row_length + j, (i + 1) * row_length + j)
                if j > 0 and grid[i][j - 1] == "1":
                    uf.union(i * row_length + j, i * row_length + j - 1)
                if j < row_length - 1 and grid[i][j + 1] == "1":
                    uf.union(i * row_length + j, i * row_length + j + 1)
    return uf.get_count()


grid = [["1","1","1"],["0","1","0"],["1","0","0"],["1","0","1"]]
print(num_islands(grid))

grid = [["1", "1", "1", "1", "0"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "1", "1"]]
print(num_islands(grid))