#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:20:42 2023

@author: johnmorgan
"""

from Trie import Trie
from TrieNode import TrieNode

# O(n), must traverse all nodes

def traverse_trie(curr, sorted_list, curr_word):
    temp_word = curr_word        
    if curr.is_end_word:
        sorted_list += [temp_word]
    for index in range(26):
        if curr.children[index] is not None:
            curr_word = temp_word + chr(index + 97)
            traverse_trie(curr.children[index], sorted_list, curr_word)

def sort_list(keys):
    if keys == None or len(keys) == 0:
        return "Bad array"
    trie = Trie()
    for key in keys:
        trie.insert(key)
    sorted_list = []
    curr_word = ""
    traverse_trie(trie.root, sorted_list, curr_word)
    return sorted_list

# Course solution, same idea

def get_words(root, result, level, word):
    # Leaf denotes end of a word
    if (root.is_end_word):
        # current word is stored till the 'level' in the character array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(temp)

    for i in range(26):
        if (root.children[i] is not None):
            # Non-null child, so add that index to the character array
            word[level] = chr(i + ord('a'))
            get_words(root.children[i], result, level + 1, word)


def sort_list(arr):
    result = []

    # Creating Trie and Inserting words from array
    trie = Trie()
    for word in arr:
        trie.insert(word)

    word = [''] * 20
    get_words(trie.root, result, 0, word)
    return result

keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their","abc"]
print(sort_list(keys))