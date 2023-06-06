#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:57:07 2023

@author: johnmorgan
"""

def can_finish(n, prereqs):
    cgraph = {}
    for prereq in prereqs:
        if prereq[1] in cgraph.keys():
            cgraph[prereq[1]] = cgraph[prereq[1]] + [prereq[0]]
        else:
            cgraph[prereq[1]] = [prereq[0]]
    for course in range(n):
        if course not in cgraph.keys():
            cgraph[course] = []
    indegrees = {}
    for course in cgraph.keys():
        indegrees[course] = 0
    for course in cgraph.keys():
        for dependency in cgraph[course]:
            indegrees[dependency] = indegrees[dependency] + 1
    sources = []
    for key, val in indegrees.items():
        if val == 0:
            sources.append(key)
    order = []
    while len(sources) > 0:
        source = sources.pop(0)
        order.append(source)
        for dependency in cgraph[source]:
            if indegrees[dependency] == 1:
                indegrees[dependency] = 0
                if dependency not in order:
                    sources.append(dependency)
            else:
                indegrees[dependency] = indegrees[dependency] - 1
    if len(order) != n:
        return False
    return True