#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:33:08 2023

@author: johnmorgan
"""

from interval import Interval

def employee_free_time(schedule):
    output, sched = [], []
    for employee in schedule:
        for interval in employee:
            sched.append(interval)
    sched.sort(key=lambda x: x.start)
    latest = sched[0].end
    for index in range(len(sched)):
        if sched[index].start > latest:
            output.append(Interval(latest, sched[index].start))
        if sched[index].end > latest:
            latest = sched[index].end
    return output

A = [Interval(1,2),Interval(5,6)]
B = [Interval(1,3),Interval(4,10)]
schedule = [A, B]
free_intervals = employee_free_time(schedule)
for interval in free_intervals:
    print(interval)