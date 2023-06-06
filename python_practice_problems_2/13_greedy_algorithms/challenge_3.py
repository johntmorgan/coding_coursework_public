#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:33:09 2023

@author: johnmorgan
"""

import math
from fractions import Fraction

def egyptian_fraction(numerator, denominator):
    curr = 2
    result = []
    while numerator > 0:
        if Fraction(numerator/denominator) >= Fraction(1/curr):
            numerator = numerator * curr - denominator
            denominator = denominator * curr
            result += [curr]
        curr += 1
    return result

# Course solution, using math.ceil
# O(logn) time complexity
# Review

def egyptian_fraction(numerator, denominator):
    """
    Finds the egyptian fraction denominators
    :param numerator: Numerator of the fraction
    :param denominator: Denominator of the fraction
    :return: A list of denominators of the egyptian fraction
    """
    lst_denominator = []
    while numerator != 0:
        x = math.ceil(denominator / numerator)
        lst_denominator.append(x)
        numerator = x * numerator - denominator
        denominator = denominator * x
    return lst_denominator

numerator = 2
denominator = 3
print(egyptian_fraction(numerator, denominator))