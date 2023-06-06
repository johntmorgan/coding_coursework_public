#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:27:19 2023

@author: johnmorgan
"""

from Node import Node
from LinkedListDAH import LinkedList

def delete_at_head(lst):
    first_element = lst.get_head()
    if first_element is not None:
        lst.head_node = first_element.next_element
        first_element.next_element = None
    return

lst = LinkedList()

for i in range(11):
    lst.insert_at_head(i)

lst.print_list()

delete_at_head(lst)
delete_at_head(lst)

lst.print_list()