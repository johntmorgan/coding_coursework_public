#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:55:51 2023

@author: johnmorgan
"""

# definition of enumerations used in elevator system
class RoomStatus(enum.Enum):
  AVAILABLE = 1
  RESERVED = 2
  OCCUPIED = 3
  NOT_AVAILABLE = 4
  BEING_SERVICED = 5
  OTHER = 6


class BookingStatus(enum.Enum):
  REQUESTED = 1
  PENDING = 2
  CONFIRMED = 3
  CANCELED = 4
  ABANDONED = 5


class AccountStatus(enum.Enum):
  ACTIVE = 1
  CLOSED = 2
  CANCELED = 3
  BLACKLISTED = 4
  BLOCKED = 5


class AccountType(enum.Enum):
  MEMBER = 1
  GUEST = 2
  MANAGER = 3
  RECEPTIONIST = 4


class PaymentStatus(enum.Enum):
  UNPAID = 1
  PENDING = 2
  COMPLETED = 3
  FILLED = 4
  DECLINED = 5
  CANCELLED = 6
  ABANDONED = 7
  SETTLING = 8
  SETTLED = 9
  REFUNDED = 10
  
class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country

class Account:
  def __init__(self, id, password, status=AccountStatus.ACTIVE):
    self.__id = id
    self.__password = password
    self.__status = status

  def reset_password(self):
    None
    
from abc import ABC, abstractmethod
class Person(ABC):
  def __init__(self, name, address, email, phone, account):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__account = account

class Guest(Person):
  def __init__(self):
    self.__total_rooms_checked_in = 0

  def get_bookings(self):
    None

class Receptionist(Person):
  def search_member(self, name):
    None

  def create_booking(self):
    None

class Housekeeper(Person):
  def assignToRoom():
    None
    
from abc import ABC, abstractmethod
class RoomCharge(ABC):
  def __init__(self):
    self.__issue_at = datetime.date.today()

  def add_invoice_item(self, invoice):
    None

class Amenity(Service):
  def __init__(self, name, description):
    self.__name = name
    self.__description = description

class RoomService(Service):
  def __init__(self, is_chargeable, request_time):
    self.__is_chargeable = is_chargeable
    self.__request_time = request_time

class KitchenService(Service):
  def __init__(self, description):
    self.__description = description
    
class Invoice:
    def __init__(self, amount):
        self.__amount = amount
    
    def create_bill():
        None
        
class RoomBooking:
  def __init__(self, reservation_number, start_date, duration_in_days,
               booking_status):
    self.__reservation_number = reservation_number
    self.__start_date = start_date
    self.__duration_in_days = duration_in_days
    self.__booking_status = booking_status
    self.__checkin = None
    self.__checkout = None
    self.__guest_id = 0
    self.__room = None
    self.__invoice = None
    self.__notifications = []

  def fetch_details(self, reservation_number):
    None
    
# BillTransaction is an abstract class
from abc import ABC, abstractmethod
class BillTransaction(ABC):
    def __init__(self, creation_date, amount, status):
        self.__creation_date = creation_date
        self.__amount = amount
        self.status = status

    @abstractmethod
    def initiate_transaction():
        pass

class CheckTransaction(BillTransaction):
    def __init__(self, creation_date, amount, status, bank_name, check_number):
        super().__init__(creation_date, amount, status)
        self.__bank_name = bank_name
        self.__check_number = check_number

    def initiate_transaction():
        pass

class CreditCardTransaction(BillTransaction):
    def __init__(self, creation_date, amount, status, name_on_card, zip_code):
        super().__init__(creation_date, amount, status)
        self.__name_on_card = name_on_card
        self.__zip_code = zip_code

    def initiate_transaction():
        pass

class CashTransaction(BillTransaction):
    def __init__(self, creation_date, amount, status, cash_tendered):
        super().__init__(creation_date, amount, status)
        self.__cash_tendered = cash_tendered

    def initiate_transaction():
        pass
    
# Notification is an abstract class
from abc import ABC, abstractmethod
class Notification(ABC):
    def __init__(self, notification_id, created_on, content):
        self.__notificationId = notificationId
        self.__created_on = created_on
        self.__content = content

    # account here refers to an instance of the Account class 
    @abstractmethod
    def send_notification(person):
        pass

class SMSNotification(Notification):
    def __init__(self, notification_id, created_on, content):
        super().__init__(notification_id, created_on, content)

    # account here refers to an instance of the Account class 
    def send_notification(person):
        # functionality 
        pass

class EmailNotification(Notification):
    def __init__(self, notification_id, created_on, content):
        super().__init__(notification_id, created_on, content)

    # account here refers to an instance of the Account class 
    def send_notification(person):
        # functionality 
        pass
    
class Room:
    def __init__(self, room_number, style, status, booking_price, is_smoking):
        self.__room_number = room_number
        self.__style = style
        self.__status = status
        self.__booking_price = booking_price
        self.__is_smoking = is_smoking
        self.__keys = []
        self.__room_housekeeping_log = []

    def is_room_available():
        None

    def checkin():
        None

    def checkout():
        None

class RoomKey:
  def __init__(self, key_id, barcode, is_active, is_master):
    self.__key_id = key_id
    self.__barcode = barcode
    self.__issued_at = datetime.date.today()
    self.__is_active = is_active
    self.__is_master = is_master

  def assign_room(self, room):
    None


class RoomHousekeeping:
  def __init__(self, description, duration, housekeeper):
    self.__description = description
    self.__start_datetime = datetime.date.today()
    self.__duration = duration
    self.__housekeeper = housekeeper

  def add_housekeeping(self, room):
    None
    
from abc import ABC, abstractmethod
class Search(ABC):
    def search(style, start_date, duration):
        None


class Catalog(Search):
    def __init__(self):
        self.__rooms = []

    def search(style, date, duration):
        None
        
class HotelBranch:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
  
    def get_rooms():
        None

# Singleton patter, but not implemented? - JM
class Hotel:
    def __init__(self, name, hotel_branch):
        self.__name = name
        self.__hotel_branch = hotel_branch

    def add_location(self, location):
        None