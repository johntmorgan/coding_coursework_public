#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:40:43 2023

@author: johnmorgan
"""

from linked_list import LinkedList

def reverse_even_length_groups(head):
    prior, start, end, tail = head, head.next, head.next, None
    counter, target = 1, 2
    while end:
        while end and counter < target:
            end = end.next
            if end:
                counter += 1
        if counter % 2 == 0:
            if end:
                tail = end.next
                end.next = None
            else:
                tail = None
            prev, curr, cnext = None, start, start.next
            while curr:
                curr.next = prev
                prev = curr
                curr = cnext
                if cnext:
                    cnext = cnext.next
            prior.next = prev
            start.next = tail
            prior = start
            if end:
                start, end = tail, tail
        elif end:
            prior = end
            end = end.next
            start = end
        counter = 1
        target += 1
    return head
    

ll = LinkedList()
nums = [11,12,13,14,15]
ll.create_linked_list(nums)
node = reverse_even_length_groups(ll.head)
while node:
    print(node.data)
    node = node.next

ll = LinkedList()
nums = [11,12,13,14,15,16]
ll.create_linked_list(nums)
node = reverse_even_length_groups(ll.head)
while node:
    print(node.data)
    node = node.next
