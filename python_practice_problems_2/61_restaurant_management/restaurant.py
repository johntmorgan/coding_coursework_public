#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:38:17 2023

@author: johnmorgan
"""

from enum import Enum

# Enumerations
class PaymentStatus(Enum):
  Unpaid = 1
  Pending = 2
  Completed = 3
  Failed = 4
  Declined = 5
  Canceled = 6
  Abandoned = 7
  Settling = 8
  Refunded = 9

class TableStatus(Enum):
  Free = 1
  Reserved = 2
  Occupied = 3
  Other = 4

class SeatType(Enum):
  Regular = 1
  Kid = 2
  Accessible = 3
  Other = 4

class AccountSatus(Enum):
  Active = 1
  Closed = 2
  Canceled = 3
  Blacklisted = 4

class OrderStatus(Enum):
  Received = 1
  Preparing = 2
  Complete = 3
  Canceled = 4
  NoStatus = 5

class ReservationStatus(Enum):
  Requested = 1
  Pending = 2
  Confirmed = 3
  CheckedIn = 4
  Canceled = 5
  Abandoned = 6
  
from abc import ABC, abstractmethod
class Account:
  def __init__(self, account_id, password, address, status):
    self.__account_id = account_id
    self.__password = password
    self.__address = address
    self.__status = status # Refers to the AccountStatus enum

  def reset_password(self):
    pass 

class Person(ABC):
  def __init__(self, name, email, phone_number):
    self.__name = name
    self.__email = email
    self.__phone_number = phone_number

class Customer(Person):
  def __init__(self, name, email, phone_number, last_visited_date):
    super().__init__(name, email, phone_number)
    self.__last_visited_date = last_visited_date

class Employee(Person):
  def __init__(self, name, email, phone_number, employee_id, joining_date):
    super().__init__(name, email, phone_number)
    self.__employee_id = employee_id
    self.__joining_date = joining_date

class Chef(Employee):
  def prepare_order():
    pass

class Waiter(Employee):
  def take_order():
    pass

class Manager(Employee):
  def add_employee():
    pass

class Receptionist(Employee):
  def create_reservation():
    pass

class Table:
  def __init__(self, table_id, status, max_capacity, location_identifier,
               seats):
    self.__table_id = table_id
    self.__status = status
    self.__max_capacity = max_capacity
    self.__location_identifier = location_identifier
    self.__seats = []

  def is_table_free(self):
    pass
  
  def add_reservation(self):
    pass
  
  def search(self, capacity, start_time):
    pass
    
class TableSeat:
  def __init__(self, table_seat_number, seat_type):
    self.__table_seat_number = table_seat_number
    self.__seat_type = seat_type
  
  def update_seat_type(self, typee):
    pass

class MealItem:
  def __init__(self, meal_item_id, quantity, menu_item):
    self.__meal_item_id = meal_item_id
    self.__quantity = quantity
    self.__menu_item = menu_item

  def update_quantity(self, quantity):
    pass

class Meal:
  def __init__(self, meal_id, seat, menu_items):
    self.__meal_id = meal_id
    self.__seat = seat
    self.__menu_items = []

  def add_meal_item(self, meal_item):
    pass

class Menu:
  def __init__(self, menu_id, title, description, price, menu_sections):
    self.__menu_id = menu_id
    self.__title = title
    self.__description = description
    self.__price = price
    self.__menu_sections = []

  def add_menu_section(self, menu_section):
    pass

  def print():
    pass

class MenuSection:
  def __init__(self, menu_section_id, title, description, menu_items):
    self.__menu_section_id = menu_section_id
    self.__title = title
    self.__description = description
    self.__menu_items = []

  def add_menu_item(menu_item):
    pass

class MenuItem:
  def __init__(self, menu_item_id, title, description, price):
    self.__menu_item_id = menu_item_id
    self.__title = title
    self.__description = description
    self.__price = price

  def update_price(price):
    pass

class Order:
  def __init__(self, order_id, status, creation_time, meals, table, waiter,
               chef):
    self.__order_id = order_id
    self.__status = status
    self.__creation_time = creation_time
    self.__meals = []
    self.__table = table
    self.__waiter = waiter
    self.__chef = chef

  def add_meal(self, meal):
    None

  def remove_meal(self, meal):
    None

class Kitchen:
    def __init__(self, name):
        self.__name = name
        self.__chefs = []

    def assign_chef(self, chef):
        None

import datetime

class Reservation:
    def __init__(self, res_id, people_count, notes, customer):
        self.__reservation_id = res_id
        self.__time_of_reservation = datetime.datetime.now()
        self.__people_count = people_count
        self.__status = ReservationStatus.REQUESTED
        self.__notes = notes
        self.__checkin_time = None
        self.__customer = customer
        self.__tables = []
        self.__notifications = []

    def update_people_count(self, count):
        None

class Payment(ABC):
    def __init__(self, payment_id, creation_date, amount, status):
        self.payment_id = payment_id
        self.creation_date = creation_date
        self.amount = amount
        self.status = status

    @abstractmethod
    def initiate_transaction():
        pass

class Check(Payment):
    def __init__(self, payment_id, creation_date, amount, status, bank_name,
                 check_number):
        super().__init__(payment_id, creation_date, amount, status)
        self.bank_name = bank_name
        self.check_number = check_number

    def initiate_transaction():
        pass

class CreditCard(Payment):
    def __init__(self, payment_id, creation_date, amount, status,
                 name_on_card, zip_code):
        super().__init__(payment_id, creation_date, amount, status)
        self.__name_on_card = name_on_card
        self.__zip_code = zip_code

    def initiate_transaction():
        pass

class Cash(Payment):
    def __init__(self, payment_id, creation_date, amount, status,
                 cash_tendered):
        super().__init__(payment_id, creation_date, amount, status)
        self.__cash_tendered = cash_tendered

    def initiate_transaction():
        pass

class Bill:
    def __init__(self, bill_id, amount, tip, tax, is_paid):
        self.__bill_id = bill_id
        self.__amount = amount
        self.__tip = tip
        self.__tax = tax
        self.__is_paid = is_paid

    def generate_bill():
        pass
    
class Notification(ABC):
    def __init__(self, notification_id, created_on, content):
        self.notification_id = notification_id
        self.created_on = created_on
        self.content = content

    # account here refers to an instance of the Account class 
    @abstractmethod
    def send(person):
        pass

class SmsNotification(Notification):
    def __init__(self, phone, notification_id, created_on, content):
        self.phone = phone
        super().__init__(notification_id, created_on, content)

    # account here refers to an instance of the Account class 
    def send(person):
        # functionality 
        pass

class EmailNotification(Notification):
    def __init__(self, email, notification_id, created_on, content):
        self.email = email
        super().__init__(notification_id, created_on, content)

    # account here refers to an instance of the Account class 
    def send(person):
        # functionality 
        pass
    
class SeatingChart:
    def __init__(self, id):
        self.__seating_chart_id = id
        self.__seating_chart_image = []

    def print(self):
        pass

class Branch:
    def __init__(self, name, location, kitchen, menu):
        self.name = name
        self.location = location
        self.kitchen = kitchen
        self.menu = menu

    def add_seating_chart(self):
        pass

class Restaurant:
    def __init__(self, name):
        self.__name = name
        self.__branches = []

    def add_branch(self, branch):
        pass