#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:22:59 2023

@author: johnmorgan
"""

# Time O(N * N * alpha(N))
# Space O(N * N) = parent list O(4 * N * N)

from slashes_union_find import UnionFind

def regions_by_slashes(grid):
    symbols = []
    for row in grid:
        symbol_row = []
        index = 0
        while index < len(row):
            if row[index] == "\\":
                symbol_row.append("back")
                index += 1
            elif row[index] == "/":
                symbol_row.append("forward")
                index += 1
            else:
                symbol_row.append("blank")
                index += 1
        symbols.append(symbol_row)
    row_length = len(symbols[0])
    uf = UnionFind(row_length * len(symbols))
    for row_index, row in enumerate(symbols):
        index = 0
        start = row_index * row_length * 4
        for symbol in symbols[row_index]:
            if symbol == "back":
                uf.union(start, start + 2)
                uf.union(start + 1, start + 3)
            elif symbol == "forward":
                uf.union(start, start + 1)
                uf.union(start + 2, start + 3)
            else:
                uf.union(start, start + 1)
                uf.union(start, start + 2)
                uf.union(start, start + 3)
            start += 4
    for row in range(len(symbols)):
        for col in range(row_length):
            index = row * row_length + col
            start = index * 4
            if row > 0:
                uf.union(start, start - row_length * 4 + 3)
            if row < len(grid) - 1:
                uf.union(start + 3, start + row_length * 4)
            if col > 0:
                uf.union(start + 1, start - 2)
            if col < row_length - 1:
                uf.union(start + 2, start + 5)
    return uf.components

grid = ["/\\","\\/"]
print(regions_by_slashes(grid))

grid = [" /", "  "]
print(regions_by_slashes(grid))

grid = ["\\\\/\\\\\\ \\", " \\\\//\\/ ", "/ / \\\\/\\", "\\\\///  \\", "/\\\\\\\\/ \\", "///////\\", "/\\\\// / ", "\\///\\\\//"]
print(regions_by_slashes(grid))