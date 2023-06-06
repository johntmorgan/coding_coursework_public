#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:29:49 2022

@author: johnmorgan
"""

def depth_first_search(Adj, s, parent = None, order = None):
    if parent is None:
        parent = [None for v in Adj]
        parent[s] = s
        order = []
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            depth_first_search(Adj, v, parent, order)
    order.append(s)
    return parent, order

def full_dfs(Adj):
    parent = [None for v in Adj]
    order= []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            depth_first_search(Adj, v, parent, order)
    return parent, order

