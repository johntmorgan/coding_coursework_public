#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:56:59 2023

@author: johnmorgan
"""

from linked_list import *

def swap_pairs(head):
    prior, start, end, tail = None, head, head, None
    while start and start.next:
        end = start.next
        tail = end.next
        end.next = start
        if prior:
            prior.next = end
        else:
            head = end
        start.next = tail
        prior = start
        start, end = tail, tail
    return head
    
ll = LinkedList()
nums = [1,2,3,4,5,6]
ll.create_linked_list(nums)
node = swap_pairs(ll.head)
while node:
    print(node.data)
    node = node.next
    
ll = LinkedList()
nums = [1,2,3,4,5,6,7]
ll.create_linked_list(nums)
node = swap_pairs(ll.head)
while node:
    print(node.data)
    node = node.next
    
ll = LinkedList()
nums = [1,2]
ll.create_linked_list(nums)
node = swap_pairs(ll.head)
while node:
    print(node.data)
    node = node.next
    
ll = LinkedList()
nums = [1]
ll.create_linked_list(nums)
node = swap_pairs(ll.head)
while node:
    print(node.data)
    node = node.next