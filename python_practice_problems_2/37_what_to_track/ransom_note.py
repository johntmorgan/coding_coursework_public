#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:56:09 2023

@author: johnmorgan
"""

def can_construct(ransom_note, magazine):
    hmap = {}
    for letter in magazine:
        if letter in hmap.keys():
            hmap[letter] += 1
        else:
            hmap[letter] = 1
    for letter in ransom_note:
        if letter not in hmap.keys():
            return False
        elif hmap[letter] == 0:
            return False
        else:
            hmap[letter] -= 1
    return True

ransom = "codinginterviewquestions"
magazine = "aboincsdefoetingvqtniewonoregessnutins"
print(can_construct(ransom, magazine))