#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:00:08 2023

@author: johnmorgan
"""

# O(n * 3^l)
# n is number of cells
# l is the word length
# 3 choices in each cell after first one explored

# O(l) space complexity

def rec_ws(grid, word, state, i, j):
    if state == word:
        return True
    else:
        if i > 0 and grid[i - 1][j] == word[len(state)]:
            state += grid[i - 1][j]
            check = rec_ws(grid, word, state, i - 1, j)
            if check == True:
                return True
            state = state[:-1]
        if i < len(grid) - 1 and grid[i + 1][j] == word[len(state)]:
            state += grid[i + 1][j]
            check = rec_ws(grid, word, state, i + 1, j)
            if check == True:
                return True
            state = state[:-1]
        if j > 0 and grid[i][j - 1] == word[len(state)]:
            state += grid[i][j - 1]
            check = rec_ws(grid, word, state, i, j - 1)
            if check == True:
                return True
            state = state[:-1]
        if j < len(grid[0]) - 1 and grid[i][j + 1] == word[len(state)]:
            state += grid[i][j + 1]
            check = rec_ws(grid, word, state, i, j + 1)
            if check == True:
                return True
            state = state[:-1]
                
def word_search(grid, word):
    state = ""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == word[0]:
                state += grid[i][j]
                check = rec_ws(grid, word, state, i, j)
                if check == True:
                    return True
                state = state[:-1]
    return False


grid = [["N","W","L","I","M"],["V","I","L","Q","O"],["O","L","A","T","O"],["R","T","A","I","N"],["O","I","T","N","C"]]
word =  "LATIN"
print(word_search(grid, word))