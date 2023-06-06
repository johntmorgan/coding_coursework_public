#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:29:33 2023

@author: johnmorgan
"""

# Enumerations
class ProductType(Enum):
  CHOCOLATE = 1
  SNACK = 2
  BEVERAGE = 3
  OTHER = 4
  
from abc import ABC, abstractmethod

class State(ABC):
  def insert_money(self, machine, amount):
    pass

  def press_button(self, machine, rack_number):
    pass

  def return_change(self, amount):
    pass

  def update_inventory(self, machine, rack_number):
    pass

  def dispense_product(self, machine, rack_number):
    pass

class NoMoneyInsertedState(State):
  def __init__(self):
    None

  def insert_money(self, machine, amount):
    # changes state to MonenInsertedState
    pass

  def press_button(self, machine, rack_number):
    pass

  def return_change(self, amount):
    pass

  def update_inventory(self, machine, rack_number):
    pass

  def dispense_product(self, machine, rack_number):
    pass

class MoneyInsertedState(State):
  def __init__(self):
    None

  def insert_money(self, machine, amount):
    pass

  def press_button(self, machine, rack_number):
    # check if product item is available
    # validate money
    # change state to DispenseState 
    pass

  def return_change(self, amount):
    pass

  def update_inventory(self, machine, rack_number):
    pass

  def dispense_product(self, machine, rack_number):
    pass

class DispenseState(State):
  def __init__(self):
    None

  def insert_money(self, machine, amount):
    pass

  def press_button(self, machine, rack_number):
    pass

  def return_change(self, amount):
    pass

  def update_inventory(self, machine, rack_number):
    pass
    
  def dispense_product(self, machine, rack_number):
    # dispense product
    # change state to NoMoneyInsertedState
    pass

class Product:
    def __init__(self, name, id, price, type):
        self.__name = name
        self.__id = id
        self.__price = price
        self.__type = type # here type is an instance of ProductType 
        

class Rack:
    def __init__(self, product_id, rack_number):
        self.__product_id = product_id
        self.__rack_number = rack_number
  
    def is_empty():
        None


class Inventory:
    def __init__(self, no_of_products, products):
        self.__no_of_products = no_of_products
        self.__products = products   
  
    def add_product(product_id, rack_id):
        None
    
    def remove_product(product_id, rack_id):
        None

# The __VendingMachine is a singleton class that ensures it will have only one active instance at a time
class __VendingMachine(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__VendingMachine, cls).__new__(cls)
    return cls.__instances

class VendingMachine(metaclass=__VendingMachine):

  def __init__(self, current_state, amount, no_of_racks, racks, available_racks):
    self.__current_state = current_state
    self.__amount = amount
    self.__no_of_racks = no_of_racks
    self.__racks = racks
    self.__available_racks = available_racks

  def insert_money(self, amount):
    pass

  def press_button(self, rack_number):
    pass

  def return_change(self, amount):
    pass

  def update_inventory(self, rack_number):
    pass

  def dispense_product(self, rack_number):
    pass

  def get_product_id_at_rack(self, rack_number):
    pass