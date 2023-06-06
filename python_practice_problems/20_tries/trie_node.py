#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:08:26 2023

@author: johnmorgan
"""

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False