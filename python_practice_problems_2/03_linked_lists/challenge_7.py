#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:48:16 2023

@author: johnmorgan
"""

from Node import Node
from LinkedList7 import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}

# O(n)

def find_mid(lst):
    length = lst.length()
    if length % 2 == 0:
        target = length // 2
    else:
        target = length // 2 + 1
    temp = lst.get_head()
    for node in range(target - 1):
        temp = temp.next_element
    return temp.data

# Still O(n), but more efficient
# Use fast and slow pointer
# Fast pointer moves 2 steps, slow pointer moves 1 step
# Return when fast pointer reaches end of list

def find_mid(lst):
    if lst.is_empty():
        return None
    current_node = lst.get_head()
    if current_node.next_element == None:
        return current_node.data
    mid_node = current_node
    current_node = current_node.next_element.next_element
    while current_node:
        mid_node = mid_node.next_element
        current_node = current_node.next_element
        if current_node:
            current_node = current_node.next_element
    if mid_node:
        return mid_node.data
    else:
        return None


lst = LinkedList()

for i in range(11):
    lst.insert_at_head(i)

lst.print_list()
print(find_mid(lst))

lst.delete_at_head()

lst.print_list()
print(find_mid(lst))

lst.delete_at_head()

lst.print_list()
print(find_mid(lst))