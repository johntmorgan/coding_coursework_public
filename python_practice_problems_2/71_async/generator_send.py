#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:14:47 2023

@author: johnmorgan
"""

def generator_function():
    while True:
        item = yield
        print("received " + str(item))


if __name__ == "__main__":
    gen = generator_function()
    next(gen)
    gen.send(37)


# Produces error
# Nothing returned

def generator_function():
    item = yield
    print("received " + str(item))


if __name__ == "__main__":
    gen = generator_function()
    next(gen)
    gen.send(37)