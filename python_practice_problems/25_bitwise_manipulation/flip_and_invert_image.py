#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:55:20 2023

@author: johnmorgan
"""

# O(n^2)

def flip_and_invert_image(image):
    for r_index, row in enumerate(image):
        for c_index, col in enumerate(row):
            image[r_index][c_index] = image[r_index][c_index] ^ 1
        start = 0
        end = len(image[0]) - 1
        while start < end:
            image[r_index][start], image[r_index][end] = image[r_index][end], image[r_index][start]
            start += 1
            end -= 1
    return image