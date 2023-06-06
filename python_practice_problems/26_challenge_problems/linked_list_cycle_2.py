#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:07:53 2023

@author: johnmorgan
"""

from linked_list import LinkedList

# Review

def detect_cycle(head):
    if (head == None or head.next == None):
        return None
    slow = head.next
    fast = head.next.next
    while fast and fast.next and slow != fast:
        slow = slow.next
        fast = fast.next.next
    if (slow != fast):
        return -1
    pos = 0
    slow = head
    while (slow != fast):
        slow = slow.next
        fast = fast.next
        pos += 1
    return pos


ll = LinkedList()
ll.create_linked_list([2,4,6,8,10])
target = ll.head
while target.data != 6:
    target = target.next
connection = ll.head
while connection.next:
    connection = connection.next
connection.next = target
print(detect_cycle(ll.head))

ll = LinkedList()
ll.create_linked_list([1,3,5,7,9])
target = ll.head
connection = ll.head
while connection.next:
    connection = connection.next
connection.next = target
print(detect_cycle(ll.head))

ll = LinkedList()
ll.create_linked_list([1,2,3,4,5])
print(detect_cycle(ll.head))

ll = LinkedList()
ll.create_linked_list([0,2,3,5,6])
target = ll.head
while target.data != 5:
    target = target.next
connection = ll.head
while connection.next:
    connection = connection.next
connection.next = target
print(detect_cycle(ll.head))

ll = LinkedList()
ll.create_linked_list([3,6,9,10,11])
target = ll.head
while target.data != 6:
    target = target.next
connection = ll.head
while connection.next:
    connection = connection.next
connection.next = target
print(detect_cycle(ll.head))

def detect_cycle(head):
    fast, slow, pos = head.next, head, 0
    while fast and slow != fast:
        slow = slow.next
        pos += 1
        fast = fast.next
        if fast:
            fast = fast.next
    if not fast:
        return -1
    vals = set()
    while slow.data not in vals:
        vals.add(slow.data)
        slow = slow.next
    target = head
    position = 0
    while target.data not in vals:
        target = target.next
        position += 1
    return position