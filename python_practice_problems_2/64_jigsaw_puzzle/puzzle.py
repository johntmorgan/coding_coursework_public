#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:17:54 2023

@author: johnmorgan
"""

from enum import Enum

class Edge(Enum):
    INDENTATION = 1 
    EXTRUSION = 2
    FLAT = 3
    
class Side: 
  def __init__(self, edge):
    self.__edge = edge
        
class Piece:
  def __init__(self):
    self.__sides = [None] * 4 # List of sides and will be of length 4

  def check_corner(self):
    pass

  def check_edge(self):
    pass

  def check_middle(self):
    pass

class __Puzzle(object):
  __instances = None

  # Puzzle is a singleton class that ensures it will have only one active instance at a time
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__Puzzle, cls).__new__(cls)
    return cls.__instances

class Puzzle(metaclass=__Puzzle):
  def __init__(self):
    self.__board = [[]] # List of List of Piece (2D array)
    self.__free = [] # List of Piece for currently free pieces (yet to be inserted in board)

  def insert_piece(self, piece, row, column):
    pass

class PuzzleSolver:
  # board here refers to the instance of the Puzzle board
  def match_pieces(self, board):
    # Returns the Puzzle board
    pass