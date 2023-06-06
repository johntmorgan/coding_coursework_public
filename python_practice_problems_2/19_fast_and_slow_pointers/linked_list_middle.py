#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:22:29 2023

@author: johnmorgan
"""

# Naive
# Count number of nodes in list
# Then re-traverse list

# Better
# Use fast and slow to get answer in 1 traversal
# O(n) time, O(1) space

from linked_list import LinkedList

def get_middle_node(head):
    fast, slow = head, head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

lst = [1,2,3,4,5]
ll = LinkedList()
ll.create_linked_list(lst)
print(get_middle_node(ll.head))

lst = [1,2,3,4,5,6]
ll = LinkedList()
ll.create_linked_list(lst)
print(get_middle_node(ll.head))