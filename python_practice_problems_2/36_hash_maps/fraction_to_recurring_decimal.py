#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 14:34:18 2023

@author: johnmorgan
"""

# O(|d|) complexity, where d is the denominator - may have at most |d| different remainders
# O(|d|) space complexity - can have to store all those remainders


def fraction_to_decimal(numerator, denominator):
    result = ""
    if numerator == 0:
        return "0"
    if denominator == 0:
        return "inf"
    # ^ for xor - JM
    if numerator < 0 and denominator > 0 or (numerator > 0 and denominator < 0):
        result += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
    quotient = numerator / denominator
    remainder = (numerator % denominator) * 10
    result += str(int(quotient))
    if remainder == 0:
        return result
    else:
        hmap = {}
        result += "."
        while remainder != 0:
            if remainder in hmap.keys():
                beginning = hmap[remainder]
                left = result[0:beginning]
                right = result[beginning:len(result)]
                result = left + "(" + right + ")"
                return result
            hmap[remainder] = len(result)
            quotient = remainder / denominator
            result += str(int(quotient))
            remainder = (remainder % denominator) * 10
        return result

print(fraction_to_decimal(2, 4))
print(fraction_to_decimal(4, 2))
print(fraction_to_decimal(5, 333))