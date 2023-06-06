#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:16:38 2023

@author: johnmorgan
"""

from LinkedList9 import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Returns a list containing the union of list1 and list2


def union(list1, list2):
    vals = {}
    prior_node = list1.get_head()
    curr_node = list1.get_head()
    vals[curr_node.data] = 1
    curr_node = curr_node.next_element
    while curr_node.next_element is not None:
        if curr_node.data in vals.keys():
            prior_node.next_element = curr_node.next_element
            curr_node = curr_node.next_element
        else:
            vals[curr_node.data] = 1
            prior_node = curr_node
            curr_node = curr_node.next_element
    curr_node.next_element = list2.get_head()
    while curr_node.next_element is not None:
        if curr_node.data in vals.keys():
            prior_node.next_element = curr_node.next_element
            curr_node = curr_node.next_element
        else:
            vals[curr_node.data] = 1
            prior_node = curr_node
            curr_node = curr_node.next_element
    return list1

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    vals = {}
    curr_node = list1.get_head()
    while curr_node.next_element is not None:
        if curr_node.data in vals.keys():
            vals[curr_node.data] = vals[curr_node.data] + 1
        else:
            vals[curr_node.data] = 1
        curr_node = curr_node.next_element
    curr_node.next_element = list2.get_head()
    while curr_node.next_element is not None:
        if curr_node.data in vals.keys():
            vals[curr_node.data] = vals[curr_node.data] + 1
        else:
            vals[curr_node.data] = 1
        curr_node = curr_node.next_element
    list1 = LinkedList()
    for key in vals.keys():
        if vals[key] > 1:
            list1.insert_at_tail(key)
    return list1

# lst1 = LinkedList()
# lst1.insert_at_head(60)
# lst1.insert_at_head(80)
# lst1.insert_at_head(20)
# lst1.insert_at_head(10)
# lst1.print_list()

# lst2 = LinkedList()
# lst2.insert_at_head(45)
# lst2.insert_at_head(60)
# lst2.insert_at_head(30)
# lst2.insert_at_head(20)
# lst2.insert_at_head(15)
# lst2.print_list()

# union_list = union(lst1, lst2)
# union_list.print_list()

lst1 = LinkedList()
lst1.insert_at_head(60)
lst1.insert_at_head(80)
lst1.insert_at_head(20)
lst1.insert_at_head(10)
lst1.print_list()

lst2 = LinkedList()
lst2.insert_at_head(45)
lst2.insert_at_head(60)
lst2.insert_at_head(30)
lst2.insert_at_head(20)
lst2.insert_at_head(15)
lst2.print_list()

int_list = intersection(lst1, lst2)
int_list.print_list()

# lst.print_list()
# remove_duplicates(lst)
# lst.print_list()