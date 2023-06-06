#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:17:05 2023

@author: johnmorgan
"""

import math
from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_traversal import traverse_linked_list
from linked_list_reversal import reverse_linked_list
            
# O(n)

def reverse_linked_list(head, k):
    scanner = head
    output_head = None
    last_tail = None
    while scanner is not None:
        count, start_reverse = 0,  scanner
        while count < k - 1 and scanner:
            scanner = scanner.next
            count += 1
        if scanner is not None:
            end_reverse = scanner
            scanner = scanner.next
            end_reverse.next = None
            if output_head is None:
                output_head = end_reverse
            prev, curr, nxt = None, start_reverse, start_reverse.next
            while curr is not None:
                curr.next = prev
                prev = curr
                curr = nxt
                if nxt is not None:
                    nxt = nxt.next
            if last_tail is not None:
                last_tail.next = prev
            last_tail = start_reverse
        else:
            last_tail.next = start_reverse
    if output_head is None:
        output_head = head
    return output_head

ll = LinkedList()
ll.create_linked_list([1,2,3,4,5])
k = 2
curr = reverse_linked_list(ll.head, k)
while curr is not None:
    print(curr.data)
    curr = curr.next