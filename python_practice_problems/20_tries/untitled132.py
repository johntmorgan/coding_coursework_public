#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:17:28 2023

@author: johnmorgan
"""

from trie_node_search_words import TrieNode


def suggested_products(products, search_word):
    trie_root = TrieNode()
    for product in products:
        node = trie_root
        node.search_words +=
        for letter in product:
            if letter in trie_root.children:
                
    

    return [[]]


products = ["mobile","mouse","moneypot","monitor","mousepad"]
search_word = "mouse"