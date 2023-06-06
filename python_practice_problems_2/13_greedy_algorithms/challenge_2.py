#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:37:31 2023

@author: johnmorgan
"""

# O(n^2)

def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """
    total_cost = 0
    n = len(pipes)
    while n > 1:
        min_index = None
        min_value = float('inf')
        min_2_index = None
        min_2_value = float('inf')
        for index in range(n):
            if pipes[index] < min_2_value:
                if pipes[index] > min_value:
                    min_2_index = index
                    min_2_value = pipes[index]
                else:
                    min_2_index = min_index
                    min_2_value = min_value
                    min_index = index
                    min_value = pipes[index]
        cost = min_value + min_2_value
        total_cost += cost
        pipes.pop(max(min_index, min_2_index))
        pipes.pop(min(min_index, min_2_index))    
        pipes.append(cost)
        n -= 1
    return total_cost

# Use heap library, O(nlog(n))

import heapq
def min_cost(pipes):
    heapq.heapify(pipes)
    cost = 0
    while len(pipes) > 1:
        first = heapq.heappop(pipes)
        second = heapq.heappop(pipes)
        cost += first + second
        heapq.heappush(pipes, first + second)
    return cost

pipes = [4, 3, 2, 6]
print(min_cost(pipes))       
            