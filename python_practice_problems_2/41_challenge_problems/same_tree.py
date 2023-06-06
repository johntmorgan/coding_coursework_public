#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:00:24 2023

@author: johnmorgan
"""

from binary_tree import *
from collections import deque

def same_tree(p, q):
    if p == None and q == None:
        return True
    if p == None or q == None:
        return False
    if p.data != q.data:
        return False
    else:
        left = same_tree(p.left, q.left)
        right = same_tree(p.right, q.right)
    return left and right

# BFS pattern - not req'd, but was supposed to be a review

def same_tree(p, q):
    p_queue, q_queue = [], []
    if p == None and q == None:
        return True
    elif p == None or q == None:
        return False
    elif p.data != q.data:
        return False
    else:
        p_queue.append(p)
        q_queue.append(q)
        while p_queue or q_queue:
            if not p_queue:
                return False
            if not q_queue:
                return False
            p_node, q_node = p_queue.pop(0), q_queue.pop(0)
            if p_node.data != q_node.data:
                return False
            else:
                if p_node.left:
                    p_queue.append(p_node.left)
                if q_node.left:
                    q_queue.append(q_node.left)
                if p_node.right:
                    p_queue.append(p_node.right)
                if q_node.right:
                    q_queue.append(q_node.right)
    return True

# deque review

def same_tree(p, q):
    p_queue, q_queue = deque(), deque()
    if p == None and q == None:
        return True
    elif p == None or q == None:
        return False
    elif p.data != q.data:
        return False
    else:
        p_queue.append(p)
        q_queue.append(q)
        while p_queue or q_queue:
            if not p_queue:
                return False
            if not q_queue:
                return False
            p_node, q_node = p_queue.popleft(), q_queue.popleft()
            if p_node.data != q_node.data:
                return False
            else:
                if p_node.left:
                    p_queue.append(p_node.left)
                if q_node.left:
                    q_queue.append(q_node.left)
                if p_node.right:
                    p_queue.append(p_node.right)
                if q_node.right:
                    q_queue.append(q_node.right)
    return True

arr = [9,7,20,3,15]
bt = BinaryTree()
for num in arr:
    bt.insert(num)
arr2 = [9,7,20,3,15]
bt2 = BinaryTree()
for num in arr2:
    bt2.insert(num)
print(same_tree(bt.root, bt2.root))