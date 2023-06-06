#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:52:00 2023

@author: johnmorgan
"""

# O(n)

def trace_path(dict1):
    vals = dict1.values()
    keys = dict1.keys()
    location = None
    for key in keys:
        if key not in vals:
            location = key
    if location == None:
        return "The start could not be found"
    else:
        path = []
        while location in keys:
            path.append([location, dict1[location]])
            location = dict1[location]
    return path

dict1 = {
  "NewYork": "Chicago",
  "Boston": "Texas",
  "Missouri": "NewYork",
  "Texas": "Missouri"
}
print(trace_path(dict1))