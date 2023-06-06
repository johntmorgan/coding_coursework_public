#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:29:35 2023

@author: johnmorgan
"""

class neighbors:
    def __init__(self):
        self.grid = [[]]
        
    def left(grid, row, col):
        return grid[row][col-1]
    
    def right(grid, row, col):
        return grid[row][col+1]
    
    def up(grid, row, col):
        return grid[row-1][col]

    def down(grid, row, col):
        return grid[row+1][col]