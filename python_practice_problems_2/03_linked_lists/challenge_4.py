#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:53:46 2023

@author: johnmorgan
"""

from Node import Node
from LinkedList4 import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Node class attributes: {data, next_element}

# Time complexity O(n)

def length(lst):
    node = lst.get_head()
    length = 0
    while node is not None:
        node = node.next_element
        length += 1
    return length

lst = LinkedList()

for i in range(11):
    lst.insert_at_head(i)

lst.print_list()
print(length(lst))

lst.delete_at_head()

lst.print_list()
print(length(lst))