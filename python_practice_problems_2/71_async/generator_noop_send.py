#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:42:05 2023

@author: johnmorgan
"""

def generate_numbers():
    i = 0
    while True:
        i += 1
        yield i
        k = yield
        print("Received in generator function: " + str(k))


if __name__ == "__main__":
    generator = generate_numbers()
    
    # The first iteration happens outside the loop
    k = next(generator)
    print("Received in main function: " + str(k))


    for i in range(0, 11):
        # The noop operation required to move the generator
        # from the first yield to the second yield statement
        next(generator)

        # send will both pass in the value to the generator
        # function and also yield the next value from the
        # generator
        k = generator.send(i+50)
        print("Received in main function: " + str(k))