#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:23:42 2023

@author: johnmorgan
"""

# O(n) time
# O(n) space

from union_find import UnionFind

def redundant_connection(edges):
	graph = UnionFind(len(edges))
	for edge in edges:
		if not graph.union(edge[0], edge[1]):
			return edge
    

edges = [[1,2],[1,3],[2,3]]
print(redundant_connection(edges))

edges = [[1,2],[2,3],[1,3]]
print(redundant_connection(edges))