#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:19:41 2023

@author: johnmorgan
"""

# Template for Node class

class TrieNode(object):
    def __init__(self):
        self.search_words = []
        self.children = {}