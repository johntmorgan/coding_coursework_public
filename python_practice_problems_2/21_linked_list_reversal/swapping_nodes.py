#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:21:27 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode

def swap_nodes(head, k):
    scanner = head
    count = 1
    while scanner is not None:
        if count == k:
            first = scanner
        scanner = scanner.next
        count += 1
    target = count - k
    count = 1
    scanner = head
    while count < target:
        scanner = scanner.next
        count += 1
    first.data, scanner.data = scanner.data, first.data
    return head

ll = LinkedList()
ll.create_linked_list([3,2,3,4,5,6])
k = 3
curr = swap_nodes(ll.head, k)
while curr is not None:
    print(curr.data)
    curr = curr.next

