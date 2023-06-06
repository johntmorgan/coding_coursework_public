#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:20:09 2023

@author: johnmorgan
"""

from trie import Trie

def replace_words(sentence, dictionary):
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    sent_arr = sentence.split()
    for index, word in enumerate(sent_arr):
        short = trie.replace(word)
        sent_arr[index] = short
    return " ".join(sent_arr)

sent = "where there is a will there is a way"
dict_arr = ["wi","wa","w"]
print(replace_words(sent, dict_arr))