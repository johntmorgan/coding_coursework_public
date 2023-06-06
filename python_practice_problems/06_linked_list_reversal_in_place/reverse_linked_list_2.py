#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:42:49 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode
            
def reverse_between(head, left, right):
    prior, start = None, head
    start_count = 1
    while start_count < left:
        prior = start
        start = start.next
        start_count += 1
    end, end_count = start, left
    while end_count < right:
        end = end.next
        end_count += 1
    tail = end.next
    end.next = None
    prev, curr, cnext = None, start, start.next
    while curr:
        curr.next = prev
        prev = curr
        curr = cnext
        if cnext:
            cnext = cnext.next
    if prior:
        prior.next = prev
    else:
        head = prev
    start.next = tail
    return head

ll = LinkedList()
left, right = 3, 6
nums = [1,2,7,4,5,4,3,10,1]
ll.create_linked_list(nums)
node = reverse_between(ll.head, left, right)
while node:
    print(node.data)
    node = node.next