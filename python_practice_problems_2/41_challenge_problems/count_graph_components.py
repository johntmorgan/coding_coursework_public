#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:33:47 2023

@author: johnmorgan
"""

# Lazy way, relies on edges being sorted

def components_count_in_graph(n, edges):
    visited = []
    components = 0   
    for edge in edges:
        if edge[0] in visited or edge[1] in visited:
            if edge[0] not in visited:
                visited.append(edge[0])
            if edge[1] not in visited:
                visited.append(edge[0])
        else:
            visited.append(edge[0])
            visited.append(edge[1])
            components += 1
    single_nodes = n - len(visited)
    components += single_nodes
    return components

# Let's practice union find though

class UnionFind:
    def __init__(self, n):
        self.parent = []
        self.rank = []
        self.count = n
        for node in range(n):
            self.parent.append(node)
            self.rank.append(0)
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

def components_count_in_graph(n, edges):
    uf = UnionFind(n)
    for edge in edges:
        uf.union(edge[0], edge[1])
    return uf.count


n = 5
edges = [[0,1],[1,2],[3,4]]
print(components_count_in_graph(n, edges))

n = 6
edges = [[0, 1], [3, 4], [4, 5]]
print(components_count_in_graph(n, edges))