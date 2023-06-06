#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:29:58 2023

@author: johnmorgan
"""

# O(n) constructor
# O(1) get_value
# O(1) set_value
# O(n) snapshot
# O(n * m) space - n = length, m = number of snapshots

class SnapshotArray:
    # Constructor
    def __init__(self, length):
        self.arr = [0] * length
        self.snap_id = 0
        self.snap_dict = {}

    # Function set_value sets the value at a given index idx to val. 
    def set_value(self, idx, val):
        self.arr[idx] = val
    
    # This function takes no parameters and returns the snapid.
    # snapid is the number of times that the snapshot() function was called minus 1. 
    def snapshot(self):
        new_arr = [0] * len(self.arr)
        for i, elem in enumerate(self.arr):
            new_arr[i] = elem
        self.snap_dict[self.snap_id] = new_arr
        self.snap_id += 1
        return self.snap_id - 1

    # Function get_value returns the value at the index idx with the given snapid.
    def get_value(self, idx, snap_id):
        return self.snap_dict[snap_id][idx]
    
# Course solution with hashmap instead of array for storage
# Get O(1) constructor instead of O(n)

class SnapshotArray:
    # Constructor
    def __init__(self, length):
        self.snapid = 0
        self.node_value = dict()
        self.node_value[0] = dict()
        self.ncount = length

    # Function set_value sets the value at a given index idx to val.
    def set_value(self, idx, val):
        if idx < self.ncount:
            self.node_value[self.snapid][idx] = val

    # This function takes no parameters and returns the snapid.
    # snapid is the number of times that the snapshot() function was called minus 1.
    def snapshot(self):
        self.node_value[self.snapid + 1] = (self.node_value[self.snapid]).copy()
        self.snapid += 1
        return self.snapid - 1

    # Function get_value returns the value at the index idx with the given snapid.
    def get_value(self, idx, snapid):
        if snapid < self.snapid and snapid >= 0 and idx < self.ncount:
            return self.node_value[snapid][idx] if idx in self.node_value[snapid] else 0
        else:
            return None

    def __str__(self):
        return str(self.node_value)

s = SnapshotArray(3)
s.set_value(0, 5)
s.snapshot()
s.set_value(0, 6)
print(s.get_value(0, 0))
s.set_value(0, 100)
s.snapshot()
print(s.get_value(1, 1))
