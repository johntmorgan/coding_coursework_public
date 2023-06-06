#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:46:32 2023

@author: johnmorgan
"""

from trie_5 import Trie

def recurse_trie(trie, node, seq, result):
    if node.is_string:
        result.append(int(seq))
    for child in node.children:
        recurse_trie(trie, node.children[child], seq + child, result)
    
def lexicographical_order(n):
    trie = Trie()
    for n in range(1, n + 1):
        trie.insert(str(n))
    result = []
    recurse_trie(trie, trie.root, "", result)
    return result

n = 22
print(lexicographical_order(n))