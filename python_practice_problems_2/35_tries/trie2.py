#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:33:10 2023

@author: johnmorgan
"""

from trie_node import *


class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    # Function to insert a string in the trie
    def insert(self, string_to_insert):
        node = self.root
        for c in string_to_insert:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children.get(c)
        node.is_word = True
    
    # Function to search a string from the trie
    def search(self, string_to_search):
        node = self.root
        for c in string_to_search:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return node.is_word
    
    # Function to search prefix of strings
    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return True