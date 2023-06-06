#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:57:55 2023

@author: johnmorgan
"""

from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}

# On average O(n), lookup O(1)
# Can get to O(n^2) with lookup O(n) of course

def detect_loop(lst):
    s = set()
    curr = lst.get_head()
    while not curr == None:
        if curr.data in s:
            return True
        else:
            s.add(curr.data)
        curr = curr.next_element
    return False

ll = LinkedList()
ll.insert_at_head(7)
ll.insert_at_head(21)
ll.insert_at_head(14)
ll.insert_at_head(7)
ll.print_list()
print(detect_loop(ll))

ll2 = LinkedList()
ll2.insert_at_head(7)
ll2.insert_at_head(21)
ll2.insert_at_head(14)
ll2.print_list()
print(detect_loop(ll2))