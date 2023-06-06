#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:29:54 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode

def swap_nodes(head, k):
    scanner = head
    counter = 0
    while scanner:
        scanner = scanner.next
        counter += 1
    if k > counter:
        return head
    length = counter
    first = head
    counter = 1
    while counter < k:
        first = first.next
        counter += 1
    second = head
    counter = 1
    while counter < length - (k - 1):
        second = second.next
        counter += 1
    first.data, second.data = second.data, first.data
    return head
    
ll = LinkedList()
nums = [3,2,3,4,5,6]
ll.create_linked_list(nums)
k = 3
node = swap_nodes(ll.head, k)
while node:
    print(node.data)
    node = node.next