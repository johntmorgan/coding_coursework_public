#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:22:40 2023

@author: johnmorgan
"""

def dfs_ocean(heights, ri, ci, width, height, visited, ocean):
    if ocean == "NW" and (ri == 0 or ci == 0):
        return True
    if ocean == "SE" and (ri == height - 1 or ci == width - 1):
        return True
    else:
        visited.append([ri, ci])
        east, west, south, north = False, False, False, False
        if ri > 0 and [ri - 1, ci] not in visited and \
            heights[ri - 1][ci] <= heights[ri][ci]:
            north = dfs_ocean(heights, ri - 1, ci, width, height, visited, ocean)
        if ri < height - 1 and [ri + 1, ci] not in visited and \
            heights[ri + 1][ci] <= heights[ri][ci]:
            south = dfs_ocean(heights, ri + 1, ci, width, height, visited, ocean)
        if ci > 0 and [ri, ci - 1] not in visited and \
            heights[ri][ci - 1] <= heights[ri][ci]:
            west = dfs_ocean(heights, ri, ci - 1, width, height, visited, ocean)
        if ci < width - 1 and [ri, ci + 1] not in visited and \
            heights[ri][ci + 1] <= heights[ri][ci]:
            east = dfs_ocean(heights, ri, ci + 1, width, height, visited, ocean)
    return north or south or west or east

def estimate_water_flow(heights):
    both_oceans = []
    height, width = len(heights), len(heights[0])
    for ri, row in enumerate(heights):
        for ci, col in enumerate(heights[0]):
            pacific = dfs_ocean(heights, ri, ci, width, height, [], "NW")
            atlantic = dfs_ocean(heights, ri, ci, width, height, [], "SE")
            if pacific and atlantic:
                both_oceans.append([ri, ci])
    return both_oceans
    
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(estimate_water_flow(heights))

heights = [[7, 3, 5, 2, 8], [2, 3, 4, 5, 6], [3, 9, 6, 8, 4]]
print(estimate_water_flow(heights))