#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:53:41 2023

@author: johnmorgan
"""

from enum import Enum
from abc import ABC, abstractmethod
import datetime

class OrderStatus(Enum):
  OPEN = 1
  FILLED = 2
  PARTIALLY_FILLED = 3
  CANCELED = 4


class TimeEnforcementType(Enum):
  GOOD_TILL_CANCELED = 1
  FILL_OR_KILL = 2
  IMMEDIATE_OR_CANCEL = 3
  ON_THE_OPEN = 4
  ON_THE_CLOSE = 5


class AccountStatus(Enum):
  ACTIVE = 1
  CLOSED = 2
  CANCELED = 3
  BLACKLISTED = 4
  NONE = 5


class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country
    
class Account(ABC):
  def __init__(self, id, password, name, address, email, phone):
    self.__id = id
    self.__password = password
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__status = AccountStatus.NONE

  @abstractmethod
  def reset_password(self):
    None

class Member(Account):
    def __init__(self):
        self.__available_funds_for_trading = 0.0
        self.__date_of_membership = datetime.date.today()
        self.__stock_positions = {}
        self.__active_orders = {}
    
    def place_sell_limit_order(self, stock_id, quantity, limit_price,
                               enforcement_type):
        pass

    def place_buy_limit_order(self, stock_id, quantity, limit_price,
                              enforcement_type):
        pass
    
    def callback_stock_exchange(self, order_id, order_parts, status):
        pass
  
    def reset_password(self):
        pass
        # functionality
    
class Admin(Account):
    def block_member():
        pass

    def unblock_member():
        pass

    def cancel_membership():
        pass
  
    def reset_password(self):
        pass
        # functionality

class Watchlist:
    def __init__(self, name, stocks):
        self.__name = name
        self.__stocks = stocks

    def get_stocks():
        pass

class Stock:
    def __init__(self, symbol, price):
        self.__symbol = symbol
        self.__price = price
        
class Search(ABC):
  def search_symbol(self, symbol):
    None

class StockInventory(Search):
    def __init__(self, inventory_name, last_update):
        self.__inventory_name = inventory_name
        self.__last_update = last_update

    def search_symbol(self, symbol):
        pass

class StockPosition:
    def __init__(self, symbol, quantity):
        self.__symbol = symbol
        self.__quantity = quantity

class StockLot:
    def __init__(self, iot_number, buying_order):
        self.__iot_number = iot_number
        self.__buying_order = buying_order

    def get_buying_price():
        pass

class OrderPart:
    def __init__(self, price, quantity, executed_at):
        self.__price = price
        self.__quantity = quantity
        self.__executed_at = executed_at

class Order(ABC):
    def __init__(self, order_number, is_buy_order, status, time_enforcement,
                 creation_time):
        self.__order_number = order_number
        self.__is_buy_order = is_buy_order
        self.__status = status
        self.__time_enforcement = time_enforcement
        self.__creation_time = creation_time
        self.__parts = {}

    def set_status(status):
        pass
  
    def save_in_database():
        pass
  
    def add_order_parts(parts):
        pass

class LimitOrder(Account):
    def __init__(self, order_number, is_buy_order, status, time_enforcement,
                 creation_time):
        super().__init__(order_number, is_buy_order, status, time_enforcement,
                         creation_time)

class StopLimitOrder(Account):
    def __init__(self, order_number, is_buy_order, status, time_enforcement,
                 creation_time):
        super().__init__(order_number, is_buy_order, status, time_enforcement,
                         creation_time)

class StopLossOrder(Account):
    def __init__(self, order_number, is_buy_order, status, time_enforcement,
                 creation_time):
        super().__init__(order_number, is_buy_order, status, time_enforcement,
                         creation_time)

class MarketOrder(Account):
    def __init__(self, order_number, is_buy_order, status, time_enforcement,
                creation_time):
        super().__init__(order_number, is_buy_order, status, time_enforcement,
                         creation_time)
        
class TransferMoney(ABC):
    def __init__(self, id, creation_date, from_account, to_account):
        self.__id = id
        self.__creation_date = creation_date
        self.__from_account = from_account
        self.__to_account = to_account

    @abstractmethod
    def initiate_transaction():
        pass
  
class ElectronicBank(TransferMoney):
    def __init__(self, id, creation_date, from_account, to_account, bank_name):
        super().__init__(id, creation_date, from_account, to_account)
        self.__bank_name = bank_name

    def initiate_transaction():
        # functionality
        pass

class Wire(TransferMoney):
    def __init__(self, id, creation_date, from_account, to_account, wire):
        super().__init__(id, creation_date, from_account, to_account)
        self.__wire = wire

    def initiate_transaction():
        # functionality
        pass

class Check(TransferMoney):
    def __init__(self, id, creation_date, from_account, to_account, check_number):
        super().__init__(id, creation_date, from_account, to_account)
        self.__check_number = check_number

    def initiate_transaction():
        # functionality
        pass

class DepositMonet:
    def __init__(self, transaction_id):
        self.__transaction_id = transaction_id

class WithdrawMoney:
    def __init__(self, transaction_id):
        self.__transaction_id = transaction_id
        
class Notification(ABC):
    def __init__(self, notification_id, creation_date, content):
        self.__notification_id = notification_id
        self.__creation_date = creation_date
        self.__content = content

    @abstractmethod
    def send_notification(self):
        pass

class SmsNotification(Notification):
    def __init__(self, notification_id, creation_date, content, phone_number):
        super().__init__(notification_id, creation_date, content)
        self.__phone_number = phone_number

    def send_notification(self):
        # functionality
        pass

class EmailNotification(Notification):
    def __init__(self, notification_id, creation_date, content, email):
        super().__init__(notification_id, creation_date, content)
        self.__email = email

    def send_notification(self):
        # functionality
        pass
    
# The StockExchange is a singleton class that ensures it will have only one
# active instance at a time
class __StockExchange(object):
    __instances = None
  
    def __new__(cls):
        if cls.__instances is None:
            cls.__instances = super(__StockExchange, cls).__new__(cls)
        return cls.__instances

class StockExchange(metaclass=__StockExchange):
    def __init__(self):
        pass
    
    def place_order(order):
      pass