#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:54:47 2023

@author: johnmorgan
"""

def pascal_recurse(target, depth, prior_row):
    if target == depth:
        return prior_row
    curr_row = [None] * (len(prior_row) + 1)
    for index in range(len(curr_row)):
        if index == 0 or index == len(curr_row) - 1:
            curr_row[index] = 1
        else:
            curr_row[index] = prior_row[index - 1] + prior_row[index]
    return pascal_recurse(target, depth + 1, curr_row)


def printPascal(var1) :
  return pascal_recurse(var1, 0, [1])

# Course solution

def printPascal(testVariable) :
    # Base Case
    if testVariable == 0 :
        return [1]
    else :
        line = [1]
        previousLine = printPascal(testVariable - 1)
        for i in range(len(previousLine) - 1):
            line.append(previousLine[i] + previousLine[i + 1])
        line += [1]
    return line


var1 = 5
print(printPascal(var1))