#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:08:07 2023

@author: johnmorgan
"""

def same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None and q is not None:
        return False
    if p is not None and q is None:
        return False
    if p.data != q.data:
        return False
    else:
        left = same_tree(p.left, q.left)
        right = same_tree(p.right, q.right)
    return left and right