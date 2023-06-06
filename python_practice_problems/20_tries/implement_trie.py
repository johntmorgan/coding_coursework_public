#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:07:13 2023

@author: johnmorgan
"""

from trie_node import *

class Trie():
    def __init__(self):
        self.root = TrieNode()

    # inserting string in trie
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                node.children[letter] = TrieNode()
                node = node.children[letter]
        node.is_word = True

    # searching for a string
    def search(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        return node.is_word

    def search_prefix(self, prefix):
        node = self.root
        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        return True
        
        
t = Trie()
print(t.insert("apple"))
print(t.search("apple"))
print(t.search("app"))
print(t.search_prefix("app"))
print(t.insert("app"))
print(t.search("app"))