#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:58:40 2023

@author: johnmorgan
"""

# Naive sort array, O(nlogn) and O(n) or O(logn) space depending on language

# Cyclic sort

def find_duplicate(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] == nums[j]:
                return nums[i]
            else:
                nums[i], nums[j] = nums[j], nums[i]
    return 0

# Fast/slow, no swapping
# O(n) time, O(1) space
# Review

def find_duplicate(nums):
    # Initialize the fast and slow pointers and make them point the first
    # element of the array
    fast = slow = nums[0]
    # PART #1
    # Traverse in array until the intersection point is not found
    while True:
        # Move the slow pointer using the nums[slow] flow
        slow = nums[slow]
        # Move the fast pointer two times fast as the slow pointer using the 
        # nums[nums[fast]] flow 
        fast = nums[nums[fast]]
        # Break of the slow pointer becomes equal to the fast pointer, i.e., 
        # if the intersection is found
        if slow == fast:
            break
    # PART #2
    # Make the slow pointer point the starting position of an array again, i.e.,
    # start the slow pointer from starting position
    slow = nums[0]
    # Traverse in an array until the slow pointer does not become equal to the
    # fast pointer
    while slow != fast:
        # Move the slow pointer using the nums[slow] flow
        slow = nums[slow]
        # Move the fast pointer slower than before, i.e., move the fast pointer
        # using the nums[fast] flow
        fast = nums[fast]
    # Return the fast pointer as it points the duplicate number of the array
    return fast

nums = [3,4,4,4,2]
print(find_duplicate(nums))