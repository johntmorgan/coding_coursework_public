#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:49:53 2023

@author: johnmorgan
"""

class hash_map:
    def __init__(self):
        self.hash_map_dict = {}
        
    def insert(self, x):
        if x in self.hash_map_dict.keys():
            self.hash_map_dict[x] += 1
        else:
            self.hash_map_dict[x] = 1