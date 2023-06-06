#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:46:47 2023

@author: johnmorgan
"""

def keep_learning_asynchronous():
    yield "Educative"

if __name__ == "__main__":
    gen = keep_learning_asynchronous()
    str = next(gen)
    print(str)
    
def keep_learning_asynchronous_2():
    yield "Educative"
    yield "Educative 2"

if __name__ == "__main__":
    gen = keep_learning_asynchronous_2()
    for item in gen:
        print(item)