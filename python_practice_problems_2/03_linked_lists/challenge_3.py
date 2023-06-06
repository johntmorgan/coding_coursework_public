#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:32:42 2023

@author: johnmorgan
"""

from Node import Node
from LinkedListDBV import LinkedList

# O(n) complexity, worst case search to end of list

def delete(lst, value):
    if lst.is_empty():
        print("List is Empty")
        return False
    temp = lst.head_node
    prior_temp = None
    while(temp is not None):
        if(temp.data is value):
            if temp == lst.head_node:
                lst.delete_at_head()
            else:
                prior_temp.next_element = temp.next_element
            return True
        prior_temp = temp
        temp = temp.next_element
    return False    
    

lst = LinkedList()

for i in range(11):
    lst.insert_at_head(i)

lst.print_list()

delete(lst, 7)
lst.print_list()

delete(lst, 3)
lst.print_list()

delete(lst, 0)
lst.print_list()

delete(lst, 10)
lst.print_list()

delete(lst, 12)
lst.print_list()

