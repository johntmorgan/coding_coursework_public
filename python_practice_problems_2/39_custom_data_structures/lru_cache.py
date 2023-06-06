#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 18:50:03 2023

@author: johnmorgan
"""

from linked_list import *

# Naive just using linked list = O(n) set and get, O(n) space
# Optimized using hash map to point to nodes: O(1) set and get, O(n) space

class LRUCache:
    def __init__(self, capacity):
        self.cache = LinkedList()
        self.cdict = {}
        self.capacity = capacity
        
    def get(self, key):
        if self.cache.size > 0:
            if key in self.cdict:
                node = self.cdict[key]
                self.cache.move_to_head(node)
                return node.second
            else:
                return -1
        else:
            return -1

    def set(self, key, value):
        if key in self.cdict:
            node = self.cdict[key]
            self.cache.move_to_head(node)
        else:
            self.cache.insert_at_head([key, value])
            self.cdict[key] = self.cache.head
            if self.cache.size > self.capacity:
                tail_key = self.cache.tail.first
                del self.cdict[tail_key]
                self.cache.remove_tail()
    
# lruc = LRUCache(2)
# print(lruc.get(10))
# lruc.set(10, 10)
# print(lruc.get(10))

# lruc = LRUCache(3)
# lruc.set(50, 50)
# lruc.set(51, 51)
# print(lruc.get(51))
# lruc.set(52, 52)
# lruc.set(53, 53)
# lruc.set(54, 54)
# print(lruc.get(53))
# lruc.set(55, 55)
# print(lruc.get(51))

lruc = LRUCache(2)
print(lruc.get(10))
lruc.set(10, 100)
print(lruc.get(10))
lruc.set(15, 50)
print(lruc.get(10))
lruc.set(30, 300)
print(lruc.get(15))
print(lruc.get(30))