#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:20:28 2023

@author: johnmorgan
"""

import math
from linked_list import LinkedList
from linked_list_node import LinkedListNode
            
def reverse_linked_list(head, k):
    first_reverse = True
    start, end, tail = head, head, None
    counter = 1
    while end:
        while end and counter <= k:
            prior = end
            end = end.next
            counter += 1
        if counter > k:
            prior.next = None
            prev, curr, cnext = None, start, start.next
            while curr:
                curr.next = prev
                prev = curr
                curr = cnext
                if cnext:
                    cnext = cnext.next
            if first_reverse:
                head = prev
                first_reverse = False
            else:
                tail.next = prev
            tail = start
            start = end
            counter = 1
        else:
            tail.next = start
    return head


ll = LinkedList()
k = 2
nums = [1,2,3,4,5]
ll.create_linked_list(nums)
node = reverse_linked_list(ll.head, k)
while node:
    print(node.data)
    node = node.next
