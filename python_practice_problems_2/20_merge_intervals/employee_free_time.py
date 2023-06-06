#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:28:54 2023

@author: johnmorgan
"""

from interval import Interval
    
# Review, another bit of a trick
# O(n)

def employee_free_time(schedule):
    sched = []
    for employee in schedule:
        for interval in employee:
            sched.append(interval)
    sched.sort(key=lambda x: x.start)
    result = []
    latest = sched[0].end
    for index in range(len(sched)):
        if sched[index].start > latest:
            result.append(Interval(latest, sched[index].start))
        if sched[index].end > latest:
            latest = sched[index].end
    return result

# lst = [[[1,2],[5,6]],[[1,3]],[[4,10]]]

# schedule = []
# for employee in lst:
#     emp_int = []
#     for interval in employee:
#         emp_int.append(Interval(interval[0], interval[1]))
#     schedule.append(emp_int)
# results = employee_free_time(schedule)
# for result in results:
#     print(result.start, result.end)
    
lst2  =[[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]

schedule = []
for employee in lst2:
    emp_int = []
    for interval in employee:
        emp_int.append(Interval(interval[0], interval[1]))
    schedule.append(emp_int)
results = employee_free_time(schedule)
for result in results:
    print(result.start, result.end)