#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:20:56 2023

@author: johnmorgan
"""
    
class UnionFind:
    def __init__(self, n):
        self.parent = []
        for i in range(n + 1):
            self.parent.append(i)
        self.rank = [0] * (n + 1)

    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union(self, v1, v2):
        p1, p2 = self.find_parent(v1), self.find_parent(v2)
        if p1 == p2:
            # Already in the same tree
            return False
        else:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
                self.rank[p1] = self.rank[p1] + self.rank[p2]
            else:
                self.parent[p1] = p2
                self.rank[p2] = self.rank[p2] + self.rank[p1]
        return True