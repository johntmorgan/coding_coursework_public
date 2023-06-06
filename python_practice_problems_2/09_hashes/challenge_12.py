#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:37:12 2023

@author: johnmorgan
"""

from LinkedList import LinkedList
from Node import Node

def union(list1, list2):
    s = set()
    curr = list1.get_head()
    while curr.next_element is not None:
        s.add(curr.data)
        curr = curr.next_element
    s.add(curr.data)
    prior = curr
    curr.next_element = list2.get_head()
    curr = curr.next_element
    while curr.next_element:
        if curr.data in s:
            prior.next_element = curr.next_element
            curr = curr.next_element
        else:
            prior = curr
            curr = curr.next_element
    return list1


def intersection(list1, list2):
    s = set()
    result_list = LinkedList()
    curr = list1.get_head()
    while curr is not None:
        s.add(curr.data)
        curr = curr.next_element
    curr = list2.get_head()
    while curr is not None:
        if curr.data in s:
            result_list.insert_at_head(curr.data)
        curr = curr.next_element
    return result_list
    

ll = LinkedList()
ll.insert_at_head(60)
ll.insert_at_head(80)
ll.insert_at_head(20)
ll.insert_at_head(10)
ll.print_list()
ll2 = LinkedList()
ll2.insert_at_head(45)
ll2.insert_at_head(60)
ll2.insert_at_head(30)
ll2.insert_at_head(20)
ll2.insert_at_head(15)
ll2.print_list()

# union(ll, ll2).print_list()

intersection(ll, ll2).print_list()

# print(intersection(ll, ll2))