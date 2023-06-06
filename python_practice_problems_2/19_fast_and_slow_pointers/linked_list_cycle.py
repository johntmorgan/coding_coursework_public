#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:59:26 2023

@author: johnmorgan
"""

# Naive approach
# Traverse list, store in set
# Return true if reach node already in set
# O(n) time complexity, but also O(n) space complexity

# Fast/slow: O(n) time complexity, O(1) space complexity

from linked_list import LinkedList

def detect_cycle(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

lst = [2,4,6,8,10]
ll = LinkedList()
ll.create_linked_list(lst)
curr = ll.head
while curr.data != 10:
    curr = curr.next
curr.next = ll.head
print(detect_cycle(ll.head))

lst2 = [1,3,5,7,9]
ll2 = LinkedList()
ll2.create_linked_list(lst2)
print(detect_cycle(ll2.head))

# [1,3,5,7,9] , -1
# [1,2,3,4,5] , 3
# [0,2,3,5,6] , -1
# [3,6,9,10,11] , 0