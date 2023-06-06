#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:17:28 2023

@author: johnmorgan
"""

# Insert O(w) - length of word
# Search in O(m) - length of search
# Space O(p) - total chars in all words

from trie_node_search_words import TrieNode

def suggested_products(products, search_word):
    products.sort()
    trie_root = TrieNode()
    for product in products:
        node = trie_root
        node.search_words.append(product)
        for letter in product:
            if letter in node.children:
                node = node.children[letter]
            else:
                node.children[letter] = TrieNode()
                node = node.children[letter]
            node.search_words.append(product)
    result = []
    node = trie_root
    for letter in search_word:
        if letter in node.children:
            node = node.children[letter]
            result.append(node.search_words[:3])
        else:
            result.append([])
    return result


products = ["mobile","mouse","moneypot","monitor","mousepad"]
search_word = "mouse"
print(suggested_products(products, search_word))