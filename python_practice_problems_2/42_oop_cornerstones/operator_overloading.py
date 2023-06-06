#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:58:40 2023

@author: johnmorgan
"""

# Overloading add function called by + operator
# Java and JS do NOT support operator overloading

class ComplexNumber: 
    # Constructor
    def __init__(self): 
        self.real = 0 
        self.imaginary = 0 
    # Set value function
    def set_value(self, real, imaginary): 
        self.real = real
        self.imaginary = imaginary 
    # Overloading function for + operator
    def __add__(self, c): 
        result = ComplexNumber() 
        result.real = self.real + c.real 
        result.imaginary = self.imaginary + c.imaginary 
        return result 
    # display results
    def display(self): 
        print( "(", self.real, "+", self.imaginary, "i)") 
 
 
c1 = ComplexNumber() 
c1.set_value(11, 5) 
c2 = ComplexNumber() 
c2.set_value(2, 6) 
c3 = ComplexNumber()
c3 = c1 + c2
c3.display() 