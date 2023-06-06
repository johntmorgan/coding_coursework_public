#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:10:13 2023

@author: johnmorgan
"""

from collections import defaultdict 
class Graph:

  # Constructor
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.vertices = vertices
    
  def addEdge(self, u, v):
    self.graph[u].append(v) 