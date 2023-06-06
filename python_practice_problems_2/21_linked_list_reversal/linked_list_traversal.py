#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:22:59 2023

@author: johnmorgan
"""

def traverse_linked_list(head):
    current, nxt = head, None
    while current:
      nxt = current.next
      current = nxt