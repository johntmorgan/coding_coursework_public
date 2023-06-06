#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:24:05 2023

@author: johnmorgan
"""

# Review, easy and super common question

def max_profit(stock_prices):
    low_price = float('inf')
    max_profit = 0
    for index, val in enumerate(stock_prices):
        if val < low_price:
            low_price = val
        elif val - low_price > max_profit:
            max_profit = val - low_price
    return max_profit

prices = [1,2,4,2,5,7,2,4,9,0,9]
print(max_profit(prices))
prices = [7,1,5,3,6,4]
print(max_profit(prices))
prices = [7,6,4,3,1]
print(max_profit(prices))
prices = [2,6,8,7,8,7,9,4,1,2,4,5,8]
print(max_profit(prices))
prices = [1,2]
print(max_profit(prices))