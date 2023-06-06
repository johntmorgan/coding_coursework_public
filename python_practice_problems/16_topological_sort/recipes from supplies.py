#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:23:16 2023

@author: johnmorgan
"""

def prepro_find_recipes(recipes, ingredients, supplies):
    graph = {}
    for index, ing_list in enumerate(ingredients):
        for ingredient in ing_list:
            if ingredient not in graph:
                graph[ingredient] = []
            graph[ingredient].append(recipes[index])
    indegrees = {}
    for node in graph:
        for child in graph[node]:
            if child not in indegrees:
                indegrees[child] = 1
            else:
                indegrees[child] += 1
    valid_recipes = []
    while supplies:
        supply = supplies.pop()
        for index, ing_list in enumerate(ingredients):
            if supply in ing_list:
                indegrees[recipes[index]] -= 1
            if indegrees[recipes[index]] == 0:
                valid_recipes.append(recipes[index])
                supplies.append(recipes[index])
                indegrees[recipes[index]] -= 1
    valid_recipes.sort()
    return valid_recipes


    
    

recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
print(prepro_find_recipes(recipes, ingredients, supplies))

# def prepro_find_recipes(recipes, ingredients, supplies):
#     ing_req = {}
#     for index in range(len(recipes)):
#         ing_req[recipes[index]] = len(ingredients[index])
#     valid_recipes = []
#     while supplies:
#         supply = supplies.pop(0)
#         for index in range(len(ingredients)):
#             if supply in ingredients[index]:
#                 ing_req[recipes[index]] -= 1
#             if ing_req[recipes[index]] == 0:
#                 supplies.append(recipes[index])
#                 valid_recipes.append(recipes[index])
#                 ing_req[recipes[index]] -= 1
#     valid_recipes.sort()
#     return valid_recipes