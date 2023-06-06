#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:28:42 2023

@author: johnmorgan
"""

class VehicleStatus(enum.Enum):
  AVAILABLE = 1
  RESERVED = 2
  LOST = 3
  BEING_SERVICED = 4

class AccountStatus(enum.Enum):
  ACTIVE = 1
  CLOSED = 2
  CANCELED = 3
  BLACKLISTED = 4
  BLOCKED = 5

class ReservationStatus(enum.Enum):
  ACTIVE = 1
  PENDING = 2
  CONFIRMED = 3
  COMPLETED = 4
  CANCELED = 5

class PaymentStatus(enum.Enum):
  UNPAID = 1
  PENDING = 2
  COMPLETED = 3
  CANCELED = 4
  REFUNDED = 5

class VanType(enum.Enum):
  PASSENGER = 1
  CARGO = 2

class CarType(enum.Enum):
  ECONOMY = 1
  COMPACT = 2
  INTERMEDIATE = 3
  STANDARD = 4
  FULL_SIZE = 5
  PREMIUM = 6
  LUXURY = 7

class MotorcycleType(enum.Enum):
  STANDARD = 1
  CRUISER = 2
  TOURING = 3
  SPORTS = 4
  OFF_ROAD = 5
  DUAL_PURPOSE = 6

class TruckType(enum.Enum)
  LIGHT_DUTY = 1
  MEDIUM_DUTY = 2
  HEAVY_DUTY = 3

class VehicleLogType(enum.Enum):
  ACCIDENT = 1
  FUELING = 2
  CLEANING_SERVICE = 3
  OIL_CHANGE = 4
  REPAIR = 5
  OTHER = 6
  
 class Address:
  def __init__(self, street_address, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country

class Person:
  def __init__(self, name, address, email, phone_number):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone_number = phone_number

class Driver(Person):
  def __init__(self, name, address, email, phone_number, driver_id):
    super().__init__(name, address, email, phone_number)
    self.__driver_id = driver_id

# Vehicle is an abstract class
from abc import ABC, abstractmethod

class Vehicle(ABC):
  def __init__(self, vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage):
    self.__vehicle_id = vehicle_id
    self.__license_number = license_number
    self.__passenger_capacity = passenger_capacity
    self.__has_sunroof = has_sunroof
    self.__status = status
    self.__model = model
    self.__manufacturing_year = manufacturing_year
    self.__mileage = mileage
    self.__log = []

  def reserve_vehicle(self):
    None

  def return_vehicle(self):
    None

class Car(Vehicle):
  def __init__(self, vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage, car_type):
    super().__init__(vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage)
    self.__type = type


class Van(Vehicle):
  def __init__(self, vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage, van_type):
    super().__init__(vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage)
    self.__type = type


class Truck(Vehicle):
  def __init__(self, vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage, truck_type):
    super().__init__(vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage)
    self.__type = type

class Motorcycle(Vehicle):
  def __init__(self, vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage, motorcycle_type):
    super().__init__(vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage)
    self.__type = type

from abc import ABC, abstractmethod

class Account(ABC):
  def __init__(self, name, address, email, phone_number, account_id, password, person):
    super().__init__(name, address, email, phone_number)
    self.__id = account_id
    self.__password = password
    self.__status = AccountStatus.NONE

  @abstractmethod
  def reset_password(self):
    None

class Receptionist(Account):
  def __init__(self, name, address, email, phone_number, account_id, password, person, date_joined):
    super().__init__(name, address, email, phoneNumber, accountId, password, person, status)
    self.__date_joined = date_joined


  def search_customer(self, name):
    None

  def add_reservation(self):
    None

  def cancel_reservation(self):
    None

  def reset_password(self):
    # functionality
  

class Customer(Account):
  def __init__(self, name, address, email, phone_number, account_id, password, person, license_number, lisense_expiry):
    super().__init__(name, address, email, phone_number, account_id, password, person, status)
    self.__license_number = license_number
    self.__lisense_expiry = lisense_expiry

  def add_reservation(self):
    None
    
  def cancel_reservation(self):
    None
    
  def get_reservations(self):
    None

  def reset_password(self):
    # functionality
    
# Equipment is an abstract class
from abc import ABC, abstractmethod

class Equipment(ABC):
  def __init__(self, equipment_id, price):
    self.__equipment_id = equipment_id
    self.__price = price

class Navigation(Equipment):
  def __init__(self, equipment_id, price):
    super().__init__(equipment_d, price)

class ChildSeat(Equipment):
  def __init__(self, equipment_id, price):
    super().__init__(equipmentId, price)

class SkiRack(Equipment):
  def __init__(self, equipment_id, price):
    super().__init__(equipment_id, price)
    
# Service is an abstract class
from abc import ABC, abstractmethod

class Service(ABC):
  def __init__(self, service_id, price):
    self.__service_id = service_id
    self.__price = price

class DriverService(Service):
    def __init__(self, service_id, price, driver_id):
        super().__init__(service_id, price)
        self.__driver_id = driver_id

class RoadsideAssistance(Service):
    def __init__(self, service_id, price):
        super().__init__(service_id, price)

class WiFi(Service):
    def __init__(self, service_id, price):
        super().__init__(service_id, price)
        
# Payment is an abstract class
from abc import ABC, abstractmethod

class Payment(ABC):
  # Data members
  def __init__(self, amount, timestamp, status):
    self.__amount = amount
    self.__timestamp = timestamp
    self.__status = status # Refers to the PaymentStatus enum

  @abstractmethod
  def make_payment(self):
    pass

class Cash(Payment):
  def __init__(self, amount, timestamp, status):
    super().__init__(amount, timestamp, status)

  def make_payment(self):
    # functionality
    pass

class CreditCard(Payment):
  # Data members
  def __init__(self, amount, timestamp, status, name_on_card, card_number,
               billing_address, code):
    self.__name_on_card = name_on_card
    self.__card_number = card_number
    self.__billing_address = billing_address
    self.__code = code
    super().__init__(amount, timestamp, status)

  def make_payment(self):
    # functionality
    pass

class VehicleLog:
  def __init__(self, log_id, log_type, description, creation_date):
    self.__log_id = log_id
    self.__log_type = log_type
    self.__description = description
    self.__creation_date = creation_date


class VehicleReservation:
  def __init__(self, reservation_id, customer_id, vehicle_id, due_date,
               return_date, pickup_location, return_location):
    self.__reservation_id = reservation_id
    self.__customer_id = customer_id
    self.__vehicle_id = vehicle_id
    self.__creation_date = datetime.date.today()
    self.__status = ReservationStatus.ACTIVE
    self.__due_date = due_date
    self.__return_date = return_date
    self.__pickup_location = pickup_location
    self.__return_location = return_location

    self.__equipments = []
    self.__services = []

  def add_equipment(self):
    None

  def add_service(self):
    None

# Notification is an abstract class
from abc import ABC, abstractmethod
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

    # account here refers to an instance of the Account class 
    def send_notification(account):
        # functionality 
        pass

class EmailNotification(Notification):
    def __init__(self, notification_id, created_on, content):
        super().__init__(notification_id, created_on, content)

    # account here refers to an instance of the Account class 
    def send_notification(account):
        # functionality 
        pass
    
class ParkingStall:
  def __init__(self, stall_id, location_identifier):
    self.__stall_id = stall_id
    self.__location_identifier = location_identifier

class Fine:
  def __init__(self, amount, reason):
    self.__amount = amount
    self.__reason = reason

  def calculate_fine(self):
    None
    
from abc import ABC, abstractmethod

class Search(ABC):
  def search_by_type(self, type):
    None

  def search_by_model(self, model):
    None

class VehicleCatalog(Search):
  def __init__(self):
    self.__vehicle_types = {}
    self.__vehicle_models = {}

  # to return all vehicles of the given type.
  def search_by_type(self, type):
    pass

  # to return all vehicles of the given model.
  def search_by_model(self, model):
    pass

