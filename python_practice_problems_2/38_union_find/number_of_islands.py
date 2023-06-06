#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:48:01 2023

@author: johnmorgan
"""

from union_find_2 import UnionFind

# Complexity O(m * n) where m is # rows, n is # columns
# Or you could just say O(n) where n is the number of grid squares - JM
# Space O(m * n) as required by union find data structure
# Not explained, but need to make parent and rank arrays for each grid square - JM

def num_islands(grid):
    ugrid = UnionFind(grid)
    row_len = len(grid[0])
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if grid[row_index][col_index] == "1":
                val = row_index * row_len + col_index
                if row_index > 0:
                    if grid[row_index - 1][col_index] == "1":
                        ugrid.union(val, val - row_len)
                if row_index < len(grid) - 1:
                    if grid[row_index + 1][col_index] == "1":
                        ugrid.union(val, val + row_len)
                if col_index > 0:
                    if grid[row_index][col_index - 1] == "1":
                        ugrid.union(val, val - 1)
                if col_index < row_len - 1:
                    if grid[row_index][col_index + 1] == "1":
                        ugrid.union(val, val + 1)
    return ugrid.get_count()

grid = [["1","1","1"],["0","1","0"],["1","0","0"],["1","0","1"]]
print(num_islands(grid))