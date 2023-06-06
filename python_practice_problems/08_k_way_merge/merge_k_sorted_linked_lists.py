#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:24:14 2023

@author: johnmorgan
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode

# Time O(nlogk), k is number of lists, n is max list length
# Space O(1)

def merge_k_lists(lists):
    while len(lists) > 1:
        new_list = LinkedList()
        node1 = lists[0].head
        node2 = lists[1].head
        curr = new_list.head
        while node1 is not None or node2 is not None:
            if node1 is None:
                target = node2
                node2 = node2.next
            elif node2 is None:
                target = node1
                node1 = node1.next
            elif node1.data < node2.data:
                target = node1
                node1 = node1.next 
            else:
                target = node2
                node2 = node2.next
            if curr is None:
                new_list.head = target
                curr = target
            else:
                curr.next = target
                curr = curr.next
        lists.pop(0)
        lists.pop(0)
        lists.append(new_list)
    return lists[0].head
    
    
ll1 = LinkedList()
ll1.create_linked_list([2])
ll2 = LinkedList()
ll2.create_linked_list([1,2,4])
ll3 = LinkedList()
ll3.create_linked_list([25,56,66,72])
node = merge_k_lists([ll1, ll2, ll3])
while node is not None:
    print(node.data)
    node = node.next