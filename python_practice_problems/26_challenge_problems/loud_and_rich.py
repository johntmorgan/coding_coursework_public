#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:03:24 2023

@author: johnmorgan
"""

def loud_and_rich(richer, quiet):
    adj = {}
    for pair in richer:
        if pair[1] in adj:
            adj[pair[1]] += [pair[0]]
        else:
            adj[pair[1]] = [pair[0]]
    quietest= []
    for i in range(len(quiet)):
        min_quiet, min_index = quiet[i], i
        if i in adj:
            to_explore = []
            for elem in adj[i]:
                to_explore.append(elem)
            while to_explore:
                curr = to_explore.pop(0)
                if quiet[curr] < min_quiet:
                    min_quiet = quiet[curr]
                    min_index = curr
                if curr in adj:
                    for elem in adj[curr]:
                        to_explore.append(elem)
        quietest.append(min_index)
    return quietest


# richer = [[0, 2],[2, 1],[3, 1],[4, 1]]
# quiet = [2, 4, 0, 1, 3]
# print(loud_and_rich(richer, quiet))


richer = [[0, 5], [1, 6], [2, 1], [3, 1], [4, 6], [5, 1], [6, 8], [7, 4], [9, 4]]
quiet = [8, 5, 4, 1, 0, 9, 2, 3, 6, 7]
print(loud_and_rich(richer, quiet))

# def loud_and_rich(richer, quiet):
#     adj = {}
#     for pair in richer:
#         if pair[1] in adj:
#             adj[pair[1]] += [pair[0]]
#         else:
#             adj[pair[1]] = [pair[0]]
#     access = {}
#     for i in range(len(quiet)):
#         access[i] = [i]
#         if i in adj:
#             to_explore = adj[i]
#             while to_explore:
#                 curr = to_explore.pop(0)
#                 access[i] += [curr]
#                 if curr in adj:
#                     to_explore += adj[curr]
#     quietest = []
#     for i in range(len(quiet)):
#         min_quiet, min_index = float('inf'), None
#         for person_index in access[i]:
#             if quiet[person_index] < min_quiet:
#                 min_quiet = quiet[person_index]
#                 min_index = person_index
#         quietest.append(min_index)
#     return quietest