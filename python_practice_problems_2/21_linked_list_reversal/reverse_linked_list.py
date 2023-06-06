#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 17:38:56 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode
            
def reverse(head):
    prev, curr, cnext = None, head, head.next
    while curr is not None:
        curr.next = prev
        prev = curr
        curr = cnext
        if cnext is not None:
            cnext = cnext.next
    return prev
    
ll = LinkedList()
ll.create_linked_list([28,21,14,7])
reverse(ll.head)
curr = ll.head
while curr is not None:
    print(curr.data)
    curr = curr.next