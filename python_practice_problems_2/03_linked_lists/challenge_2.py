#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 18:58:19 2023

@author: johnmorgan
"""

from Node import Node
from LinkedList2 import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Searches a value in the given list.

# JM solution

# def search(lst, value):
#     if lst.is_empty():
#         return False
#     else:
#         curr_node = lst.get_head()
#         if curr_node.data == value:
#             return True
#         while curr_node.next_element:
#             curr_node = curr_node.next_element
#             if curr_node.data == value:
#                 return True
#         return False

# Better, more terse solution
# O(n) time complexity, O(1) space complexity

def search(lst, value):
    current_node = lst.get_head()
    while current_node:
        if current_node.data == value:
            return True
        current_node = current_node.next_element
    return False

# Recursive
# O(n) time complexity, O(n) space complexity

# def search(node, value):
#     if(not node):
#         return False
#     if(node.data is value):
#         return True
#     return search(node.next_element, value)

lst = LinkedList()

lst.insert_at_tail(4)
lst.insert_at_tail(10)
lst.insert_at_tail(90)
lst.insert_at_tail(5)

print(search(lst, 4))
print(search(lst, 5))
print(search(lst, 90))
print(search(lst, 15))