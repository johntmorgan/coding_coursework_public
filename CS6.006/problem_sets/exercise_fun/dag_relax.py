#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:33:03 2022

@author: johnmorgan
"""

def general_relax(Adj, w, s):
    d = [float('inf') for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    # while some_edge_relaxable(Adj, w, d):
    #     (u, v) = get_relaxable_edge(Adj, w, d)
    #     try_to_relax(Adj, w, d, parent, u, v)
    return d, parent

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

def DAG_Relaxation(Adj, w, s):
    _, order = depth_first_search(Adj, s) # Run DFS on graph
    order.reverse() 
    d = [float('inf') for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    for u in order:
        for v in Adj[u]:
            try_to_relax(Adj, w, d, parent, u, v)
    return d, parent

def try_to_relax(Adj, w, d, parent, u, v):
    if d[v] > d[u] + w(w, v):
        d[v] = d[u] + w(u, v)
        parent[v] = u