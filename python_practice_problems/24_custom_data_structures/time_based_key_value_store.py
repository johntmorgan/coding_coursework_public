#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:00:13 2023

@author: johnmorgan
"""

from binary_search import * 

class TimeStamp:
    def __init__(self):
        self.key_ts_dict = {}
        self.ts_val_dict = {}

    def set_value(self, key, value, timestamp):
        if key in self.key_ts_dict:
            self.key_ts_dict[key].append(timestamp)
        else:
            self.key_ts_dict[key] = [timestamp]
        self.ts_val_dict[timestamp] = value
    
    def get_value(self, key, timestamp):
        if not key in self.key_ts_dict:
            return ""
        else:
            ts_arr = self.key_ts_dict[key]
            stamp = binary_search(ts_arr, timestamp)
            if stamp is None:
                if ts_arr[len(ts_arr) - 1] < timestamp:
                    return self.ts_val_dict[ts_arr[len(ts_arr) - 1]]
                else:
                    return ""
            if ts_arr[stamp] <= timestamp:
                return self.ts_val_dict[self.key_ts_dict[key][stamp]]
            elif ts_arr[stamp] > 0:
                return self.ts_val_dict[self.key_ts_dict[key][stamp - 1]]
            else:
                return ""
       
            
# ts = TimeStamp()
# ts.set_value("foo","bar", 1)
# print(ts.get_value("foo", 1))

# ts = TimeStamp()
# ts.set_value("foo","bar", 1)
# print(ts.get_value("foo", 2))

ts = TimeStamp()
ts.set_value("foo","tan", 7)
ts.set_value("foo","ban", 9)
print(ts.get_value("foo", 8))
print(ts.get_value("foo", 9))

# from collections import defaultdict
# from binary_search import * 

# class TimeStamp:
#     def __init__(self):
#         self.values_dict = {}
#         self.timestamps_dict = defaultdict(int)
#         self.values_arr = []

#     #  Set TimeStamp data variables
#     def set_value(self, key, value, timestamp):
#         self.timestamps_dict[timestamp] = key
#         self.values_dict[(timestamp, key)] = value
#         self.values_arr.append(timestamp)

#     # Get time_stamp data variables
#     def get_value(self, key, timestamp):
#         if timestamp in self.timestamps_dict:
#             key = self.timestamps_dict[timestamp]
#             return self.values_dict[(timestamp, key)]
#         elif len(self.values_arr) == 0:
#             return ""
#         else:
#             prior = binary_search(self.values_arr, timestamp)
#             if not prior:
#                 prior = 0
#             else:
#                 prior -= 1
#             if self.values_arr[prior] <= timestamp:
#                 timestamp = self.values_arr[prior]
#                 key = self.timestamps_dict[timestamp]
#                 return self.values_dict[(timestamp, key)]
#             else:
#                 return ""