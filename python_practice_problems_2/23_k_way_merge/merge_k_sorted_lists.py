#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 14:36:31 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode

# Tip: You may use some of the code templates provided
# in the support files

# O(nlogk) where k is the number of lists

def merge_k_lists(lists):
    while len(lists) > 1:
        ll = LinkedList()
        p1 = lists[0].head
        p2 = lists[1].head
        curr = None
        while p1 is not None or p2 is not None:
            if p1 is None:
                new_node = LinkedListNode(p2.data)
                p2 = p2.next
            elif p2 is None:
                new_node = LinkedListNode(p1.data)
                p1 = p1.next
            else:
                if p1.data < p2.data:
                    new_node = LinkedListNode(p1.data)
                    p1 = p1.next
                else:
                    new_node = LinkedListNode(p2.data)
                    p2 = p2.next
            if ll.head:
                curr.next = new_node
                curr = curr.next
            else:
                ll.head = new_node
                curr = ll.head
        lists.pop(0)
        lists.pop(0)
        lists.append(ll)
    return lists[0].head       
    

ll1 = LinkedList()
ll1.create_linked_list([11,41,51])
ll2 = LinkedList()
ll2.create_linked_list([21,23,42])
curr = merge_k_lists([ll1, ll2])
while curr is not None:
    print(curr.data)
    curr = curr.next
    
[[2], [1, 2, 4], [25, 56, 66, 72]]

ll1 = LinkedList()
ll1.create_linked_list([2])
ll2 = LinkedList()
ll2.create_linked_list([1,2,4])
ll3 = LinkedList()
ll3.create_linked_list([25,56,66,72])
curr = merge_k_lists([ll1, ll2, ll3])
while curr is not None:
    print(curr.data)
    curr = curr.next