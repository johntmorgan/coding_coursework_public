#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:54:50 2023

@author: johnmorgan
"""

from trie_node_5 import *


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
        node.is_string = True
    
    # Function to search a string from the trie
    def search(self, string_to_search):
        node = self.root
        for c in string_to_search:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return node.is_string
    
    # Function to search prefix of strings
    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return True

    # Function to delete the characters in the searched word that are not shared
    def remove_characters(self, string_to_delete):
        node = self.root
        child_list = []
    
        for c in string_to_delete:
            child_list.append([node, c])
            node = node.children[c]
        
        for pair in reversed(child_list):
            parent = pair[0]
            child_char = pair[1]
            target = parent.children[child_char]

            if target.children:
                return
            del parent.children[child_char]