#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:31:34 2023

@author: johnmorgan
"""

# Enumerations
class GameStatus(enum.Enum):
  Active =1
  BlackWin =2
  WhiteWin = 3
  Forfeit = 4
  Stalemate = 5
  Resignation = 6

class AccountStatus(enum.Enum):
  ACTIVE = 1
  CLOSED = 2
  CANCELED = 3
  BLACKLISTED = 4
  NONE = 5

# Custom Person data type class
class Person:
  def __init__(self, name, street_address, city, state, zip_code, country):
    self.__name = name
    self.__street_address = street_address
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country
    
class Box:
  def __init__(self, piece, x, y):
    self.__piece = piece
    self.__x = x
    self.__y = y

class Chessboard:
  def __init__(self, boxes, creation_date):
    self.__boxes = boxes
    self.__creation_date = creation_date

  def get_pieces(self):
    None
  def reset_board(self):
    None
  def update_board(self):
    None
    
from abc import ABC, abstractmethod
class Piece(ABC):
  def __init__(self, killed, white):
    self.__killed = killed
    self.__white = white

  def is_white(self):
    pass
    
  def is_killed(self):
    pass

  @abstractmethod
  def can_move(self, board, start, end):
    pass

class King(Piece):
  def __init__(self, killed, white, castling_done):
    super().__init__(killed, white)
    self.__castling_done = False
  
  def can_move(self, board, start, end):
    pass

class Queen(Piece):
  def __init__(self, killed, white):
    super().__init__(killed, white)
  
  def can_move(self, board, start, end):
    pass

class Knight(Piece):
  def __init__(self, killed, white):
    super().__init__(killed, white)
  
  def can_move(self, board, start, end):
    pass

class Bishop(Piece):
  def __init__(self, killed, white):
    super().__init__(killed, white)
  
  def can_move(self, board, start, end):
    pass

class Rook(Piece):
  def __init__(self, killed, white):
    super().__init__(killed, white)
  
  def can_move(self, board, start, end):
    pass

class Pawn(Piece):
  def __init__(self, killed, white):
    super().__init__(killed, white)
  
  def can_move(self, board, start, end):
    pass

class Move:
  def __init__(self, start, end, piece_killed, piece_moved,
               player, castling_move):
    self.__start = start
    self.__end = end
    self.__piece_killed = piece_killed
    self.__piece_moved = piece_moved
    self.__player = player
    self.__castling_move = castling_move

  def is_castling_move(self):
    None
    
class Account:
  def __init__(self, id, password, status):
    self.__id = id
    self.__password = password
    self.__status = status

  def reset_password(self):
    None

class Player(Account):
  def __init__(self, id, password, status, person, total_games_played,
               white_side):
    super().__init__(id, password, status)
    self.__person = person
    self.__total_games_played = total_games_played
    self.__white_side = False
  
  def is_white_side(self):
    pass

  def is_checked(self):
    pass

class Admin(Account):
  def __init__(self, id, password, status):
    super().__init__(id, password, status)
  
  def block_user(self):
    pass

class ChessMoveController:
  def validate_move():
    None

class ChessGameView:
  def play_move(self):
    None
    
class ChessGame: # BlackjackGame??? - JM
  def __init__(self, players, board, current_turn, status, moves_played):
    self.__player = player
    self.__board = board
    self.__current_turn = current_turn
    self.__status = status
    self.__moves_played = moves_played

  def is_over(self):
    pass

  def player_move(self, player, start_x, start_y, end_x, end_y):
    # 1. start box 
    # 2. end box
    # 3. move
    # 4. call makeMove() method
    

  def make_move(self, move, player):
    # 1. Validation of source piece
    # 2. Check whether or not the color ofthe piece is white
    # 3. Check if it is a valid move or not
    # 4. Check whether it is a castling move or not
    # 5. Store the move