#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:51:51 2023

@author: johnmorgan
"""

def can_construct(ransom_note, magazine):
    mag_dict = {}
    for letter in magazine:
        if letter in mag_dict:
            mag_dict[letter] += 1
        else:
            mag_dict[letter] = 1
    for letter in ransom_note:
        if letter in mag_dict:
            if mag_dict[letter] > 0:
                mag_dict[letter] -= 1
            else:
                return False
        else:
            return False
    return True

ransom_note = "codinginterviewquestions"
magazine = "aboincsdefoetingvqtniewonoregessnutins"
print(can_construct(ransom_note, magazine))