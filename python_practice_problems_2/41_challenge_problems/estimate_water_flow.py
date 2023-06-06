#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:02:57 2023

@author: johnmorgan
"""

def dfs_nw(row, col, heights, width, height, visited=[]):
    if row == 0:
        return True
    if col == 0:
        return True
    w_ocean, n_ocean, e_ocean, s_ocean = False, False, False, False
    if heights[row][col - 1] <= heights[row][col] and \
        [row, col - 1] not in visited:
        visited.append([row, col - 1])
        w_ocean = dfs_nw(row, col - 1, heights, width, height, visited)
    if heights[row - 1][col] <= heights[row][col] and \
        [row - 1, col] not in visited:
        visited.append([row - 1, col])
        n_ocean = dfs_nw(row - 1, col, heights, width, height, visited)
    if row < height - 1 and [row + 1, col] not in visited and \
        heights[row + 1][col] <= heights[row][col]:
        visited.append([row + 1, col])
        s_ocean = dfs_nw(row + 1, col, heights, width, height, visited)
    if col < width - 1 and [row, col + 1] not in visited and \
        heights[row][col + 1] < heights[row][col]:
        visited.append([row, col + 1])
        e_ocean = dfs_nw(row, col + 1, heights, width, height, visited)
    return n_ocean or s_ocean or w_ocean or e_ocean
        
def dfs_se(row, col, heights, width, height, visited=[]):
    if row == height - 1:
        return True
    if col == width - 1:
        return True
    w_ocean, n_ocean, e_ocean, s_ocean = False, False, False, False
    if heights[row][col - 1] <= heights[row][col] and \
        [row, col - 1] not in visited:
        visited.append([row, col - 1])
        w_ocean = dfs_se(row, col - 1, heights, width, height, visited)
    if heights[row - 1][col] <= heights[row][col] and \
        [row - 1, col] not in visited:
        visited.append([row - 1, col])
        n_ocean = dfs_se(row - 1, col, heights, width, height, visited)
    if row < height - 1 and [row + 1, col] not in visited and \
        heights[row + 1][col] <= heights[row][col]:
        visited.append([row + 1, col])
        s_ocean = dfs_se(row + 1, col, heights, width, height, visited)
    if col < width - 1 and [row, col + 1] not in visited and \
        heights[row][col + 1] < heights[row][col]:
        visited.append([row, col + 1])
        e_ocean = dfs_se(row, col + 1, heights, width, height, visited)
    return n_ocean or s_ocean or w_ocean or e_ocean

def estimate_water_flow(heights):
    both_oceans = []
    width, height = len(heights[0]), len(heights)
    for i, row in enumerate(heights):
        for j, col in enumerate(row):
            pacific = dfs_nw(i, j, heights, width, height, [])
            atlantic = dfs_se(i, j, heights, width, height, [])
            if pacific and atlantic:
                both_oceans.append([i, j])
    return both_oceans

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(estimate_water_flow(heights))