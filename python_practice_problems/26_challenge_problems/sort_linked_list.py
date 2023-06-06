#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:25:55 2023

@author: johnmorgan
"""

# Review
# Working on machine but not on Educative test suite...

from linked_list import *
from linked_list_node import *

def divide(head):
    fast, slow = head.next, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    curr = LinkedListNode(None)
    result = curr
    while left and right:
        if left.data < right.data:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    if left:
        curr.next = left
    if right:
        curr.next = right
    return result.next

def sort_list(head):
    if not head or not head.next:
        return head
    left = head
    right = divide(head)
    temp = right.next
    right.next = None
    right = temp
    left = sort_list(left)
    right = sort_list(right)
    head = merge(left, right)
    return head


data_list = [4, 2, 1, 3]
ll = LinkedList()
ll.create_linked_list(data_list)
curr = sort_list(ll.head)
while curr is not None:
    print(curr.data)
    curr = curr.next
 
data_list = [4, 2, 1, 5, 3]
ll = LinkedList()
ll.create_linked_list(data_list)
curr = sort_list(ll.head)
while curr is not None:
    print(curr.data)
    curr = curr.next
    
data_list = [-231, -59, -20, -532, -659, 486]
ll = LinkedList()
ll.create_linked_list(data_list)
curr = sort_list(ll.head)
while curr is not None:
    print(curr.data)
    curr = curr.next
    
data_list = [90,67,-89,11,12,34,-56,-100,47]
ll = LinkedList()
ll.create_linked_list(data_list)
curr = sort_list(ll.head)
while curr is not None:
    print(curr.data)
    curr = curr.next