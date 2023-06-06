#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:47:16 2023

@author: johnmorgan
"""

# O(N + E) time and space, N number of words E edges in graph

from graph import *
from collections import defaultdict, Counter, deque

def alien_order(words):
    dgraph = graph()
    dependencies = []
    for index, word in enumerate(words):
        if index < len(words) - 1:
            next_word = words[index + 1]
            diff_found = False
            letter_index = 0
            if len(next_word) < len(word) and word[:len(next_word)] == next_word:
                return ""
            while not diff_found and letter_index < len(word) - 1 and \
                letter_index < len(next_word) - 1:
                if word[letter_index] == next_word[letter_index]:
                    letter_index += 1
                else:
                    diff_found = True
                    dependencies.append([next_word[letter_index],
                                         word[letter_index]])
    dgraph.initializing_graph(dependencies)
    dgraph.building_graph(dependencies)
    indegrees = {}
    for parent in dgraph.graph:
        if parent not in indegrees:
            indegrees[parent] = 0
        for child in dgraph.graph[parent]:
            if child not in indegrees:
                indegrees[child] = 1
            else:
                indegrees[child] += 1
    sources = deque()
    for node in indegrees:
        if indegrees[node] == 0:
            sources.append(node)
            indegrees[node] = -1
    result = []
    while sources:
        node = sources.popleft()
        result.append(node)
        for child in dgraph.graph[node]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                sources.append(child)
                indegrees[child] = -1
    if len(result) != len(indegrees):
        return ""
    for word in words:
        for letter in word:
            if letter not in result:
                result.append(letter)
    return "".join(result)
                
    
words = ["xro","xma","per","prt","oxh","olv"]
print(alien_order(words))