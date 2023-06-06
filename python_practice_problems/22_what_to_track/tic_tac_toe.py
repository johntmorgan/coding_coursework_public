#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:22:54 2023

@author: johnmorgan
"""

class TicTacToe:
    def __init__(self, n):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.diagonal = 0
        self.antidiagonal = 0
    
    def move(self, row, col, player):
        if row < 0 or row > len(self.board) - 1 or col < 0 or \
            col > len(self.board[0]) - 1 or self.board[row][col] != 0:
            return "Invalid move!"
        else:
            if player == 1:
                self.board[row][col] = 1
            else:
                self.board[row][col] -= 1
            if row == col:
                if player == 1:
                    self.diagonal += 1
                else:
                    self.diagonal -= 1
            if row == len(self.board) - 1 - col or col == len(self.board[0]) - 1 - row:
                if player == 1:
                    self.antidiagonal += 1
                else:
                    self.antidiagonal -= 1
            for row in self.board:
                if sum(row) == len(self.board):
                    return 1
                if sum(row) == -len(self.board):
                    return 2
            for col_index in range(len(self.board[0])):
                col_sum = 0
                for row_index in range(len(self.board)):
                    col_sum += self.board[row_index][col_index]
                if col_sum == len(self.board[0]):
                    return 1
                if col_sum == -len(self.board[0]):
                    return 2
            return 0
                
                