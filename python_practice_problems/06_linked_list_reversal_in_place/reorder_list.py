#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:05:43 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode

def reorder_list(head):
    if head.next == None:
        return head
    fast, slow, prior = head, head, None
    while fast:
        fast = fast.next
        prior = slow
        slow = slow.next
        if fast:
            fast = fast.next
    prior.next = None
    prev, curr, cnext = None, slow, slow.next
    while curr:
        curr.next = prev
        prev = curr
        curr = cnext
        if cnext:
            cnext = cnext.next
    first, second = head, prev
    while first and second:
        first_next = first.next
        first.next = second
        second_next = second.next
        second.next = first_next
        first, second = first_next, second_next
    return head

ll = LinkedList()
nums = [1,1,2,2,3,-1,10,12]
ll.create_linked_list(nums)
node = reorder_list(ll.head)
while node:
    print(node.data)
    node = node.next
