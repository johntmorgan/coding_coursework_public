#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:14:08 2023

@author: johnmorgan
"""

def find_recipes(recipes, ingredients, supplies):
    rdict = {}
    for index in range(len(recipes)):
        rdict[recipes[index]] = len(ingredients[index])
    for supply in supplies:
        for index in range(len(ingredients)):
            if supply in ingredients[index]:
                rdict[recipes[index]] = rdict[recipes[index]] - 1
    prepped, good_recipes = [], []
    for key, val in rdict.items():
        if val == 0:
            prepped.append(key)
            good_recipes.append(key)
    while len(prepped) > 0:
        prep = prepped.pop(0)
        for index in range(len(ingredients)):
            if supply in ingredients[index]:
                if rdict[recipes[index]] == 1:
                    rdict[recipes[index]] = 0
                    prepped.append(recipes[index])
                    good_recipes.append(recipes[index])
                else:
                    rdict[recipes[index]] = rdict[recipes[index]] - 1      
    return good_recipes

recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
print(find_recipes(recipes, ingredients, supplies))