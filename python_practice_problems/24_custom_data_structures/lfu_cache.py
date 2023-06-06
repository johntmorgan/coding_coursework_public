#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:03:54 2023

@author: johnmorgan
"""

import collections
from lfu_linked_list import DLinkedList
from lfu_linked_listnode_dict import LinkedListNode
        
class LFUCache:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.node_dict = dict() # key: Node
        self.freq_dict = collections.defaultdict(DLinkedList)
        self.min_freq = 0
        
    def update_node(self, node):
        freq = node.freq
        self.freq_dict[freq].pop(node)
        if self.min_freq == freq and not self.freq_dict[freq]:
            self.min_freq += 1
        node.freq += 1
        freq = node.freq
        self.freq_dict[freq].append(node)
    
    def get(self, key):
        if key not in self.node_dict:
            return -1
        node = self.node_dict[key]
        self.update_node(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.node_dict:
            node = self.node_dict[key]
            self.update_node(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.freq_dict[self.min_freq].pop()
                del self.node_dict[node.key]
                self.size -= 1
            node = LinkedListNode(key, value)
            self.node_dict[key] = node
            self.freq_dict[1].append(node)
            self.min_freq = 1
            self.size += 1
            

# from lfu_linked_list import LinkedList
# from lfu_linked_listnode_dict import LinkedListNode

# class LFUCache(object):
#     def __init__(self, capacity):
#         self.size = 0
#         self.capacity = capacity
#         self.val_dict = {}
#         self.freq_dict = {}
    
#     def get(self, key):
#         if key in self.val_dict:
#             self.freq_dict[key] += 1
#             return self.val_dict[key]
#         else:
#             return -1
    
#     def put(self, key, value):
#         if key in self.val_dict:
#             self.freq_dict[key] += 1
#             self.val_dict[key] = value
#         else:
#             if self.size < self.capacity:
#                 self.freq_dict[key] = 1
#                 self.val_dict[key] = value
#                 self.size += 1
#             else:
#                 low = min(self.freq_dict, key=self.freq_dict.get)
#                 del self.val_dict[low]
#                 del self.freq_dict[low]
#                 self.freq_dict[key] = 1
#                 self.val_dict[key] = value
                
                
# class LFUCache(object):
#     def __init__(self, capacity):
#         self.ll = LinkedList()
#         self.node_dict = {}
#         self.freq_dict = {}
#         self.capacity = capacity
#         self.size = 0
    
#     def get(self, key):
#         if key in self.node_dict:
#             self.freq_dict[key] += 1
#             return self.node_dict[key].val
#         else:
#             return -1

#     def put(self, key, value):
#         if key in self.node_dict:
#             self.freq_dict[key] += 1
#         else:
#             if self.size < self.capacity:
#                 node = LinkedListNode(key, value, 1)
#                 self.ll.append(node)
#                 self.node_dict[key] = self.ll.tail
#                 self.size += 1
#             else:
#                 low = min(self.freq_dict, key=self.freq_dict.get)
#                 self.ll.delete(self.node_dict[low])
#                 del self.node_dict[low]
#                 del self.freq_dict[low]
#                 node = LinkedListNode(key, value, 1)
#                 self.ll.append(node)
#                 self.node_dict[key] = self.ll.tail
#             self.freq_dict[key] = 1