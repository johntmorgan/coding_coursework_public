#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 18:50:02 2022

@author: johnmorgan
"""

def try_to_relax(Adj, w, d, parent, u, v):
    if d[v] > d[u] + w(w, v):
        d[v] = d[u] + w(u, v)
        parent[v] = u

# Adj = adjacency lists
# w = weights
# s = start
def bellman_ford(Adj, w, s):
    # initialization
    infinity = float('inf')
    d = [infinity for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    V = len(Adj)
    for k in range(V - 1):
        for u in range(V):
            for v in Adj[u]:
                try_to_relax(Adj, w, d, parent, u, v)
    for u in range(V):
        for v in Adj[u]:
            if d[v] > d[u] + w(u, v):
                raise Exception("There is a negative loop!")
    return d, parent