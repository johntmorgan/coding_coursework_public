#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:30:35 2023

@author: johnmorgan
"""

from Trie import Trie
from TrieNode import TrieNode

# My solution... O(mh + n) imo

def traverse(trie, curr, word, word_index):
    if curr.is_end_word and word_index == len(word):
        return True
    letter_index = ord(word[word_index]) - ord('a')
    if curr.children[letter_index] is not None:
        return traverse(trie, curr.children[letter_index], word, word_index + 1)
    elif curr.is_end_word:
        return traverse(trie, trie.root, word, word_index)
    return False

def is_formation_possible(dictionary, word):
    trie = Trie()
    for entry in dictionary:
        trie.insert(entry)
    word_index = 0
    return traverse(trie, trie.root, word, word_index)

# Course solution... O(mh + n^2), or O(n^2) if trie constructed, used repeatedly
# m words, average length h

# def is_formation_possible(dct, word):

#     # Create Trie and insert dctionary elements in it
#     trie = Trie()
#     for elem in dct:
#         trie.insert(elem)

#     # Get Root
#     current = trie.root

#     # Iterate all the letters of the word
#     for i in range(len(word)):
#         # get index of the character from Trie
#         char = trie.get_index(word[i])

#         # if the prefix of word does not exist, word would not either
#         if current.children[char] is None:
#             return False

#         # if the substring of the word exists as a word in trie,
#         # check whether rest of the word also exists,
#         # if it does return true
#         elif current.children[char].is_end_word:
#             if trie.search(word[i+1:]):
#                 print(word[:i + 1], word[i+1:])
#                 return True

#         current = current.children[char]

#     return False


dictionary = ["the", "hello", "there", "answer", "any", "by", "world", "their", "abc"]

word = "helloworld"
print(is_formation_possible(dictionary, word))
word = "hello"
print(is_formation_possible(dictionary, word))
word = "hellonope"
print(is_formation_possible(dictionary, word))