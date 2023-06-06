#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:30:54 2023

@author: johnmorgan
"""

from heapq import *

def tasks(tasks_list):
    count = 0
    tasks, machines = [], []
    for task in tasks_list:
        heappush(tasks, task)
    while len(tasks) > 0:
        curr_task = heappop(tasks)
        if len(machines) == 0:
            heappush(machines, curr_task[1])
            count += 1
        elif machines[0] > curr_task[0]:
            heappush(machines, curr_task[1])
            count += 1
        else:
            heappop(machines)
            heappush(machines, curr_task[1])
    return count
    

tasks_list = [[1, 3], [2, 6], [5, 9], [4, 7], [8, 10], [8, 10], [12, 15]]
print(tasks(tasks_list))