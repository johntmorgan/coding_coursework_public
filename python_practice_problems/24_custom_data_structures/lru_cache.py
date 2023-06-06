#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:34:27 2023

@author: johnmorgan
"""

from linked_list import *

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.node_dict = {}
        self.cache = LinkedList()
    
    def get(self, key):
        if key in self.node_dict:
            node = self.node_dict[key]
            self.cache.move_to_head(node)
            return node.second
        else:
            return -1
        
    def set(self, key, value):
        if key in self.node_dict:
            node = self.node_dict[key]
            self.cache.move_to_head(node)
            node.second = value
        else:
            self.cache.insert_at_head([key, value])
            self.node_dict[key] = self.cache.head
            if self.cache.size > self.capacity:
                tail = self.cache.get_tail()
                del self.node_dict[tail.first]
                self.cache.remove_tail()
