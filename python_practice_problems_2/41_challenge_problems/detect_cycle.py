#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:45:03 2023

@author: johnmorgan
"""

from linked_list_2 import LinkedList

# O(n) space with hashmaps

def detect_cycle(head):
    node = head
    d = {}
    pos = 0
    while node is not None:
        if node.data in d.keys():
            return d[node.data]
        else:
            d[node.data] = pos
        node = node.next
        pos += 1
    return -1

# O(1) space with fast/slow
# When fast catches slow:
# x is length before cycle
# y is length beyond cycle where fast + slow meet
# fast catches slow (cycle length - non cycle into cycle)
# travel another non cycle and slow has completed a cycle while head has reached cycle

def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast: break
    if not fast or not fast.next:
        return -1
    pos = 0
    while head != slow:
        head, slow = head.next, slow.next
        pos += 1
    return pos

pos = 2
nums = [2,4,6,8,10]
ll = LinkedList()
ll.create_linked_list(nums)
node = ll.head
while node.next is not None:
    node = node.next
count = 0
node2 = ll.head
while count != pos:
    node2 = node2.next
    count += 1
node.next = node2
print(detect_cycle(ll.head))

pos = 0
nums = [1,3,5,7,9]
ll = LinkedList()
ll.create_linked_list(nums)
node = ll.head
while node.next is not None:
    node = node.next
count = 0
node2 = ll.head
while count != pos:
    node2 = node2.next
    count += 1
node.next = node2
print(detect_cycle(ll.head))

nums = [1,2,3,4,5]
ll = LinkedList()
ll.create_linked_list(nums)
node = ll.head
while node.next is not None:
    node = node.next
print(detect_cycle(ll.head))

pos = 3
nums = [0,2,3,5,6]
ll = LinkedList()
ll.create_linked_list(nums)
node = ll.head
while node.next is not None:
    node = node.next
count = 0
node2 = ll.head
while count != pos:
    node2 = node2.next
    count += 1
node.next = node2
print(detect_cycle(ll.head))

pos = 1
nums = [3,6,9,10,11]
ll = LinkedList()
ll.create_linked_list(nums)
node = ll.head
while node.next is not None:
    node = node.next
count = 0
node2 = ll.head
while count != pos:
    node2 = node2.next
    count += 1
node.next = node2
print(detect_cycle(ll.head))