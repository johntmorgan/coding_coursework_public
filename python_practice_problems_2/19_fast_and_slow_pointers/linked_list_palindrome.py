#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:30:25 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list
from print_list import print_list_with_forward_arrow

# O(n), O(1) space complexity

def palindrome(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        if fast.next.next:
            fast = fast.next.next
        else:
            fast = fast.next
    if prev.data == prev.next.data:
        prev.next = None
        reverse_linked_list(slow)
        first, second = head, fast
    else:
        prev.next = None
        reverse_linked_list(slow)
        first, second = head, fast
    while first is not None and second is not None:
        if first.data != second.data:       
            return False
        first = first.next
        second = second.next
    return True


lst = [1,2,3,3,2,1]
ll = LinkedList()
ll.create_linked_list(lst)
print(palindrome(ll.head))

lst = [1,2,3,2,1]
ll = LinkedList()
ll.create_linked_list(lst)
print(palindrome(ll.head))

lst = [1,2,3,5,2,1]
ll = LinkedList()
ll.create_linked_list(lst)
print(palindrome(ll.head))

lst = [1,2,3,4,1]
ll = LinkedList()
ll.create_linked_list(lst)
print(palindrome(ll.head))