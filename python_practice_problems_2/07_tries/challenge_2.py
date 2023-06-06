#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:57:10 2023

@author: johnmorgan
"""

from Trie import Trie
from TrieNode import TrieNode

# O(n) again, must traverse all nodes

def find_words_helper(curr, words, curr_word):
    new_word = curr_word
    if curr.is_end_word == True:
        words.append(curr_word)
    for letter_index in range(26):
        if curr.children[letter_index] is not None:
            curr_word = new_word + chr(letter_index + 97)
            find_words_helper(curr.children[letter_index], words, curr_word)
    return

def find_words(root):
    if root is None:
        return 0
    words = []
    find_words_helper(root, words, "")
    words.sort()
    return words

# Course solution

# def get_words(root, result, level, word):
#     if root.is_end_word:
#         temp = ""
#         for x in range(level):
#             temp += word[x]
#         result.append(str(temp))

#     for i in range(26):
#         if root.children[i]:
#             # Non-None child, so add that index to the character array
#             word[level] = chr(i + ord('a'))  # Add character for the level
#             get_words(root.children[i], result, level + 1, word)

# def find_words(root):
#     result = []
#     word = [None] * 20  # assuming max level is 20
#     get_words(root, result, 0, word)
#     return result


trie = Trie()
trie.insert('the')
trie.insert('a')
trie.insert('there')
trie.insert('answer')
trie.insert('any')
trie.insert('by')
trie.insert('bye')
trie.insert('their')
trie.insert('abc')
print(find_words(trie.root))