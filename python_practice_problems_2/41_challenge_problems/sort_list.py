#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:01:15 2023

@author: johnmorgan
"""
from linked_list import *
from linked_list_node import *

# Lazy O(nlogn), using O(n) external space

def sort_list(head):
    nums = []
    node = head
    while node is not None:
        nums.append(node.data)
        node = node.next
    nums.sort()
    node = head
    index = 0
    while node is not None:
        node.data = nums[index]
        node = node.next
        index += 1

# Correct way, key is fast/slow which I did correctly
# Review merge setup

def get_middle(head):
    if (head == None):
        return head
    slow, fast = head, head
    while (fast.next != None and 
           fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(l1, l2):
    result = None
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.data <= l2.data:
        result = l1
        result.next = merge(l1.next, l2)
    else:
        result = l2
        result.next = merge(l1, l2.next)
    return result
      
def sort_list(head):
    if head == None or head.next == None:
        return head
    middle = get_middle(head)
    head2 = middle.next
    middle.next = None
    left = sort_list(head)
    right = sort_list(head2)
    return merge(left, right)

nums = [90,67,-89,11,12,34,-56,-100,47]
ll = LinkedList()
ll.create_linked_list(nums)
result = sort_list(ll.head)
node = result
while node is not None:
    print(node.data)
    node = node.next