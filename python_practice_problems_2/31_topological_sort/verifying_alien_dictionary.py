#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:39:47 2023

@author: johnmorgan
"""

# O(n) to store letters
# O(m) to iterate over all letters in words
# O(m) because O(n) is O(1), fixed number of letters
# O(1) space, fixed size b/c fixed number of letters
 
def verify_alien_dictionary(words, order):
    odict = {}
    for index in range(len(order)):
        odict[order[index]] = index
    for index in range(len(words) - 1):
        word1 = words[index]
        word2 = words[index + 1]
        wlen = min(len(word1), len(word2))
        matched, index = False, 0
        while not matched and index < wlen:
            if word1[index] == word2[index]:
                index += 1
            else: 
                if odict[word1[index]] > odict[word2[index]]:
                    return False
                matched = True
        if len(word1) > len(word2) and word1[:wlen] == word2[:wlen]:
            return False
    return True
        

words = ["passengers","the","to","unknown"]
order = "ptuabcdefghijklmnoqrsvwxyz"
print(verify_alien_dictionary(words, order))

words = ["passengers","to","the","unknown"]
order = "ptuabcdefghijklmnoqrsvwxyz"
print(verify_alien_dictionary(words, order))