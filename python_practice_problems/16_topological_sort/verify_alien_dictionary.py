#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:24:07 2023

@author: johnmorgan
"""

# O(m) where m is total number of letters in words
# O(1) space - only 26 letters to store ever

def verify_alien_dictionary(words, order):
    if len(words) < 2:
        return True
    lrank = {}
    for index, letter in enumerate(order):
        lrank[letter] = index + 1
    for index, word in enumerate(words):
        if index < len(words) - 1:
            next_word = words[index + 1]
            l_index = 0
            validated = False
            while not validated and l_index < len(word) and l_index < len(next_word):
                if word[l_index] == next_word[l_index]:
                    l_index += 1
                else:
                    if lrank[word[l_index]] < lrank[next_word[l_index]]:
                        validated = True
                    else:
                        return False
            if not validated and len(next_word) < len(word):
                return False   
    return True
    
    
words = ["passengers","to","the","unknown"]
order = "ptuabcdefghijklmnoqrsvwxyz"
print(verify_alien_dictionary(words, order))

words = ["passengers","to","the","unknown"]
order = "ptuabcdefgoijklmnhqrsvwxyz"
print(verify_alien_dictionary(words, order))

words = ["marvellous", "marvel"]
order = "marvelbcdfghijknopqstuwxyz"
print(verify_alien_dictionary(words, order))