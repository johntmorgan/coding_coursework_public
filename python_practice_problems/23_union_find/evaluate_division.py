#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:49:49 2023

@author: johnmorgan
"""

# Review

from malware_union_find import UnionFind

def eq_dfs(eq_dict, start, end, product, visited):
    visited.append(start)
    neighbors = eq_dict[start]
    if end in neighbors:
        answer = product * neighbors[end]
    else:
        for neighbor, value in neighbors.items():
            if neighbor not in visited:
                answer = eq_dfs(eq_dict, neighbor, end, product * value, visited)
            if answer:
                break
    return answer

def evaluate_equations(equations, values, queries):
    letters = {}
    eq_dict = {}
    count = 0
    for index, (num, den) in enumerate(equations):
        if num not in letters:
            letters[num] = count
            count += 1
        if den not in letters:
            letters[den] = count
            count += 1
        if num not in eq_dict:
            eq_dict[num] = {}
        eq_dict[num][den] = values[index]
        if den not in eq_dict:
            eq_dict[den] = {}
        eq_dict[den][num] = 1 / values[index]
    uf = UnionFind(count)
    for equation in equations:
        uf.union(letters[equation[0]], letters[equation[1]])
    result = []
    for num, den in queries:
        if num not in letters or den not in letters:
            result.append(-1.0)
        elif uf.find(letters[num]) != uf.find(letters[den]):
            result.append(-1.0)
        else:
            result.append(eq_dfs(eq_dict, num, den, 1, []))
    return(result)

equations = [["a","b"],["b","c"]]
values = [2,3]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(evaluate_equations(equations, values, queries))


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