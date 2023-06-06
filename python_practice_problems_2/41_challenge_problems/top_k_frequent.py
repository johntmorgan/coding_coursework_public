#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:21:28 2023

@author: johnmorgan
"""

def top_k_frequent(words, k):
    freq = {}
    words.sort()
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    by_freq = {}
    max_freq = 0
    for word in freq.items():
        if word[1] in by_freq:
            by_freq[word[1]] += [word[0]]
        else:
            by_freq[word[1]] = [word[0]]
        if word[1] > max_freq:
            max_freq = word[1]
    res = []
    while k > 0:
        top_freq = []
        while not top_freq:
            if max_freq in by_freq:
                top_freq = by_freq[max_freq]
            max_freq -= 1
        while top_freq != [] and k > 0:
            res.append(top_freq.pop(0))
            k -= 1
    return res

k = 3
words = ["lets","play","cricket","and","then","lets","play","badminton"]
print(top_k_frequent(words, k))