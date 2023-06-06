#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:16:56 2023

@author: johnmorgan
"""

from backtracking import *

# Recurrence T(n) = nT(n - 1) + O(n^2)
# No worse than O(n^n) time
# Space O(n)

def valid(col, state):
    if col in state:
        return False
    for index in range(len(state)):
        if col == state[index] - (len(state) - index):
            return False
        elif col == state[index] + (len(state) - index):
            return False
    return True
    
def dfs(result, state, n):
    if len(state) == n:
        result.append(state)
        return
    else:
        print(state)
        for col in range(n):
            if valid(col, state):
                state.append(col)
                dfs(result, state, n)
                state.pop()

def solve_n_queens(n):
    result = []
    state = []
    dfs(result, state, n)
    return len(result)


print(solve_n_queens(3))
print(solve_n_queens(4))

# Iterative

# def is_valid_move(proposed_row, proposed_col, solution):
#   for i in range(0, proposed_row):
#     old_row = i
#     old_col = solution[i]
#     diagonal_offset = proposed_row - old_row
#     if (old_col == proposed_col or
#       old_col == proposed_col - diagonal_offset or
#         old_col == proposed_col + diagonal_offset):
#       return False

#   return True


# def solve_n_queens(n):
#   results = []
#   solution = [-1] * n
#   sol_stack = []

#   row = 0
#   col = 0

#   while row < n:
#     # For the current state of the solution, check if a queen can be placed in any
#     # column of this row
#     while col < n:
#       if is_valid_move(row, col, solution):
#         # If this is a safe position for a queen (a valid move), save 
#         # it to the current solution on the stack...
#         sol_stack.append(col)
#         solution[row] = col
#         row = row + 1
#         col = 0
#         # ... and move on to checking the next row (breaking out of the inner loop)
#         break
#       col = col + 1

#     # If we have checked all the columns
#     if col == n:
#       # If we are working on a solution
#       if sol_stack:
#         # Backtracking, as current row does not offer a safe spot given the previous move
#         # So, get set up to check the previous row with the next column
#         col = sol_stack[-1] + 1
#         sol_stack.pop()
#         row = row - 1
#       else:
#         # If we have backtracked all the way and found this to be a dead-end,
#         # break out of the inner loop
#         break  # no more solutions exist
      
#     # If we have found a safe spot for a queen in each of the rows
#     if row == n:
#       # add the solution into results
#       results.append(solution)

#       # backtrack to find the next solution
#       row = row - 1
#       col = sol_stack[-1] + 1
#       sol_stack.pop()

#   return len(results)