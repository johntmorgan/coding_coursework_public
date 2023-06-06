#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:33:04 2023

@author: johnmorgan
"""


def createStack() : # Function to create an empty stack
  stack = []
  return stack 

def isEmpty(stack) :
  return len(stack) == 0

def push(stack, item) : # push item to stack
  stack.append( item ) 

def pop(stack) : # pop item from stack

  if(isEmpty(stack)) : # display error if stack empty  
    print("Stack Underflow ")
    exit(1)

  return stack.pop() 