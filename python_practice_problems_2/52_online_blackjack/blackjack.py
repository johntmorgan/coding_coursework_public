#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:16:58 2023

@author: johnmorgan
"""

# Enumeration
class Suit(enum.Enum):
  HEART = 1
  SPADE = 2
  CLUB = 3
  DIAMOND = 4

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
    
class Card:
  def __init__(self, suit, face_value):
    self.__suit = suit
    self.__face_value = face_value
    
class Deck:
  def __init__(self, cards):
    self.__cards = []

  def get_cards(self):
    None

class Shoe:
  def __init__(self, decks, number_of_decks):
    self.__decks = {}
    self.__number_of_decks = number_of_decks

  def create_shoe(self):
    None

  def shuffle(self):
    None

  def deal_card(self):
    None
    
class Hand:
  def __init__(self, cards):
    self.__cards = []

  def get_scores(self):
    None

  def add_card(self, card):
    None
    
from abc import ABC, abstractmethod
class Player:
  def __init__(self, id, password, balance, status, person, hand):
    self.__id = id
    self.__password = password
    self.__balance = balance
    self.__status = status
    self.__person = person
    self.__hand = hand

  def add_hand(self, hand):
    None
  def remove_hand(self, hand):
    None

  def reset_password(self):
    None
  def add_to_hand(self, hand):
    None

class BlackjackPlayer(Player):
  def __init__(self, id, password, balance, status, person, hand, bet, total_cash):
    super().__init__(id, password, balance, status, person, hand)
    self.__bet = bet
    self.__total_cash = total_cash

  def place_bet(self, bet):
    None
  
  def reset_password(self):
    # functionality

class Dealer(Player):
  def __init__(self, id, password, balance, status, person, hand):
    super().__init__(id, password, balance, status, person, hand)

  def get_total_score(self):
    None

  def reset_password(self):
    # functionality

class BlackjackController:
  def validate_action():
    None

class BlackjackGameView:
  def play_action(self, action, hand):
    None
    
class BlackjackGame:
  def __init__(self, player, dealer, shoe):
    self.__id = id
    self.__player = player
    self.__dealer = dealer
    self.__shoe = shoe
    self.__MAX_NUM_OF_DECKS = 4

  def play_action(action, hand):
    pass

  def hit(hand):
    pass

  def stand():
    pass

  def start():
    pass