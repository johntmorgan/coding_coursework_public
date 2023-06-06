#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:31:38 2023

@author: johnmorgan
"""

from Trie import Trie
from TrieNode import TrieNode

# Cheesing it by array length (mutating)

def total_words_helper(curr, words):
    if curr.is_end_word == True:
        words.append([1])
    for letter_index in range(26):
        if curr.children[letter_index] is not None:
            total_words_helper(curr.children[letter_index], words)
    return

def total_words(root):
    if root is None:
        return 0
    words = []
    total_words_helper(root, words)
    return len(words)

# Proper solution without array
# O(n), must traverse every node

def total_words(root):
	result = 0
	if root.is_end_word:
		result += 1
	for letter in root.children:
		if letter is not None:
			result += total_words(letter)
	return result


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
print(total_words(trie.root))