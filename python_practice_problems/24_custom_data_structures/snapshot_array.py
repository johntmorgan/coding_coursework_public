#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 18:37:04 2023

@author: johnmorgan
"""

class SnapshotArray:
    def __init__(self, length):
        self.arr = [0] * length
        self.snap_dict = {}
        self.snap_counter = 0
        
    def set_value(self, idx, val):
        self.arr[idx] = val
        
    def snapshot(self):
        snap_arr = [0] * len(self.arr)
        for i, elem in enumerate(self.arr):
            snap_arr[i] = elem
        self.snap_dict[self.snap_counter] = snap_arr 
        self.snap_counter += 1
        return self.snap_counter - 1
    
    def get_value(self, idx, snap_id):
        return self.snap_dict[snap_id][idx]
    
    