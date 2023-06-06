#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 18:33:01 2023

@author: johnmorgan
"""

from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Inserts a value at the end of the list

# def insert_at_head(self, data):
#   temp_node = Node(data)
#   temp_node.next_element = self.head_node
#   self.head_node = temp_node
#   return self.head_node

# O(n), must traverse whole list

def insert_at_tail(lst, value):
    new_node = Node(value)
    if lst.is_empty():
        lst.head_node = new_node
    else:
        curr_node = lst.get_head()
        while curr_node.next_element:
            curr_node = curr_node.next_element
        curr_node.next_element = new_node

lst = LinkedList()
    
insert_at_tail(lst, 3)
insert_at_tail(lst, 5)
insert_at_tail(lst, 7)

lst.print_list()