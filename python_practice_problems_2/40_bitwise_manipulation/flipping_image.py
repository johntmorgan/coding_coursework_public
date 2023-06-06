#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:29:38 2023

@author: johnmorgan
"""

# Review, though not bad already

# Naive
# O(n * n) flip, O(n * n) invert

# Bitwise
# Same time/space complexity but better hardware support = faster

def flip_and_invert_image(image):
    for row in image:
        row.reverse()
    for r_index, row in enumerate(image):
        for c_index, col in enumerate(image[0]):
            image[r_index][c_index] = image[r_index][c_index] ^ 1
    return image

# Course solution, better

def flip_and_invert_image(image):
    image = [i[::-1] for i in image]
    for i in range(len(image)):
        image[i] = [j ^ 1 for j in image[i]]
    return image

image = [[1,1,0],[1,0,1],[0,0,0]]
print(flip_and_invert_image(image))