#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 14:16:25 2023

@author: johnmorgan
"""

from bucket import *

# Average-case complexity is O(1), worst-case O(n)
# Space - hashmap size m + key value pairs n = O(n + m)

class MyHashMap():
    # Use the constructor below to initialize the hashmap based on the keyspace
    def __init__(self, key_space):
        self.key_space = key_space
        self.arr = [None] * key_space

    def put(self, key, value):
        bucket = key % self.key_space
        if self.arr[bucket] == None:
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
        prev = self.arr[bucket]
        if self.arr[bucket] == None:
            return -1
        if self.arr[bucket][0] == key:
            if self.arr[bucket][2] == None:
                self.arr[bucket] = None
            else:
                node = self.arr[bucket][2]
                while node is not None:
                    prev = node
                    node = node[2]
                    if node[0] == key:
                        prev[2] = node[2]
                        break
    
hmap = MyHashMap(11)
hmap.put(15,250)
print(hmap.get(15))
print(hmap.get(5))
print(hmap.remove(5))