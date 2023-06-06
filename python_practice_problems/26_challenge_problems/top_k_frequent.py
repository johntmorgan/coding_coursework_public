#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:58:17 2023

@author: johnmorgan
"""

def top_k_frequent(words, k):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    max_freq = 0
    freq_arr = {}
    for w_freq in freq:
        if freq[w_freq] in freq_arr:
            freq_arr[freq[w_freq]] += [w_freq]
        else:
            freq_arr[freq[w_freq]] = [w_freq]
        if freq[w_freq] > max_freq:
            max_freq = freq[w_freq]
    res = []
    while k > 0:
        if max_freq in freq_arr:
            curr = freq_arr[max_freq]
            curr.sort()
            while curr and k > 0:
                res.append(curr.pop(0))
                k -= 1
        max_freq -= 1
    return res
    
    
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(top_k_frequent(words, k))