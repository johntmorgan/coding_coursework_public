#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 18:10:22 2023

@author: johnmorgan
"""

from collections import defaultdict
from binary_search import * 

# Naive 3 lists
# Set O(1), but get O(n) and space O(n)

# Now get O(logn)

class TimeStamp:
    def __init__(self):
        self.values_dict = {}
        self.timestamps_dict = defaultdict(int)
        self.values_arr = []

    #  Set TimeStamp data variables
    def set_value(self, key, value, timestamp):
        self.timestamps_dict[timestamp] = key
        self.values_dict[(timestamp, key)] = value
        self.values_arr.append(timestamp)

    # Get time_stamp data variables
    def get_value(self, key, timestamp):
        if timestamp in self.timestamps_dict:
            key = self.timestamps_dict[timestamp]
            return self.values_dict[(timestamp, key)]
        elif len(self.values_arr) == 0:
            return ""
        else:
            prior = binary_search(self.values_arr, timestamp)
            if not prior:
                prior = 0
            else:
                prior -= 1
            if self.values_arr[prior] <= timestamp:
                timestamp = self.values_arr[prior]
                key = self.timestamps_dict[timestamp]
                return self.values_dict[(timestamp, key)]
            else:
                return ""
 
# Course solution   
 
class TimeStamp:
    def __init__(self):
        self.values_dict = {}
        self.timestamps_dict = {}

    #  Set TimeStamp data variables
    def set_value(self, key, value, timestamp):
        saved = False
        if key in self.values_dict:
            if timestamp < self.timestamps_dict[key][- 1]:
                value = self.timestamps_dict[key][- 1]
            elif value != self.values_dict[key][len(self.values_dict[key])-1]:
                self.values_dict[key].append(value)
                self.timestamps_dict[key].append(timestamp)
                saved = True
        else:
            self.values_dict[key] = [value]
            self.timestamps_dict[key] = [timestamp]
            saved = True

    # Find the index of right most occurrence of the given timestamp
    # using binary search
    def search_index(self, n, key, timestamp):
        left = 0
        j=right = n
        mid = 0
        while left < right:
            mid = (left+right) >> 1
            if self.timestamps_dict[key][mid] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return left-1

    # Get time_stamp data variables
    def get_value(self, key, timestamp):
        if key not in self.values_dict:
            return ""
        else:
            index = self.search_index(len(self.timestamps_dict[key]),
                                      key, timestamp)
            if index > -1:
                return self.values_dict[key][index]
            return ""
            

# t = TimeStamp()
# t.set_value("foo", "bar", 1)
# print(t.get_value("foo", 1))

# t = TimeStamp()
# t.set_value("foo", "bar", 1)
# print(t.get_value("foo", 2))

t = TimeStamp()
t.set_value("foo", "tan", 7)
t.set_value("foo", "ban", 9)
print(t.values_dict)
print(t.get_value("foo", 8))
print(t.get_value("foo", 9))