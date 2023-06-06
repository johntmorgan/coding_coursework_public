#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:01:23 2023

@author: johnmorgan
"""

import math
from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_traversal import traverse_linked_list
from linked_list_reversal import reverse_linked_list

def reverse_between(head, left, right):
    if left == right:
        return head
    count = 1
    scanner = head
    clean_left, clean_right = None, None
    while scanner is not None:
        if count == left - 1:
            clean_left = scanner
            scanner = scanner.next
            clean_left.next = None
        elif count == left:
            new_tail = scanner
            scanner = scanner.next
        elif count == right:
            new_head = scanner
            scanner = scanner.next
        elif count == right + 1:
            clean_right = scanner
            scanner = scanner.next
            new_head.next = None
        else:
            scanner = scanner.next
        count += 1
    prev, curr, nxt = None, new_tail, new_tail.next
    while curr is not None:
        curr.next = prev
        prev = curr
        curr = nxt
        if nxt is not None and nxt.next is not None:
            nxt = nxt.next
        else:
            nxt = None
    if clean_left is not None:
        clean_left.next = new_head
        new_head = head
    else:
        head = new_head
    if clean_right is not None:
        new_tail.next = clean_right
    return new_head
        

# ll = LinkedList()
# ll.create_linked_list([1,2,3,4,5])
# left, right = 2, 4
# curr = reverse_between(ll.head, left, right)
# while curr is not None:
#     print(curr.data)
#     curr = curr.next

ll = LinkedList()
ll.create_linked_list([1,2,3,4,5,6,3,2,1])
left, right = 1,9
curr = reverse_between(ll.head, left, right)
while curr is not None:
    print(curr.data)
    curr = curr.next
