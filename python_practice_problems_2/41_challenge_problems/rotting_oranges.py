#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:03:11 2023

@author: johnmorgan
"""

def min_minutes_to_rot(grid):
    rotten = []
    good = 0
    for row_index, row in enumerate(grid):
        for col_index, val in enumerate(row):
            if val == 2:
                rotten += [[row_index, col_index]]
            elif val == 1:
                good += 1
    minutes = 0
    while rotten and good > 0:
        newly_rotten = []
        for bad in rotten:
            if bad[0] > 0:
                if grid[bad[0] - 1][bad[1]] == 1:
                    grid[bad[0] - 1][bad[1]] = 2
                    newly_rotten.append([bad[0] - 1, bad[1]])
                    good -= 1
            if bad[0] < len(grid) - 1:
                if grid[bad[0] + 1][bad[1]] == 1:
                    grid[bad[0] + 1][bad[1]] = 2
                    newly_rotten.append([bad[0] + 1, bad[1]])
                    good -= 1
            if bad[1] > 0:
                if grid[bad[0]][bad[1] - 1] == 1:
                    grid[bad[0]][bad[1] - 1] = 2
                    newly_rotten.append([bad[0], bad[1] - 1])
                    good -= 1
            if bad[1] < len(grid[0]) - 1:
                if grid[bad[0]][bad[1] + 1] == 1:
                    grid[bad[0]][bad[1] + 1] = 2
                    newly_rotten.append([bad[0], bad[1] + 1])
                    good -= 1
        rotten = newly_rotten
        minutes += 1
    if good == 0:
        return minutes
    return -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(min_minutes_to_rot(grid))
