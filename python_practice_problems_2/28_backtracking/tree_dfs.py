#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:42:02 2023

@author: johnmorgan
"""

def dfs_tree(root):
    if root is None:
        return
    dfs_tree(root.left)
    dfs_tree(root.right)