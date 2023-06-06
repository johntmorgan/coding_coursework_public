#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:38:41 2023

@author: johnmorgan
"""

from union_find_3 import UnionFind

# Review
# O(n * n * alpha(n))
# Space O(n * n) - parent list 4n^2 to store

def regions_by_slashes(grid):
    n = len(grid)
    find_union = UnionFind(4 * n * n)
    for r_index, row in enumerate(grid):
        for c_index, val in enumerate(row):
            root = 4 * (r_index * n + c_index)
            if val in ['/', ' ']:
                find_union.union(root + 0, root + 1)
                find_union.union(root + 2, root + 3)
            if val in ['\\', ' ']:
                find_union.union(root + 0, root + 2)
                find_union.union(root + 1, root + 3)
            # connect top
            if r_index > 0:
                find_union.union(root + 0, root - 4 * n + 3)
            # connect bottom
            if r_index + 1 < n:
                find_union.union(root + 3, root + 4 * n)
            # connect left side
            if c_index > 0:
                find_union.union(root + 1, root - 4 + 2)
            # connect right side
            if c_index + 1 < n:
                find_union.union(root + 2, root + 4 + 1)
    return sum(find_union.find(x) == x for x in range(4 * n * n))

grid = ["/\\","\\/"]
print(regions_by_slashes(grid))