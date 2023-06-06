#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:10:44 2023

@author: johnmorgan
"""

from binary_tree_node import BinaryTreeNode
from binary_tree import BinaryTree

With array indices, fun stuff, too bad the solution assumed actual nodes

def sub_recur_index(root, sub_root, main_index, sub_index):
    if main_index > len(root) - 1 and sub_index > len(sub_root) - 1:
        return True
    elif main_index > len(root) - 1 or sub_index > len(sub_root) - 1:
        return False
    if root[main_index] != sub_root[sub_index]:
        return False
    else:
        m1 = sub_recur_index(root, sub_root, 2 * main_index + 1, 2 * sub_index + 1)
        m2 = sub_recur_index(root, sub_root, 2 * main_index + 1, 2 * sub_index + 1)
    return m1 and m2

def subtree_index(root, sub_root):
    for index, node in enumerate(root):
        if node == sub_root[0]:
            main_index = index
            sub_index = 0
            test = sub_recur_index(root, sub_root, main_index, sub_index)
            if test == True:
                return True
    return False

root = [1,5,10,3,6]
sub_root = [5,3,6]
print(subtree_index(root, sub_root))
sub_root = [1,5,10]
print(subtree_index(root, sub_root))
sub_root = [20,3,6]
print(subtree_index(root, sub_root))

# With binary tree setup

def sub_recur(root, sub_root):
    if root is None and sub_root is None:
        return True
    if root is None and sub_root is not None:
        return False
    if root is not None and sub_root is None:
        return False
    if root.data != sub_root.data:
        return False
    else:
        left = sub_recur(root.left, sub_root.left)
        right = sub_recur(root.right, sub_root.right)
    return left and right

def subtree(node, sub_node):
    if node is None:
        return False
    if node.data == sub_node.data:
        match = sub_recur(node, sub_node)
        if match:
            return True
    else:
        left, right = False, False
        if node.left and sub_node.left:
            left = subtree(node.left, sub_node)
        if node.right and sub_node.right:
            right = subtree(node.left, sub_node)
        return left or right
    return False

main = [5,3,6,1,4]
sub = [3,1,4]
main_tree = BinaryTree(main)
sub_tree = BinaryTree(sub)
print(subtree(main_tree.root, sub_tree.root))
sub = [3,2,4]
sub_tree = BinaryTree(sub)
print(subtree(main_tree.root, sub_tree.root))
sub = [20,30,50]
sub_tree = BinaryTree(sub)
print(subtree(main_tree.root, sub_tree.root))
sub = [3,1,2,4]
sub_tree = BinaryTree(sub)
print(subtree(main_tree.root, sub_tree.root))