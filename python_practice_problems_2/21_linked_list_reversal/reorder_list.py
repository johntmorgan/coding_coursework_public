#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:46:06 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode
            
def reorder_list(head):
    if head.next == None:
        return head
    fast, slow = head, head
    while fast is not None:
        l1_end = slow
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next
    l1_end.next = None
    prev, curr, nxt = None, slow, slow.next
    while curr is not None:
        curr.next = prev
        prev = curr
        curr = nxt
        if nxt is not None:
            nxt = nxt.next
    l1 = head
    l2 = prev
    while l1 is not None:
        if l2 is not None:
            tmp = l1.next
            l1.next = l2
            old_l2 = l2
            l2 = l2.next
            old_l2.next = tmp
            l1 = tmp
        else:
            l1 = l1.next
    return head

ll = LinkedList()
ll.create_linked_list([1,1,2,2,3,-1,10,12])
curr = reorder_list(ll.head)
while curr is not None:
    print(curr.data)
    curr = curr.next
