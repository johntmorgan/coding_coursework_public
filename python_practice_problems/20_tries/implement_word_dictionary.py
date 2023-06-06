#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:19:15 2023

@author: johnmorgan
"""

from trie_node import *

# Tip: You may use some of the code templates provided
# in the support files

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.word_arr = []

    def add_word(self, word):
        self.word_arr.append(word)
        node = self.root
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
            
    def search_word(self, word):
        curr_nodes = [self.root]
        next_nodes = []
        for c in word:
            while curr_nodes:
                curr = curr_nodes.pop(0)
                if c != ".":
                    if c in curr.children:
                        next_nodes.append(curr.children[c])
                else:
                    for child in curr.children:
                        next_nodes.append(curr.children[child])
            curr_nodes, next_nodes = next_nodes, curr_nodes
        for node in curr_nodes:
            if node.is_word:
                return True
        return False
            

    def get_words(self):
        return self.word_arr
    

# wd = WordDictionary()
# print(wd.add_word("bad"))
# print(wd.add_word("dad"))
# print(wd.add_word("mad"))
# print(wd.get_words())
# print(wd.search_word("bad"))
# print(wd.search_word(".ad"))
# print(wd.search_word("b.."))
# print(wd.search_word("b.g"))
# print(wd.get_words())

wd = WordDictionary()
print(wd.get_words())
print(wd.add_word("apple"))
print(wd.add_word("grape"))
print(wd.get_words())
print(wd.search_word("strawberry"))
print(wd.add_word("banana"))
print(wd.add_word("banan"))
print(wd.search_word("bana.."))
print(wd.get_words())