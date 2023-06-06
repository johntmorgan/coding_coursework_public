#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:56:07 2023

@author: johnmorgan
"""

class Animal:
  def __init__(self):
    pass
  
  def print_animal(self):
    print("I am from the Animal class")

  def print_animal_two(self):
    print("I am from the Animal class")


class Lion(Animal):
  def __init__(self):
    super();

  def print_animal(self): # method overriding
    print("I am from the Lion class")


lion = Lion()
lion.print_animal()
lion.print_animal_two()