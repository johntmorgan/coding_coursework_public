#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:59:59 2023

@author: johnmorgan
"""

from linked_list import LinkedList

def get_middle_node(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
    
print(get_middle_node(None))