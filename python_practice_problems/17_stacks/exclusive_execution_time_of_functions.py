#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:51:27 2023

@author: johnmorgan
"""

def exclusive_time(n, logs):
    times = [0] * n
    stack = []
    for entry in logs:
        arr_log = entry.split(":")
        if arr_log[1] == "start":
            stack.append([arr_log[0], arr_log[2]])
        else:
            start = stack.pop()
            diff = int(arr_log[2]) - int(start[1]) + 1
            times[int(arr_log[0])] += diff
            if stack:
                times[int(stack[-1][0])] -= diff
    return times

n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(exclusive_time(n, logs))

n = 5
logs =  ["0:start:0", "1:start:5", "1:end:9", "4:start:10", "2:start:13",
          "2:end:15", "3:start:16", "3:end:18", "4:end:21", "0:end:22"]
print(exclusive_time(n, logs))

n = 5 
logs = ["0:start:0", "1:start:5", "1:end:9", "2:start:1", "2:end:4",
        "1:start:10", "3:start:13", "3:end:15", "4:start:16", "4:end:18",
        "1:end:21", "0:end:22"]
print(exclusive_time(n, logs))
