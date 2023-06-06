#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:07:49 2023

@author: johnmorgan
"""

# JM solution, wordy!

def dtb_recurse(var1, power, dtb_str):
    if power < 0:
        return dtb_str
    else:
        if 2**power <= var1:
            return dtb_recurse(var1 - 2**power, power - 1, dtb_str + "1" )
        else:
            return dtb_recurse(var1, power - 1, dtb_str + "0")

def decimalToBinary(var1):
    if var1 == 0:
        return "0"
    if var1 == 1:
        return "1"
    power = 0
    while 2**power <= var1:
        power += 1
    return dtb_recurse(var1, power - 1, "")

# Course solution
# Review, way more convenient

def decimalToBinary(testVariable) :
  if testVariable <= 1:
    return str(testVariable)
  else:
    return decimalToBinary(testVariable // 2) + decimalToBinary(testVariable % 2) # Floor division - 
      # division that results into whole number adjusted to the left in the number line

var1 = 11
print(decimalToBinary(var1))

var1 = 2
print(decimalToBinary(var1))

var1 = 0
print(decimalToBinary(var1))