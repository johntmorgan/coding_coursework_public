#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:51:38 2023

@author: johnmorgan
"""

from Node1 import Node
from BST1 import BinarySearchTree
from BSTDisplay import *

def findKthMax(root, k):
    if root is None:
        return None
    curr_node = root
    visited = []
    node_count = 0
    while node_count < k:
        while curr_node.rightChild and curr_node.rightChild.val not in visited:
            curr_node = curr_node.rightChild
        if curr_node.val not in visited:
            visited += [curr_node.val]
            node_count += 1
        elif curr_node.leftChild and curr_node.leftChild.val not in visited:
            curr_node = curr_node.leftChild
        else:
            curr_node = root
    return curr_node.val

# Can also do an in-order traversal to create an array
# O(n), always traverses entire tree no matter what k is

# def findKthMax(root, k):
#     tree = []
#     inOrderTraverse(root, tree)  # Get sorted tree list
#     if ((len(tree)-k) >= 0) and (k > 0):  # check if k is valid
#         return tree[-k]  # return the kth max value
#     return None  # return none if no value found

# def inOrderTraverse(node, tree):
#     # Helper recursive function to traverse the tree inorder
#     if node is not None:  # check if node exists
#         inOrderTraverse(node.leftChild, tree)  # traverse left sub-tree
#         if len(tree) is 0:
#             # Append if empty tree
#             tree.append(node.val)
#         elif tree[-1] is not node.val:
#             # Ensure not a duplicate
#             tree.append(node.val)  # add current node value
#         inOrderTraverse(node.rightChild, tree)

# Recursive solution
# Worst-case still O(n)
# But best case O(log(n)), when k = 1

# def findKthMax(root, k):
#     if k < 1:
#         return None
#     node = findKthMaxRecursive(root, k)  # get the node at kth position
#     if(node is not None):  # check if node received
#         return node.val  # return kth node value
#     return None  # return None if no node found


# counter = 0  # global count variable
# current_max = None

# def findKthMaxRecursive(root, k):
#     global counter  # use global counter to track k
#     global current_max # track current max
#     if(root is None):  # check if root exists
#         return None

#     # recurse to right for max node
#     node = findKthMaxRecursive(root.rightChild, k)
#     if(counter is not k) and (root.val is not current_max):
#         # Increment counter if kth element is not found
#         counter += 1
#         current_max = root.val
#         node = root
#     elif current_max is None:
#         # Increment counter if kth element is not found
#         # and there is no current_max set
#         counter += 1
#         current_max = root.val
#         node = root
#     # Base condition reached as kth largest is found
#     if(counter == k):
#         return node  # return kth node
#     else:
#         # Traverse left child if kth element is not reached
#         # traverse left tree for kth node
#         return findKthMaxRecursive(root.leftChild, k)

BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(2)
BST.insert(5)
BST.insert(8)
BST.insert(12)
BST.insert(10)
BST.insert(14)
# display(BST.root)
print(findKthMax(BST.root, 8))