#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:55:51 2023

@author: johnmorgan
"""

class FreqStack:
    def __init__(self):
        self.freq_dict = {}
        self.freq_group = {}
        self.max_freq = 0
        
    def push(self, value):
        if value in self.freq_dict:
            self.freq_dict[value] += 1
        else:
            self.freq_dict[value] = 1
        frequency = self.freq_dict[value]
        if frequency in self.freq_group:
            self.freq_group[frequency].append(value)
        else:
            self.freq_group[frequency] = [value]
        if frequency > self.max_freq:
            self.max_freq += 1
                     
    def pop(self):
        if self.max_freq > 0:
            val = self.freq_group[self.max_freq].pop()
            if not self.freq_group[self.max_freq]:
                self.max_freq -= 1
            return val
        else:
            return -1