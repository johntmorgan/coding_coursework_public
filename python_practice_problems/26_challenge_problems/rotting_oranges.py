#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 17:17:40 2023

@author: johnmorgan
"""

def min_minutes_to_rot(grid):
    minutes = 0
    good = 0
    rotten = []
    for ri, row in enumerate(grid):
        for ci, col in enumerate(row):
            if grid[ri][ci] == 2:
                rotten.append([ri, ci])
            elif grid[ri][ci] == 1:
                good += 1
    newly_rotten = []
    for elem in rotten:
        newly_rotten.append(elem)
    while newly_rotten and good > 0:
        last_rotten = newly_rotten
        newly_rotten = []
        while last_rotten:
            curr = last_rotten.pop(0)
            row, col = curr[0], curr[1]
            if row > 0 and grid[row - 1][col] == 1:
                grid[row - 1][col] = 2
                newly_rotten.append([row - 1, col])
                good -= 1
            if row < len(grid) - 1 and grid[row + 1][col] == 1:
                grid[row + 1][col] = 2
                newly_rotten.append([row + 1, col])
                good -= 1
            if col > 0 and grid[row][col - 1] == 1:
                grid[row][col - 1] = 2
                newly_rotten.append([row, col - 1])  
                good -= 1
            if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
                grid[row][col + 1] = 2
                newly_rotten.append([row, col + 1])  
                good -= 1
        minutes += 1
    if good > 0:
        return -1
    return minutes
    
    
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(min_minutes_to_rot(grid))


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