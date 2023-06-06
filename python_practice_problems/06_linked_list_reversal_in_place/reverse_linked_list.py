#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:10:07 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode

def reverse(head):
    prev, curr, nxt = None, head, head.next
    while curr:
        curr.next = prev
        prev = curr
        curr = nxt
        if nxt:
            nxt = nxt.next
    return prev

ll = LinkedList()
ll.create_linked_list([1,-2,3,4,-5,4,3,10,1])
node = reverse(ll.head)
while node:
    print(node.data)
    node = node.next
