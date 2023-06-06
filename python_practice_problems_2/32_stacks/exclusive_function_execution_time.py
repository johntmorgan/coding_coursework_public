#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:59:14 2023

@author: johnmorgan
"""

from logs import *
from stack import *
from collections import deque

# O(mlogn), m events and n function digits (hmm - JM)
# O(mlogn) space complexity

def exclusive_time(n, logs):
    times = [0] * n
    stack = create_stack()
    for log in logs:
        arr_log = log.split(":")
        if arr_log[1] == "start":
            push(stack, [int(arr_log[0]), int(arr_log[2]), 0])
        else:
            start = pop(stack)
            run_time = int(arr_log[2]) - start[1] + 1
            times[start[0]] = times[start[0]] + run_time + start[2]
            for calling in stack:
                calling[2] = calling[2] - (run_time + start[2])
    return times

# n = 2
# logs = ["0:start:0","1:start:3","1:end:6","0:end:10"]
# print(exclusive_time(n, logs))

n = 5
logs = ["0:start:0", "1:start:5", "1:end:9", "4:start:10", "2:start:13",
        "2:end:15", "3:start:16", "3:end:18", "4:end:21", "0:end:22"]
print(exclusive_time(n, logs))

n = 5 
logs = ["0:start:0", "1:start:5", "1:end:9", "2:start:1", "2:end:4",
        "1:start:10", "3:start:13", "3:end:15", "4:start:16", "4:end:18",
        "1:end:21", "0:end:22"]
print(exclusive_time(n, logs))