#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:33:05 2023

@author: johnmorgan
"""

# JM long way of doing it

# def balanced(testVariable, startIndex = 0, currentIndex = 0, interior = False):
#     counter = 0
#     end_pair = False
#     while not end_pair and currentIndex < len(testVariable):
#         if testVariable[currentIndex] == "(":
#             counter += 1
#         elif testVariable[currentIndex] == ")":
#             counter -= 1
#         if counter == 0:
#             end_pair = True
#         elif counter < 0:
#             return False
#         else:
#             currentIndex += 1
#     if currentIndex == len(testVariable):
#         return False
#     if startIndex == currentIndex - 1:
#         interior_ok = True
#     else:
#         interior_ok = balanced(testVariable, startIndex + 1, startIndex + 1, True)
#     if currentIndex == len(testVariable) - 1 or interior == True:
#         end_ok = True
#     else:
#         end_ok = balanced(testVariable, currentIndex + 1, currentIndex + 1, False)
#     return interior_ok and end_ok

# Simple course solution
# Review

def balanced(testVariable, startIndex = 0, currentIndex = 0):
    # If have reached end, are all paired?
    if startIndex == len(testVariable):
        return currentIndex == 0
    # Unpaired opening bracket          
    if currentIndex < 0:
        return False
    if testVariable[startIndex] == "(":
        return balanced(testVariable, startIndex + 1, currentIndex + 1)
    elif testVariable[startIndex] == ")" : 
        return balanced(testVariable, startIndex + 1, currentIndex - 1)
        
testVariable = ["(", ")", "(", ")"]
print(balanced(testVariable, 0, 0))

testVariable = ["(", "(", ")", ")"]
print(balanced(testVariable, 0, 0))

testVariable = ["(", "(", "(", ")", ")", ")", "(", "(", "(", ")", ")", ")"]
print(balanced(testVariable, 0, 0))

testVariable = ["(", "(", "(", ")", ")", ")", "(", "(", "(", "(", ")", ")"]
print(balanced(testVariable, 0, 0))

testVariable = ['(', '(', ')', ')', '(', ')']
print(balanced(testVariable, 0, 0))

testVariable = [')', '(']
print(balanced(testVariable, 0, 0))
