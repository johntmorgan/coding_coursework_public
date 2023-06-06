#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:12:17 2023

@author: johnmorgan
"""

from union_find import UnionFind

def redundant_connection(edges)
    graph = UnionFind(len(edges))
    for edge in edges:
        if not(graph(union(edge[0], edge[1]))):
            return edge
        