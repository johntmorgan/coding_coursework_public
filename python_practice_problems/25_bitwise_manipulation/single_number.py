#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:41:53 2023

@author: johnmorgan
"""

def single_number(nums):
    result = 0
    for num in nums:
        result = result ^ num
    return result