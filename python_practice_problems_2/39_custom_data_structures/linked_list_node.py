#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 19:03:36 2023

@author: johnmorgan
"""

# Template for LinkedListNode class

class LinkedListNode:
    def __init__(self, pair):
        self.second = pair[1]
        self.first = pair[0]
        self.pair = pair
        self.next = None
        self.prev = None