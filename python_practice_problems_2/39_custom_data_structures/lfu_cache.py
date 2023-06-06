#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:43:17 2023

@author: johnmorgan
"""

from linked_list_2 import LinkedList
from linked_list_node_2 import LinkedListNode

class LFUCache(object):
    def __init__(self, capacity):
        self.ll = LinkedList()
        self.node_dict = {}
        self.freq_dict = {}
        self.capacity = capacity
        self.size = 0
    
    def get(self, key):
        if key in self.node_dict:
            self.freq_dict[key] += 1
            return self.node_dict[key].val
        else:
            return -1

    def put(self, key, value):
        if key in self.node_dict:
            self.freq_dict[key] += 1
        else:
            if self.size < self.capacity:
                node = LinkedListNode(key, value, 1)
                self.ll.append(node)
                self.node_dict[key] = self.ll.tail
                self.size += 1
            else:
                low = min(self.freq_dict, key=self.freq_dict.get)
                self.ll.delete(self.node_dict[low])
                del self.node_dict[low]
                del self.freq_dict[low]
                node = LinkedListNode(key, value, 1)
                self.ll.append(node)
                self.node_dict[key] = self.ll.tail
            self.freq_dict[key] = 1

lfu = LFUCache(2)
lfu.put(1, 1)

lfu = LFUCache(2)
lfu.put(1, 1)

lfu = LFUCache(2)
print(lfu.get(10))
lfu.put(10, 100)
print(lfu.get(10))
lfu.put(15, 50)
print(lfu.get(10))
lfu.put(30, 300)
print(lfu.get(15))
print(lfu.get(30))