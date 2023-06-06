#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:02:35 2023

@author: johnmorgan
"""

from trie3 import Trie

# O(n * 3^l) - n is number of cells, l is length of longest string
# Have 4 directions to explor initially, but one is already explored
# O(m) space - m = all chars in all strings added together
# Call stack may be O(n) space - exploring entire length of grid
# O(m + n) space

def recurse_search(trie, grid, node, row_index, col_index, word, visited, lresults):
    if node.is_string == True:
        lresults.append(word)
        trie.remove_characters(word)
    if row_index > 0:
        if grid[row_index - 1][col_index] in node.children.keys() and \
            [row_index - 1, col_index] not in visited:
            visited.append([row_index - 1, col_index])
            letter = grid[row_index - 1][col_index]
            recurse_search(trie, grid, node.children[letter], row_index - 1, col_index,
                           word + letter, visited, lresults)
    if row_index < len(grid) - 1:
        if grid[row_index + 1][col_index] in node.children.keys() and \
            [row_index + 1, col_index] not in visited:
            visited.append([row_index + 1, col_index])
            letter = grid[row_index + 1][col_index]
            recurse_search(trie, grid, node.children[letter], row_index + 1, col_index,
                           word + letter, visited, lresults)
    if col_index > 0:
        if grid[row_index][col_index - 1] in node.children.keys() and \
            [row_index, col_index - 1] not in visited:
            visited.append([row_index, col_index - 1])
            letter = grid[row_index][col_index - 1]
            recurse_search(trie, grid, node.children[letter], row_index, col_index - 1,
                           word + letter, visited, lresults)
    if col_index < len(grid[0]) - 1:
        if grid[row_index][col_index + 1] in node.children.keys() and \
            [row_index, col_index + 1] not in visited:
            visited.append([row_index, col_index + 1])
            letter = grid[row_index][col_index + 1]
            recurse_search(trie, grid, node.children[letter], row_index, col_index + 1,
                           word + letter, visited, lresults)
    return lresults

def find_strings(grid, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    result = []
    for row_index, row in enumerate(grid):
        for col_index, letter in enumerate(row):
            if letter in trie.root.children.keys():
                visited = [[row_index, col_index]]
                letter_results = []
                found = recurse_search(trie, grid, trie.root.children[letter],
                                       row_index, col_index, letter, visited,
                                       letter_results)
                for elem in found:
                    result.append(elem)
    return result

# Faster course solution

def find_strings(grid, words):
    trie_for_words = Trie()
    result = []
    # Inserting strings in the dictionary
    for word in words:
        trie_for_words.insert(word)
    # Calling dfs for all the cells in the grid
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            dfs(trie_for_words, trie_for_words.root, grid, j, i, result)       
    return result

def dfs(words_trie, node, grid, row, col, result, word=''):
    # Checking if we found the string
    if node.is_string:
        result.append(word)
        node.is_string = False
        # remove the characters in the word that are not shared
        words_trie.remove_characters(word)
    
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        char = grid[row][col]
        # Getting child node of current node from Trie
        child = node.children.get(char)
        # if child node exists in Trie
        if child is not None:
            word += char
            # Marking it as visited before exploration
            grid[row][col] = None
            # Recursively calling DFS to search in all four directions
            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(words_trie, child, grid, row + row_offset, col + col_offset, result, word)

            # Restoring state after exploration
            grid[row][col] = char

# words = ["SLIME","SAILOR","MATCH","COCOON"]
# grid = [["C","S","L","I","M"],["O","I","L","M","O"],["O","L","I","E","O"],["R","T","A","S","N"],["S","I","T","A","C"]]
# print(find_strings(grid, words))

# words = ["BUY","STUFF","ONLINE","NOW"]
# grid = [["C","S","L","I","M"],["O","I","B","M","O"],["O","L","U","E","O"],["N","L","Y","S","N"],["S","I","N","E","C"]]
# print(find_strings(grid, words))

# words = ["REINDEER","IN","RAIN"]
# grid = [["C","O","L","I","M"],["I","N","L","M","O"],["A","L","I","E","O"],["R","T","A","S","N"],["S","I","T","A","C"]]
# print(find_strings(grid, words))

words = ["STREET", "STREETCAR", "STRING", "STING", "RING", "RACECAR"]
grid = [["S", "T", "R", "A", "C"], ["I", "R", "E", "E", "E"], ["N", "G", "I", "T", "C"], ["I", "T", "S", "R", "A"]] 
print(find_strings(grid, words))





