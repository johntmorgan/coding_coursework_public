#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:02:07 2023

@author: johnmorgan
"""

# O(1) push and pop
# O(n) space where n is number of elements in freqstack

class FreqStack:
    def __init__(self):
        self.stack = []
        self.sdict = {}

    def push(self, value):
        self.stack.append(value)
        if value in self.sdict.keys():
            self.sdict[value] += 1
        else:
            self.sdict[value] = 1

    def pop(self):
        if len(self.stack) == 0:
            return None
        poss = []
        max_freq = 0
        for key, val in self.sdict.items():
            if val > max_freq:
                poss = [key]
                max_freq = val
            elif val == max_freq:
                poss.append(key)
        found_index = len(self.stack) - 1
        while self.stack[found_index] not in poss:
            found_index -= 1
        return_val = self.stack[found_index]
        self.stack = self.stack[:found_index] + self.stack[found_index + 1:]
        self.sdict[return_val] -= 1
        return return_val

# Review more clever course way of doing it building up dict
# Freq key, value = elems array
# Change max freq if none left in array

# O(1) push and pop
# O(n) space where n is number of elements in freqstack

from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.frequency = defaultdict(int)
        self.group = defaultdict(list)
        self.max_frequency = 0

    def push(self, value):
        freq = self.frequency[value] + 1
        self.frequency[value] = freq
        if freq > self.max_frequency:
            self.max_frequency = freq
        self.group[freq].append(value)

    def pop(self):
        value = ""
        if self.max_frequency > 0:
            value = self.group[self.max_frequency].pop()
            self.frequency[value] -= 1
            if not self.group[self.max_frequency]:
                self.max_frequency -= 1
        else:
            return -1
        return value
            
    
fs = FreqStack()
fs.push(5)
fs.push(7)
fs.push(7)
fs.push(5)
print(fs.pop())
print(fs.pop())
