#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:34:25 2023

@author: johnmorgan
"""

# Review, did not remember reverse grid fill approach

from crossing_union_find import UnionFind

def last_day_to_cross(row, col, cells):
    grid = [[0 for _ in range(col)] for _ in range(row)]
    # Size of grid PLUS top and bottom connectors
    uf = UnionFind(row * col + 1)
    
    # Go through cells in reverse order
    for i in range(len(cells) - 1, -1, -1):
        crow, ccol = cells[i][0] - 1, cells[i][1] - 1
        grid[crow][ccol] = 1
        uf_index = uf.find_index(crow, ccol, col)
        if crow > 0:
            if grid[crow - 1][ccol] == 1:
                neigh_index = uf.find_index(crow - 1, ccol, col)
                uf.union(uf_index, neigh_index)
        if crow < len(grid) - 1:
            if grid[crow + 1][ccol] == 1:
                neigh_index = uf.find_index(crow + 1, ccol, col)
                uf.union(uf_index, neigh_index)
        if ccol > 0:
            if grid[crow][ccol - 1] == 1:
                neigh_index = uf.find_index(crow, ccol - 1, col)
                uf.union(uf_index, neigh_index)
        if ccol < len(grid[0]) - 1:
            if grid[crow][ccol + 1] == 1:
                neigh_index = uf.find_index(crow, ccol + 1, col)
                uf.union(uf_index, neigh_index)    
        if crow == 0:
            uf.union(0, uf_index)
        if crow == len(grid) - 1:
            last_index = row * col + 1
            uf.union(uf_index, last_index)
        top_connector_parent = uf.find(0)
        bottom_connector_parent = uf.find(row * col + 1)
        if top_connector_parent == bottom_connector_parent:
            return i


# cells = [[3, 2], [1, 3], [2, 2], [3, 1], [1, 1], [1, 2], [2, 3], [3, 3], [2, 1]]
# row = 3
# col = 3
# print(last_day_to_cross(row, col, cells))

cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
row = 3
col = 3
print(last_day_to_cross(row, col, cells))
