#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:49:08 2023

@author: johnmorgan
"""

from trie_5 import *

def rfs(result, grid, trie, visited, i, ci, node, seq):
    if node.is_string and seq not in result:
        result.append(seq)
    else:
        if i > 0 and [i - 1, ci] not in visited:
            test = grid[i - 1][ci]
            if test in node.children:
                prior = node
                node = node.children[test]
                seq += test
                visited.append([i - 1, ci])
                rfs(result, grid, trie, visited, i - 1, ci, node, seq)
                node = prior
                seq = seq[:-1]
                visited.pop()
        if i < len(grid) - 1 and [i + 1, ci] not in visited:
            test = grid[i + 1][ci]
            if test in node.children:
                prior = node
                node = node.children[test]
                seq += test
                visited.append([i + 1, ci])
                rfs(result, grid, trie,  visited, i + 1, ci, node, seq)
                node = prior
                seq = seq[:-1]
                visited.pop()
        if ci > 0 and [i, ci - 1] not in visited:
            test = grid[i][ci - 1]
            if test in node.children:
                prior = node
                node = node.children[test]
                seq += test
                visited.append([i, ci - 1])
                rfs(result, grid, trie, visited, i, ci - 1, node, seq)
                node = prior
                seq = seq[:-1]
                visited.pop()
        if ci < len(grid[0]) - 1 and [i, ci + 1] not in visited:
            test = grid[i][ci + 1]
            if test in node.children:
                prior = node
                node = node.children[test]
                seq += test
                visited.append([i, ci + 1])
                rfs(result, grid, trie, visited, i, ci + 1, node, seq)
                node = prior
                seq = seq[:-1]
                visited.pop()
    
def find_strings(grid, words):
    result = []
    trie = Trie()
    visited = []
    for word in words:
        trie.insert(word)
    for i, row in enumerate(grid):
        for ci, col in enumerate(row):
            char = grid[i][ci]
            if char in trie.root.children:
                seq = char
                visited.append([i, ci])
                node = trie.root.children[char]
                rfs(result, grid, trie, visited, i, ci, node, seq)
                visited.pop()
    return result

grid = [["C","S","L","I","M"],
        ["O","I","L","M","O"],
        ["O","L","I","E","O"],
        ["R","T","A","S","N"],
        ["S","I","T","A","C"]]
words = ["SLIME","SAILOR","MATCH","COCOON"]
print(find_strings(grid, words))