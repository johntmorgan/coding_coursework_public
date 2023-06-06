#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:19:03 2023

@author: johnmorgan
"""

class graph:
    def __init__(self):
        self.graph_list = {}

    def initializing_graph(self, dependencies):
        for x in dependencies:
            parent, child = x[1], x[0]
            self.graph_list[parent], self.graph_list[child] = [], []
    
    def building_graph(self, dependencies):
        for dependency in dependencies:
            parent, child = dependency[1], dependency[0]
            self.graph_list[parent].append(child)