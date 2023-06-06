#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:48:45 2023

@author: johnmorgan
"""

from linked_list_node import LinkedListNode

class LinkedList():
    def __init__(self):
      self.head = None
      self.tail = None
    
    def append(self, node):
      node.next, node.prev = None, None  # avoid dirty node
      if self.head is None:
        self.head = node
      else:
        self.tail.next = node
        node.prev = self.tail
      self.tail = node
    
    def delete(self, node):
      if node.prev:
        node.prev.next = node.next
      else:
        self.head = node.next
      if node.next:
        node.next.prev = node.prev
      else:
        self.tail = node.prev
      node.next, node.prev = None, None