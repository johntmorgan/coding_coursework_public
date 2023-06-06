#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:47:25 2023

@author: johnmorgan
"""

from linked_list import LinkedList

def palindrome(head):
    fast, slow = head, head
    while fast is not None:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    prev = None
    curr = slow
    nxt = curr.next
    while curr is not None:
        curr.next = prev
        prev = curr
        curr = nxt
        if nxt:
            nxt = nxt.next
    first, second = head, prev
    while first is not None and second is not None:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next
    return True

arr = [1,2,3,2,1]
ll = LinkedList()
ll.create_linked_list(arr)
print(palindrome(ll.head))

arr = [1,2,3,4,1]
ll = LinkedList()
ll.create_linked_list(arr)
print(palindrome(ll.head))

arr = [1,2,3,3,2,1]
ll = LinkedList()
ll.create_linked_list(arr)
print(palindrome(ll.head))

arr = [1,2,3,4,2,1]
ll = LinkedList()
ll.create_linked_list(arr)
print(palindrome(ll.head))