#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:55:19 2023

@author: johnmorgan
"""

# Init O(n) to allocate space and fill with values
# Move O(1)
# O(n) space

class TicTacToe:
    # Constructor will be used to initialize TicTacToe data members 
    def __init__(self, n): 
        self.board = [[0 for _ in range(0, n)] for _ in range(0, n)]
        self.diagonal = 0 
        self.anti_diagonal = 0

    # move will be used to play a move by a specific player and identify who
    # wins at each move
    def move(self, row, col, player):
        if self.board[row][col] != 0:
            return "Invalid move"
        else:
            len_row = len(self.board[row])
            if player == 1:
                self.board[row][col] = 1
                if row == col:
                    self.diagonal += 1
                if col == len_row - row:
                    self.anti_diagonal += 1
            elif player == 2:
                self.board[row][col] = -1
                if row == col:
                    self.diagonal -= 1
                if col == len_row - row:
                    self.anti_diagonal -= 1
            if sum(self.board[row]) == len_row:
                return 1
            elif sum(self.board[row]) == -len_row:
                return 2
            if self.diagonal == len_row or self.anti_diagonal == len_row:
                return 1
            elif self.diagonal == -len_row or \
                self.anti_diagonal == -len_row:
                return 2
            for column in range(len_row):
                col_sum = 0
                for colrow in self.board:
                    col_sum += colrow[column]
                if col_sum == len_row:
                    return 1
                elif col_sum == -len_row:
                    return 2
        return 0
    
tt = TicTacToe(3)
tt.move(0, 0, 1)
tt.move(0, 2, 2)
tt.move(2, 2, 1)
tt.move(1, 1, 2)
tt.move(2, 0, 1)
tt.move(1, 0, 2)
print(tt.move(2, 1, 1))