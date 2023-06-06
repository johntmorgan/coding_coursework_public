#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:17:26 2023

@author: johnmorgan
"""

def max_profit(stock_prices):
    buy, sell = 0, 0
    max_profit = 0
    while sell < len(stock_prices):
        profit = stock_prices[sell] - stock_prices[buy]
        if profit > max_profit:
            max_profit = profit
        if stock_prices[sell] < stock_prices[buy]:
            buy = sell
        sell += 1
    return max_profit

prices = [1,2,4,2,5,7,2,4,9,0,9]
print(max_profit(prices))