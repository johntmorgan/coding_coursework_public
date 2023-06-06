#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:35:34 2023

@author: johnmorgan
"""

# Time complexity = O(n + n) = O(n)
# Space complexity O(n) - need to copy into list because strings immutable

def reverse_words(sentence):
    sent = [*sentence.strip()]
    sent.reverse()
    start, end = 0, 0
    while start < len(sent):
        while sent[end] != " " and end < len(sent) - 1:
            end += 1
        next_word_index = end + 1
        if next_word_index < len(sent):
            while sent[next_word_index] == " ":
                sent = sent[0:next_word_index] + sent[next_word_index + 1:len(sent)]
        if sent[end] == " ":
            end -= 1
        while end > start:
            sent[start], sent[end] = sent[end], sent[start]
            start += 1
            end -= 1
        start, end = next_word_index, next_word_index
    return "".join(sent)

sent = "We love Python"
print(reverse_words(sent))
sent = "To be or not to be"
print(reverse_words(sent))
sent = "You are amazing"
print(reverse_words(sent))
sent = "Hello     World"
print(reverse_words(sent))
sent = "Hey"
print(reverse_words(sent))