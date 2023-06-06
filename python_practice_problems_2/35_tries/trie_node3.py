#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:05:03 2023

@author: johnmorgan
"""

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_string = False