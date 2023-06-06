#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:11:41 2023

@author: johnmorgan
"""

from enum import Enum
from abc import ABC, abstractmethod

class Address:
  def __init__(self, zip_code, street_address, city, state, country):
    self.__zip_code = zip_code
    self.__street_address = street_address
    self.__city = city
    self.__state = state
    self.__country = country

class AccountStatus(Enum):
  ACTIVE = 1 
  DISABLED = 2
  CLOSED = 3
  BLOCKED = 4

class SeatStatus(Enum):
  AVAILABLE = 1 
  BOOKED = 2
  CHANCE = 3

class SeatType(Enum):
  REGULAR = 1 
  ACCESSIBLE = 2
  EMERGENCY_EXIT = 3
  EXTRA_LEG_ROOM = 4

class SeatClass(Enum):
  ECONOMY = 1 
  ECONOMY_PLUS = 2
  BUSINESS = 3
  FIRST_CLASS = 4

class FlightStatus(Enum):
  ACTIVE = 1 
  SCHEDULED = 2
  DELAYED = 3
  LANDED = 4
  DEPARTED = 5
  CANCELED = 6
  DIVERTED = 7
  UNKNOWN = 8

class ReservationStatus(Enum):
  REQUESTED = 1 
  PENDING = 2
  CONFIRMED = 3
  CHECKED_IN = 4
  CANCELED = 5

class PaymentStatus(Enum):
  PENDING = 1 
  COMPLETED = 2
  FAILED = 3
  DECLINED = 4
  CANCELED = 5
  REFUNDED = 6

class Account:
  def __init__(self, status, account_id, username, password):
    self.__status = status # Refers to the AccountStatus enum
    self.__account_id = account_id
    self.__username = username
    self.__password = password

  def reset_password(self):
    pass 

class Account:
  def __init__(self, passenger_id, name, date_of_birth, gender,
               passport_number):
    self.__passenger_id = passenger_id 
    self.__name = name
    self.__date_of_birth = date_of_birth
    self.__gender = gender
    self.__passport_number = passport_number
    
class Person(ABC):
  def __init__(self, name, address, email, phone, account):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__account = account

class Admin(Person):
  def __init__(self, name, address, email, phone, account):
    super().__init__(name, address, email, phone, account)

  def add_aircraft(self, aircraft):
    None
  
  def add_flight(self, flight):
    None
  
  def cancel_flight(self, flight):
    None

  def assign_crew(self, flight):
    None

  def block_user(self, user):
    None

  def unblock_user(self, user):
    None

class Crew(Person):
  def __init__(self, name, address, email, phone, account):
    super().__init__(name, address, email, phone, account)
  
  def view_schedule(self):
    None

class FrontDeskOfficer(Person):
  def __init__(self, name, address, email, phone, account):
    super().__init__(name, address, email, phone, account)
  
  def view_itinerary():
    None

  def create_itinerary():
    None

  def create_reservation():
    None

  def assign_seat():
    None
  
  def make_payment():
    None

class Customer(Person):
  def __init__(self, name, address, email, phone, account, customer_id):
    self.__customer_id = customer_id
    
    super().__init__(name, address, email, phone, account)
  
  def view_itinerary():
    None

  def create_itinerary():
    None

  def create_reservation():
    None

  def assign_seat():
    None
  
  def make_payment():
    None

class Seat:
  def __init__(self, seat_number, seat_type, _class):
    self.__seat_number = seat_number 
    self.__seat_type = seat_type
    self.___class = _class


class FlightSeat(Seat):
  def __init__(self, fare, status, email, seat_number, seat_type, _class,
               reservation_number):
    self.__fare = fare
    self.__status = status
    self.__reservation_number = reservation_number
  
    super().__init__(seat_number, seat_type, _class)

class Flight:
  def __init__(self, flight_no, duration_min, departure, arrival):
    self.__flight_no = flight_no 
    self.__duration_min = duration_min
    self.__departure = departure
    self.__arrival = arrival
    self.__instances = []

class FlightInstance:
  def __init__(self, flight, departure_time, gate, status, aircraft, seats):
    self.__flight = flight 
    self.__departure_time = departure_time
    self.__gate = gate
    self.__status = status
    self.__aircraft = aircraft
    self.__seats = seats
  
class Itinerary:
  def __init__(self, starting_airport, final_airport, creation_date,
               reservations, passengers):
    self.__starting_airport = starting_airport
    self.__final_airport = final_airport
    self.__creation_date = creation_date
    self.__reservations = reservations
    self.__passengers = passengers

  def make_reservation(self):
    pass 

  def make_payment(self):
    pass 

class FlightReservation:
  def __init__(self, reservation_number, flight, seat_map, status, creation_date):
    self.__reservation_number = reservation_number 
    self.__flight = flight
    self.__seat_map = seat_map
    self.__status = status
    self.__creation_date = creation_date

class Payment(ABC):
  def __init__(self, payment_id, amount, status, timestamp):
    self.__payment_id = payment_id
    self.__amount = amount
    self.__status = status # Refers to the PaymentStatus enum
    self.__timestamp = timestamp

  @abstractmethod
  def make_payment(self):
    pass

class Cash(Payment):
  def __init__(self, payment_id, amount, status, timestamp):
    super().__init__(payment_id, amount, status, timestamp)

  def make_payment(self):
    # functionality
    pass

class CreditCard(Payment):
  def __init__(self, payment_id, amount, status, timestamp, name_on_card,
               card_number):
    self.__name_on_card = name_on_card
    self.__card_number = card_number
    super().__init__(payment_id, amount, status, timestamp)

  def make_payment(self):
    # functionality
    pass

class Notification(ABC):
  def __init__(self, notification_id, created_on, content):
    self.__notification_id = notification_id
    self.__created_on = created_on
    self.__content = content

    # account here refers to an instance of the Account class 
  @abstractmethod
  def send_notification(account):
    pass

class SmsNotification(Notification):
  def __init__(self, notification_id, created_on, content):
    super().__init__(notification_id, created_on, content)

  def send_notification(account):
    # functionality 
    pass

class EmailNotification(Notification):
  def __init__(self, notification_id, created_on, content):
    super().__init__(notification_id, created_on, content)

  def send_notification(account):
    # functionality 
    pass

class Search(ABC):
  def search_flight(self, source, dest, arrival, departure):
    pass

class SearchCatalog(Search):
  def __init__(self):
    self.__flights = {}

  def search_flight(self, source, dest, arrival, departure):
    # functionality
    pass

class Airport:
  def __init__(self, name, code, address):
    self.__name = name
    self.__code = code
    self.__address = address
    self.__flights = [] # List of flights

class Aircraft:
  def __init__(self, name, code, model, seat_capacity, seats):
    self.__name = name
    self.__code = code
    self.__models = model
    self.__seat_capacity = seat_capacity
    self.__seats = [] # List of seats

# The Airline is a singleton class that ensures it will have only one active
# instance at a time
class __Airline(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__Airline, cls).__new__(cls)
    return cls.__instances

class Airline(metaclass = __Airline):
  def __init__(self, name, code):
    self.__name = name
    self.__code = code
    self.__flights = [] # List of flights
    self.__aircrafts = [] # List of aircrafts
    self.__crew = [] # List of crew
