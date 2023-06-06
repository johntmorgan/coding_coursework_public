#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:55:46 2023

@author: johnmorgan
"""

def is_prime(i):
    if i == 1 or i == 2 or i == 3:
        return True

    k = 2

    while k <= i / 2:
        if i % k == 0:
            return False
        k += 1

    return True


def get_primes():
    i = 1
    while True:
        if is_prime(i):
            yield i
        i += 1


if __name__ == "__main__":
    gen = get_primes()

    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
