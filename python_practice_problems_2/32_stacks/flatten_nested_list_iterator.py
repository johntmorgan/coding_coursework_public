#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:50:24 2023

@author: johnmorgan
"""

from nested_integers import NestedIntegers

class NestedIterator:
    # Initializes the NestedIterator with nlist
    def __init__(self, nlist):
        self.stack = []
        self.fixed_list = []
        if isinstance(nlist, list):
            for elem in nlist:
                self.fixed_list.append(elem)
        else:
            for elem in nlist.integer:
                self.fixed_list.append(elem)
        self.recurse_pop(self.fixed_list, self.stack)
        
    def recurse_pop(self, fixed_list, stack):
        if isinstance(fixed_list, int):
            stack.append(fixed_list)
            return
        elif len(fixed_list) == 0:
            return
        else:
            while len(fixed_list) > 0:
                last_elem = fixed_list.pop()
                self.recurse_pop(last_elem, stack)
                self.recurse_pop(fixed_list, stack)
                
    # checks if there are still some integers in nlist
    def has_next(self):
        return len(self.stack) > 0

    # returns the next element from nlist
    def next(self):
        return self.stack.pop()


# Course solution
# O(n + l) - n number of element, l number of nested lists
# Actually breaks on my machine - meh, moving on here.

# class NestedIterator:
#     def __init__(self, nested_list):
#         self.nested_list_stack = list(reversed(nested_list))
#     def has_next(self):
#         # Iterate in the stack while the stack is not empty
#         while len(self.nested_list_stack) > 0: 
#             # Save the top value of the stack
#             top = self.nested_list_stack[-1]
#             # Check if the top value is integer, if true return True, 
#             # if not continue
#             if top.is_integer():
#                 return True
#             # If the top is not an integer, it must be the list of integers
#             # Pop the list from the stack and save it in the top_list
#             top_list = self.nested_list_stack.pop().get_list()
#             # Save the length of the top_list in i and iterate in the list
#             i = len(top_list) - 1
#             while i >= 0:
#                 # Append the values of the nested list into the stack
#                 self.nested_list_stack.append(top_list[i])
#                 i -= 1
#         return False

#     # next will return the integer from the nested_list 
#     def next(self): 
#         # Check if there is still an integer in the stack
#         if self.has_next():
#             # If true pop and return the top of the stack
#             return self.nested_list_stack.pop().get_integer()
#         return None


# ------ Please don't change the following function ----------
# flatten_list function is used for testing porpuses.
# Your code will be tested using this function
def flatten_list(nested_iterator_object):
    result = []
    while nested_iterator_object.has_next():
        result.append(nested_iterator_object.next()) 
    return result

n = NestedIntegers([1,2,[3,[4,5,6],[7,8],9],10])
print(n.integer)
ni = NestedIterator(n)
print(ni.has_next())
print(ni.next())
# print(ni.next())
# print(ni.has_next())
# print(ni.next())
