#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:35:32 2023

@author: johnmorgan
"""

# Review this

def fraction_to_decimal(num, denom):
    if num == 0:
        return "0"
    if denom == 0:
        return "inf"
    result = ""
    if num * denom < 0:
        result += "-"
        num = abs(num)
        denom = abs(denom)
    quotient = num / denom
    remainder = (num % denom) * 10
    result += str(int(quotient))
    if remainder == 0:
        return result
    else:
        hmap = {}
        result += "."
        while remainder != 0:
            if remainder in hmap:
                beginning = hmap[remainder]
                left = result[0:beginning]
                right = result[beginning:len(result)]
                result = left + "(" + right + ")"
                return result
            hmap[remainder] = len(result)
            quotient = remainder / denom
            result += (str(int(quotient)))
            remainder = (remainder % denom) * 10
        return result

numerator = 5
denominator = 333
print(fraction_to_decimal(numerator, denominator))

numerator = -5
denominator = 333
print(fraction_to_decimal(numerator, denominator))