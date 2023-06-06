#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:36:19 2023

@author: johnmorgan
"""

from lfu_linked_list_node import LinkedListNode

class DLinkedList():
    def __init__(self):
        self._sentinel = LinkedListNode(None, None) # dummy node
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1
    
    def pop(self, node=None):
        if self._size == 0:
            return
        if not node:
            node = self._sentinel.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node