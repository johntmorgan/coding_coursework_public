#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:10:25 2023

@author: johnmorgan
"""

import copy

DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9' ]

def is_valid(digit, board, i, j):
    if digit in board[i]:
        return False
    for row in range(len(board)):
        if board[row][j] == digit:
            return False
    if 0 <= i <= 2:
        y_square = [0,2]
    elif 3 <= i <= 5:
        y_square = [3,5]
    else:
        y_square = [6,8]
    if 0 <= j <= 2:
        x_square = [0,2]
    elif 3 <= j <= 5:
        x_square = [3,5]
    else:
        x_square = [6,8]
    for x in range(x_square[0], x_square[1] + 1):
        for y in range(y_square[0], y_square[1] + 1):
            if board[y][x] == digit:
                return False
    return True

def recurse_sudoku(board, i, j, solution):
    finished = True
    for row in board:
        if "." in row:
            finished = False
    if finished:
        for row in board:
            solution.append(copy.deepcopy(row))
        return
    while board[i][j] != ".":
        if j < len(board) - 1:
            j += 1
        else:
            j = 0
            i += 1
    for digit in DIGITS:
        if is_valid(digit, board, i, j):
            board[i][j] = digit
            recurse_sudoku(board, i, j, solution)
            board[i][j] = "."
    return solution

def solve_sudoku(board):
    solution = []
    recurse_sudoku(board, 0, 0, solution)
    return solution

board = [[".",".",".",".",".",".",".","7","."],["2","7","5",".",".",".","3","1","4"],[".",".",".",".","2","7",".","5","."],["9","8",".",".",".",".",".","3","1"],[".","3","1","8",".","4",".",".","."],[".",".",".","1",".",".","8",".","5"],["7",".","6","2",".",".","1","8","."],[".","9",".","7",".",".",".",".","."],["4","1",".",".",".","5",".",".","7"]]
print(solve_sudoku(board))