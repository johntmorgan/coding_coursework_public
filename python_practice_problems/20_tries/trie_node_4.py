#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:19:52 2023

@author: johnmorgan
"""

class TrieNode():
  def __init__(self):
    self.nodes = []
    self.complete = False
    for i in range (0, 26):
      self.nodes.append(None)