#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:27:08 2023

@author: johnmorgan
"""

# O(n * 3^l) n is number of cells, l is length of word
# O(l) space complexity

def recurse_word(grid, word, row, col, curr, visited):
    if curr == word:
        return True
    else:
        search_up, search_down, search_left, search_right = False, False, False, False
        if row > 0 and grid[row - 1][col] == word[len(curr)] and \
            [row - 1, col] not in visited:
            visited.append([row - 1, col])
            search_up = recurse_word(grid, word, row - 1, col,
                                     curr + word[len(curr)], visited)
            visited.pop()
        if row < len(grid) - 1 and grid[row + 1][col] == word[len(curr)] and \
            [row + 1, col] not in visited:
            visited.append([row + 1, col])
            search_down = recurse_word(grid, word, row + 1, col,
                                       curr + word[len(curr)], visited)
            visited.pop()
        if col > 0 and grid[row][col - 1] == word[len(curr)] and \
            [row, col - 1] not in visited:
            visited.append([row, col - 1])
            search_left = recurse_word(grid, word, row, col - 1,
                                       curr + word[len(curr)], visited)
            visited.pop()
        if col < len(grid[0]) - 1 and grid[row][col + 1] == word[len(curr)] and \
            [row, col + 1] not in visited:
            visited.append([row, col + 1])
            search_right = recurse_word(grid, word, row, col + 1,
                                        curr + word[len(curr)], visited)
            visited.pop()
        return search_up or search_down or search_left or search_right

def word_search(grid, word):
    found = False
    for row_index in range(len(grid)):
        for col_index in range(len(grid[0])):
            if not found and grid[row_index][col_index] == word[0]:
                found = recurse_word(grid, word, row_index, col_index, word[0], [])
    return found

# More efficient, review

def word_search(grid, word):
    n = len(grid)
    if n < 1:
        return False
    m = len(grid[0])
    if m < 1:
        return False
    for row in range(n):
        for col in range(m):
            if depth_first_search(row, col, word, grid):
                return True
    return False

def depth_first_search(row, col, word, grid):
    if len(word) == 0:
        return True
    if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) \
            or grid[row][col].lower() != word[0].lower():
        return False
    result = False
    grid[row][col] = '*'
    for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        result = depth_first_search(row + rowOffset, col + colOffset,
                                    word[1:], grid)
        if result:
            break
    grid[row][col] = word[0]
    return result

grid = [["N","W","L","I","M"],
        ["V","I","L","Q","O"],
        ["O","L","A","T","O"],
        ["R","T","A","I","N"],
        ["O","I","T","N","C"]]
word = "LATIN"
print(word_search(grid, word))

grid = [["N","W","L","I","M"],
        ["V","I","L","Q","O"],
        ["O","L","A","T","O"],
        ["R","T","A","X","N"],
        ["O","I","T","N","C"]]
word = "LATIN"
print(word_search(grid, word))