#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:33:35 2023

@author: johnmorgan
"""

class depth_fs:
  def __init__(self):
    self.root = trie_node()
    self.can_find = False

  def depth_first_search(self, node, target, i):
    # if word found, return true 
    if self.can_find:
        return
    # if node is NULL, return    
    if not root:
        return
    # if there's only one character in the word, check if it matches the query    
    if len(word) == i: 
        if root.complete:
            self.can_find = True
        return 
    index = ord(word[i]) - ord('a')
    self.depth_first_search(root.nodes[index], word, i + 1)
  