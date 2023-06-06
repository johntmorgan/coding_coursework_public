#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:50:46 2023

@author: johnmorgan
"""

from trie_node import *

# All functions O(l) - l is word length
# Space - insert O(l), others O(1)

class Trie():
    def __init__(self):
        self.root = TrieNode()
        return None
    
    def insert(self, string):
        node = self.root
        for char in string:
            if char in node.children.keys():
                node = node.children[char]
            else:
                node.children[char] = TrieNode()
                node = node.children[char]
        node.is_word = True
    
    def search(self, string):
        node = self.root
        for char in string:
            if char in node.children.keys():
                node = node.children[char]
            else:
                return False
        if node.is_word:
            return True
        else:
            return False
        return node.is_word
        
    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children.keys():
                node = node.children[char]
            else:
                return False
        return True


t = Trie()
t.insert("apple")
print(t.search("apple"))
print(t.search("app"))
print(t.search_prefix("app"))
t.insert("app")
print(t.search("app"))