#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:52:13 2023

@author: johnmorgan
"""

from linked_list import LinkedList

def detect_cycle(head):
    fast, slow = head, head
    while fast is not None:
        fast = fast.next
        if fast:
            fast = fast.next
        slow = slow.next
        if fast == slow:
            return True
    return False

ll = LinkedList()
arr = [2, 4, 6, 8, 10]
index = 2
ll.create_linked_list(arr)
# curr = ll.head
# while curr.next is not None:
#     curr = curr.next
# target = ll.head
# count = 0
# while count != index:
#     target = target.next
#     count += 1
# curr.next = target
print(detect_cycle(ll.head))