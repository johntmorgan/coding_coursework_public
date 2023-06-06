#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:53:21 2023

@author: johnmorgan
"""

from bucket import *

class MyHashMap():
    def __init__(self, key_space):
        self.key_space = key_space
        self.arr = [None] * key_space
    
    def put(self, key, value):
        bucket = key % self.key_space
        if not self.arr[bucket]:
            self.arr[bucket] = (key, value, None)
        else:
            node = self.arr[bucket][2]
            while node[2]:
                node = node[2]
            node[2] = (key, value, None)
    
    def get(self, key):
        bucket = key % self.key_space
        if self.arr[bucket] == None:
            return -1
        elif self.arr[bucket][0] == key:
            return self.arr[bucket][1]
        else:
            node = self.arr[bucket][2]
            while node is not None:
                node = node[2]
                if node[0] == key:
                    return node[1]
            return -1
                
    def remove(self, key):
        bucket = key % self.key_space
        if self.arr[bucket] == None:
            return -1
        elif self.arr[bucket][0] == key:
            if self.arr[bucket][2] == None:
                self.arr[bucket] = None
            else:
                self.arr[bucket] = self.arr[bucket][2]
            return
        else:
            prev = self.arr[bucket]
            node = self.arr[bucket][2]
            while node is not None:
                prev = node
                node = node[2]
                if node[0] == key:
                    prev[2] = node[2]
                    break
            return -1
            