#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:55:35 2023

@author: johnmorgan
"""

from trie3 import Trie

def recurse_lex(trie, node, result, word=""):
    if node.is_string:
        result.append(int(word))
    for number in node.children.keys():
        recurse_lex(trie, node.children[number], result, word + number)

def lexicographical_order(n):
    trie = Trie()
    for num in range(1, n + 1):
        trie.insert(str(num))
    result = []
    recurse_lex(trie, trie.root, result)
    return result

print(lexicographical_order(22))