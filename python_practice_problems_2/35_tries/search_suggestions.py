#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:56:19 2023

@author: johnmorgan
"""

from trie_node import TrieNode

# O(w) insertion
# O(m) search
# O(1) insert space, O(p) search, where p is number of chars in list

def recurse_trie(node, curr_word, pre_result, search_word):
    if node.is_word and curr_word not in pre_result:
        pre_result += [curr_word]
    if node.children == {}:
        return
    else:
        for child_letter in node.children.keys():
            recurse_trie(node.children[child_letter], curr_word + child_letter, 
                         pre_result, search_word)

def suggested_products(products, search_word):
    root = TrieNode()
    node = root
    for product in products:
        for char in product:
            if char in node.children.keys():
                node = node.children[char]
            else:
                node.children[char] = TrieNode()
                node = node.children[char]
        node.is_word = True
        node = root
    result = []
    for prefix in range(1, len(search_word) + 1):
        pre_result = []
        node = root
        target = search_word[:prefix]
        target_ok = True
        for char in target:
            if char in node.children.keys():
                node = node.children[char]
            else:
                target_ok = False
        if target_ok == True:
            if node.is_word:
                pre_result += [target]
            recurse_trie(node, target, pre_result, search_word)
            pre_result.sort()  
        result.append(pre_result[0:3])
    return result

# Course solution

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, data):
        node = self.root
        idx = 0
        for char in data:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(node.search_words) < 3:
                node.search_words.append(data)
            idx += 1

    def search(self, word):
        result, node = [], self.root
        for i, char in enumerate(word):
            if char not in node.children:
                temp = [[] for _ in range(len(word) - i)]
                return result + temp
            else:
                node = node.children[char]
                result.append(node.search_words[:])
        return result


def suggested_products(products, search_word):
    products.sort()
    trie = Trie()
    for x in products:
        trie.insert(x)
    return trie.search(search_word)

products = ["mobile","mouse","moneypot","monitor","mousepad"]
search_word = "mouse"
print(suggested_products(products, search_word))

products = ["havana"]
search_word = "tatiana"
print(suggested_products(products, search_word))