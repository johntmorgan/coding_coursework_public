#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:08:22 2023

@author: johnmorgan
"""

from trie_3 import Trie

def replace_words(sentence, dictionary):
    trie = Trie()
    for entry in dictionary:
        trie.insert(entry)
    sent = sentence.strip().split(" ")
    output = ""
    for word in sent:
        output += trie.replace(word)
        output += " "
    return output.strip()
    
    
sentence = "where there is a will there is a way"
dictionary = ["wi","wa","w"]
print(replace_words(sentence, dictionary))