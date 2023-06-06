#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:29:48 2023

@author: johnmorgan
"""

from trie2 import *

# Tip: You may use some of the code templates provided
# in the support files

# Time O(m) add, search O(m), wildcard_search O(26^m), get words O(n * 26^m)
# Space O(n * m), search O(m) for recursion stack, get words O(n * m)

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def add_word(self, word):
        self.trie.insert(word)

    def recurse_search(self, node, word):
        if word == "" and node.is_word:
            return True
        elif word == "":
            return False
        else:
            letter = word[0]
            if letter in node.children.keys():
                node = node.children[letter]
                return self.recurse_search(node, word[1:])
            elif letter == "." and len(node.children.keys()) > 0:
                any_work = False
                for next_letter in node.children.keys():
                    works = self.recurse_search(node.children[next_letter], word[1:])
                    if works == True:
                        any_work = True 
                return any_work
            else:
                return False
        return False
        
    def search_word(self, word):
        node = self.trie.root
        return self.recurse_search(node, word)

    def recurse_words(self, node, curr, words):
        if node.is_word:
            words.append(curr)
        if node.children == {}:
            return
        for letter in node.children.keys():
            self.recurse_words(node.children[letter], curr + letter, words)
            
    def get_words(self):
        words = []
        node = self.trie.root
        self.recurse_words(node, "", words)
        return words

# wd = WordDictionary()
# wd.add_word("bad")
# wd.add_word("dad")
# wd.add_word("mad")
# print(wd.get_words())
# print(wd.search_word("pad"))
# print(wd.search_word("bad"))
# print(wd.search_word(".ad"))
# print(wd.search_word("b.."))
# print(wd.get_words())

wd = WordDictionary()
wd.add_word("hi")
print(wd.search_word("h."))