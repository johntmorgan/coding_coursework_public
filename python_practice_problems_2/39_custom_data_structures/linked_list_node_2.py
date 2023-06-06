#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:48:51 2023

@author: johnmorgan
"""

# Template for linked list node class

class LinkedListNode():
  def __init__(self, key, value, freq):
      self.key = key
      self.val = value
      self.freq = freq
      self.next = None
      self.prev = None