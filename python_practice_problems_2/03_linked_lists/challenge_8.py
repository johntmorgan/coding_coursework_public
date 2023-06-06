#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:58:15 2023

@author: johnmorgan
"""

from LinkedList7 import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}

# O(n)
# Official solution = O(n^2) double loop because no hashes allowed yet

def remove_duplicates(lst):
    vals = {}
    prior_node = lst.get_head()
    curr_node = lst.get_head()
    vals[curr_node.data] = 1
    curr_node = curr_node.next_element
    while curr_node is not None:
        if curr_node.data in vals.keys():
            prior_node.next_element = curr_node.next_element
            curr_node = curr_node.next_element
        else:
            vals[curr_node.data] = 1
            prior_node = curr_node
            curr_node = curr_node.next_element

lst = LinkedList()
lst.insert_at_head(6)
lst.insert_at_head(5)
lst.insert_at_head(4)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.insert_at_head(2)
lst.insert_at_head(2)
lst.insert_at_head(1)

lst.print_list()
remove_duplicates(lst)
lst.print_list()