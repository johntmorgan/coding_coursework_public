#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:36:24 2023

@author: johnmorgan
"""

# Template for linked list node class

class LinkedListNode():
  def __init__(self, key, value):
      self.key = key
      self.val = value
      self.freq = 1
      self.next = None
      self.prev = None