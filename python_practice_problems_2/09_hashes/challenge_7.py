#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 18:10:37 2023

@author: johnmorgan
"""

# O(m) complexity

def is_formation_possible(lst, word):
    c_dict = dict()
    for d_word in lst:
        if word[0:len(d_word)] == d_word:
            c_dict[word[len(d_word):len(word)]] = d_word
    for d_word in lst:
        keys = c_dict.keys()
        if d_word in keys:
            return True
    return False

# O(m + n^2)
# Book solution
# Review I guess

def is_formation_possible(lst, word):
    if len(word) < 2 or len(lst) < 2:
        return False
    hash_table = HashTable()
    for elem in lst:
        hash_table.insert(elem, True)
    for i in range(1, len(word)):
        # Slice the word into two strings in each iteration
        first = word[0:i]
        second = word[i:len(word)]
        check1 = False
        check2 = False
        if hash_table.search(first) is not None:
            check1 = True
        if hash_table.search(second) is not None:
            check2 = True
        # Return True If both substrings are present in the hash table
        if check1 and check2:
            return True
    return False

lst = ["the", "hello", "there", "answer", "any",
       "by", "world", "their","abc"]
word = "helloworld"
print(is_formation_possible(lst, word))
word = "helloworld"
print(is_formation_possible(lst, word))
word = "worldhello"
print(is_formation_possible(lst, word))
word = "hellothar"
print(is_formation_possible(lst, word))