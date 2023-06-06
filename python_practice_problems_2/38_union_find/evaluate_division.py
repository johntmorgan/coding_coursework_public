#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:38:14 2023

@author: johnmorgan
"""

# Leetcode 399 - medium (hard?)
# Practice again

def eq_dfs(graph, start, end, product, visited):
    visited.append(start)
    neighbors = graph[start]    
    answer = -1.0
    if end in neighbors:
        answer = product * neighbors[end]
    else:
        for neighbor, value in neighbors.items():
            if neighbor not in visited:
                answer = eq_dfs(graph, neighbor, end, product * value, visited)
            if answer != -1.0:
                break
    return answer

def evaluate_equations(equations, values, queries):
    graph = {}
    for index, (num, den) in enumerate(equations):
        if num not in graph:
            graph[num] = {}
        graph[num][den] = values[index]
        if den not in graph:
            graph[den] = {}
        graph[den][num] = 1 / values[index]
    result = []
    for num, den in queries:
        if num not in graph or den not in graph:
            result.append(-1.0)
        elif num == den:
            result.append(1.0)
        else:
            result.append(eq_dfs(graph, num, den, 1, []))
    return result

equations = [["a","b"],["b","c"]]
values = [2,3]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(evaluate_equations(equations, values, queries))