#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:40:35 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode

def reverse_even_length_groups(head):
    if head.next is None:
        return head
    clean, scanner, target = head, head, 1
    while scanner is not None:
        n = 0
        new_tail = scanner
        while n < target and scanner is not None:
            new_head = scanner
            scanner = scanner.next
            n += 1
        if n % 2 == 0:
            new_head.next = None
            clean.next = None
            prev, curr, nxt = None, new_tail, new_tail.next
            while curr is not None:
                curr.next = prev
                prev = curr
                curr = nxt
                if nxt is not None:
                    nxt = nxt.next
            clean.next = new_head
            new_tail.next = scanner
            clean = new_tail
        else:
            clean = new_head
        target += 1
    return head

ll = LinkedList()
ll.create_linked_list([1,2,3,4])
curr = reverse_even_length_groups(ll.head)
while curr is not None:
    print(curr.data)
    curr = curr.next
