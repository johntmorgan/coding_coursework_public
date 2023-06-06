#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:33:40 2023

@author: johnmorgan
"""

from linked_list_node import *
from linked_list import *

def swap_pairs(head):
    scanner = head
    new_head = None
    while scanner is not None:
        start = scanner
        scanner = scanner.next
        if scanner is not None:
            finish = scanner
            scanner = scanner.next
        else:
            finish = None
        if finish is not None:
            finish.next = start
            start.next = scanner
            if new_head == None:
                new_head = finish
            else:
                last_end.next = finish
            last_end = start
        else:
            last_end.next = start
    return new_head

ll = LinkedList()
ll.create_linked_list([1,2,3,4, 5])
curr = swap_pairs(ll.head)
while curr is not None:
    print(curr.data)
    curr = curr.next