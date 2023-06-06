#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:32:47 2023

@author: johnmorgan
"""

# Template for traversing a linked list

def reverse_linked_list(node):
  		temp = None
  		while node is not None:
  			next = node.next
  			node.next = temp
  			temp = node
  			node = next
  		return temp