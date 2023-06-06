#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:09:55 2023

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

class NestedIterator:
    def __init__(self, nested_list):
        self.nested_list_stack = list(reversed(nested_list))

    def has_next(self):
        while len(self.nested_list_stack) > 0:
            top = self.nested_list_stack[-1]
            if top.is_integer():
                return True
            top_list = self.nested_list_stack.pop().get_list()
            i = len(top_list) - 1
            while i >= 0:
                self.nested_list_stack.append(top_list[i])
                i -= 1
        return False

    def next(self):
        if self.has_next():
            return self.nested_list_stack.pop().get_integer()
        return None


nums = [1,2,[3,[4,5,6],[7,8],9],10]
ni = NestedIterator(nums)
print(ni.has_next())
print(ni.next())
print(ni.has_next())
print(ni.next())
for _ in range(7):
    ni.next()
print(ni.has_next())
print(ni.next())
print(ni.has_next())