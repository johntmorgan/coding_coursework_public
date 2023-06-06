#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:05:01 2023

@author: johnmorgan
"""

import heapq

# O(nlogn)

def tasks(tasks_list):
    machine_count = 0
    task_heap = []
    used_machines = []
    for task in tasks_list:
        heapq.heappush(task_heap, task)
    while len(task_heap) > 0:
        new_task = heapq.heappop(task_heap)
        if len(used_machines) == 0:
            heapq.heappush(used_machines, new_task[1])
        else:
            if used_machines[0] <= new_task[0]:
                heapq.heappop(used_machines)
            heapq.heappush(used_machines, new_task[1])
    return len(used_machines)

lst = [[1,1],[5,5],[8,8],[4,4],[6,6],[10,10],[7,7]]
print(tasks(lst))

lst = [[1,7],[1,7],[1,7],[1,7],[1,7],[1,7]]
print(tasks(lst))

lst = [[1,7],[8,13],[5,6],[10,14],[6,7]]
print(tasks(lst))