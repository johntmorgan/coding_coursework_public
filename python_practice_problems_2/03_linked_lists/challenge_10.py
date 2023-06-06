#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:59:05 2023

@author: johnmorgan
"""

from LinkedList9 import LinkedList
from Node import Node

# O(n) time complexity
# Can also advance end pointer n spots
# Then advance curr_node, stop when end pointer hits end

def find_nth(lst, n):
    length = lst.length()
    if n < length:
        target = length - n
    else:
        return -1
    curr_node = lst.get_head()
    for _ in range(target):
        if curr_node is not None:
            curr_node = curr_node.next_element
    return curr_node.data

lst1 = LinkedList()
lst1.insert_at_head(99)
lst1.insert_at_head(39)
lst1.insert_at_head(47)
lst1.insert_at_head(78)
lst1.insert_at_head(60)
lst1.insert_at_head(18)
lst1.insert_at_head(22)
lst1.print_list()

int_list = find_nth(lst1, 3)