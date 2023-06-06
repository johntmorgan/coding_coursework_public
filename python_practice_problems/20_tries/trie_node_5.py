#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:54:58 2023

@author: johnmorgan
"""

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_string = False