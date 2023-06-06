#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:23:26 2023

@author: johnmorgan
"""

from union_find_3 import UnionFind

# Naive approach
# O(k4nm^2) n * m = array size, k = number of days
# O(n^2) = space, because of grid

# Review/redo from scratch
# O(m * n * alpha * (m * n))
# Alpha is Ackerman function, slow growing max effectively 4
# O(m * n) space to store cell values

def last_day_to_cross(row, col, cells):
    connections = UnionFind(row * col + 2)
    neighbours = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    cells = [(r - 1, c - 1) for r, c in cells]
    grid = [[1] * col for _ in range(row)]
    for i in range(len(cells) - 1, -1, -1):
        r, c = cells[i][0], cells[i][1]
        grid[r][c] = 0
        for r_neigh, c_neigh in neighbours:
            first_ind = connections.find_index(r + r_neigh, c + c_neigh, col)
            if r + r_neigh >= 0 and r + r_neigh < row and \
                c + c_neigh >= 0 and c + c_neigh < col and \
                    grid[r + r_neigh][c + c_neigh] == 0:
                second_ind = connections.find_index(r, c, col)
                connections.union(first_ind, second_ind)
        if r == 0:
            connections.union(0, connections.find_index(r, c, col))
        if r == row - 1:
            rr = row * col + 1
            cc = connections.find_index(r, c, col)
            connections.union(rr, cc)
        f1 = connections.find(0)
        f2 = connections.find(row*col + 1)
        if f1 == f2:
            return i

row = 2
col = 2
cells = [[1,1],[1,2],[2,1],[2,2]]
print(last_day_to_cross(row, col, cells))

# row = 3
# col = 3
# # Answer: 3
# cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
# print(last_day_to_cross(row, col, cells))