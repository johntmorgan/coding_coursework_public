#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:52:35 2023

@author: johnmorgan
"""

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False