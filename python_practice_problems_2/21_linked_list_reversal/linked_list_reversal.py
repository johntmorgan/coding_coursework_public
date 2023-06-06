#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:23:08 2023

@author: johnmorgan
"""

def reverse_linked_list(head):
	prev, curr = None, head
	while curr:
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt
	return prev
