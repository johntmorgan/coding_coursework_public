#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:51:18 2023

@author: johnmorgan
"""

def generate_numbers():
    i = 0

    while True:
        i += 1
        k = (yield i)
        print(k)


if __name__ == "__main__":
    generator = generate_numbers()

    item = generator.send(None)
    print("received " + str(item))

    for i in range(0, 5):
        item = generator.send(55 + i)
        print("received " + str(item))
