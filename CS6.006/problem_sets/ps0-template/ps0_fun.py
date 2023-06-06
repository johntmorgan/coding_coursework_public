#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:23:22 2022

@author: johnmorgan
"""

total = 0
for i in range(1,7):
    for j in range(1,7):
        total += i * j

print(total / 36 )