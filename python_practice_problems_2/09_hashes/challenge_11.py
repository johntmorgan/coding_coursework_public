#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:08:26 2023

@author: johnmorgan
"""

from LinkedList import LinkedList
from Node import Node

# O(n), lousy way to do it

def remove_duplicates(lst):
    d = dict()
    curr = lst.get_head()
    while curr != None:
        if curr.data in d.keys():
            d[curr.data] = d[curr.data] + 1
        else:
            d[curr.data] = 1
        curr = curr.next_element
    prior = None
    curr = lst.get_head()
    while curr != None:
        if d[curr.data] == 1:
            prior = curr
            curr = curr.next_element
        else:
            if d[curr.data] > 1:
                d[curr.data] = -1
                prior = curr
                curr = curr.next_element
            else:
                if prior != None:
                    prior.next_element = curr.next_element
                else:
                    lst.head_node = curr.next_element
                curr = curr.next_element

# O(n) simple set
# Review, had a clumsy answer here
# Iterate over set, if have seen before delete node

def remove_duplicates(lst):
    s = set()
    prior = None
    curr = lst.get_head()
    while curr != None:
        if curr.data not in s:
            s.add(curr.data)
            prior = curr
            curr = curr.next_element
        else:
            if prior != None:
                prior.next_element = curr.next_element
            else:
                lst.head_node = curr.next_element
            curr = curr.next_element

ll = LinkedList()
ll.insert_at_head(6)
ll.insert_at_head(5)
ll.insert_at_head(4)
ll.insert_at_head(4)
ll.insert_at_head(3)
ll.insert_at_head(2)
ll.insert_at_head(2)
ll.insert_at_head(2)
ll.insert_at_head(1)
ll.print_list()
remove_duplicates(ll)
ll.print_list()
