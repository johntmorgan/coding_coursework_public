#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:19:34 2023

@author: johnmorgan
"""

# Template for backtracking using dfs

class backtracking:
    def __init__(self):
        self.state = []    
        
    def dfs(state):
        res = []
        if is_solution(state):
            res.append(state[:]) # e.g. add a copy of the state to final result list
            return

        for choice in choices:
            if valid(choice):
                state.add(choice) # make move
                dfs(state)
                state.remove(choice) # backtrack