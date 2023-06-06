#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:10:37 2023

@author: johnmorgan
"""

def get_item():
    try:
        yield 5

    except GeneratorExit:
        print("GeneratorExit exception raised")


if __name__ == "__main__":
    gen = get_item()

    print(next(gen))
    print("Main exiting")