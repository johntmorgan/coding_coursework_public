#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:28:45 2023

@author: johnmorgan
"""

class PaymentStatus(enum.Enum):
  PENDING = 1
  CONFIRMED = 2
  DECLINED = 3
  REFUNDED = 4

class BookingStatus(enum.Enum):
  PENDING = 1
  CONFIRMED = 2
  CANCELLED = 3
  DENIED = 4
  REFUNDED = 5

class PaymentStatus(enum.Enum):
  AVAILABLE = 1
  BOOKED = 2
  RESERVED = 3
  
from abc import ABC, abstractmethod

class Person(ABC):
  def __init__(self, name, address, phone, email):
    self.__name = name
    self.__address = address
    self.__phone = phone
    self.__email = email

class Customer(Person):
  def __init__(self, name, address, phone, email):
    self.__bookings = [] # List of bookings 
    super().__init__(name, address, phone, email)
  
  # booking here refers to an instance of the Booking class 
  def create_booking(self, booking):
    pass
  def update_booking(self, booking):
    pass
  def delete_booking(self, booking):
    pass

class Admin(Person):
  def __init__(self, name, address, phone, email):
    super().__init__(name, address, phone, email)

  # show here refers to an instance of the ShowTime class
  def add_show(self, show):
    pass
  def update_show(self, show):
    pass
  def delete_show(self, show):
    pass
  def add_movie(self, movie):
    pass
  def delete_movie(self, movie):
    pass

class TicketAgent(Person):
  def __init__(self, name, address, phone, email):
    super().__init__(name, address, phone, email)

  # booking here refers to an instance of the Booking class
  def create_booking(self, booking):
    pass
  
# Seat is an abstract class
from abc import ABC, abstractmethod

class Seat(ABC):
  # Data members
  def __init__(self, seat_no, status):
    self.__seat_no = seat_no
    self.__status = status # Refers to the SeatStatus enum

  # Member functions
  def is_available(self):
    pass

  @abstractmethod
  def set_seat(self):
    pass

  @abstractmethod
  def set_rate(self):
    pass

class Platinum(Seat):
  def __init__(self, seat_no, status, rate):
    self.__rate = rate
    super().__init__(seat_no, status)

  def set_seat(self):
    # functionality

  def set_rate(self):
    # functionality

class Gold(Seat):
  def __init__(self, seat_no, status, rate):
    self.__rate = rate
    super().__init__(seat_no, status)

  def set_seat(self):
    # functionality

  def set_rate(self):
    # functionality

class Silver(Seat):
  def __init__(self, seat_no, status, rate):
    self.__rate = rate
    super().__init__(seat_no, status)

  def set_seat(self):
    # functionality

  def set_rate(self):
    # functionality
    
class Movie:
  # Data members
  def __init__(self, title, genre, language, release_date, duration):
    self.__title = title
    self.__genre = genre
    # release_date attribute represent date and time
    self.__release_date = release_date
    self.__language = language
    self.__duration = duration
    self.__shows = [] # List of shows

class ShowTime:
  # Data members
  def __init__(self, show_id, start_time, date, duration):
    self.__show_id = show_id
    # __start_time and __date attributes represent date and time
    self.__start_time = start_time
    self.__date = date
    self.__duration = duration
    self.__seats = [] # List of seats

  # Displays the list of available seats
  def show_available_seats():
    pass

class MovieTicket:
  # Data members
  def __init__(self, ticket_id, seat, movie, show):
    self.__ticket_id = ticket_id
    self.__seat = seat # References an instance of the Seat class
    self.__movie = movie # References an instance of the Movie class
    self.__show = show # References an instance of the ShowTime class
    
class City:
  # Data members
  def __init__(self, name, state, zip_code):
    self.__name = name
    self.__state = state
    self.__zip_code = zip_code
    self.__cinemas = [] # List of cinemas

class Cinema: 
  # Data members
  def __init__(self, cinema_id, city):
    self.__cinema_id = cinema_id
    self.__city = city # Refers to an instance of the City class
    self.__halls = [] # List of halls

class Hall:
  # Data members
  def __init__(self, hall_id):
    self.__hall_id = hall_id
    self.__shows = [] # List of shows

  # Returns list of shows
  def find_current_shows():
    pass

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
  def __init__(self, amount, timestamp, status, name_on_card, card_number, billing_address, code):
    self.__name_on_card = name_on_card
    self.__card_number = card_number
    self.__billing_address = billing_address
    self.__code = code
    super().__init__(amount, timestamp, status)

  def make_payment(self):
    # functionality
    pass

# Notification is an abstract class
from abc import ABC, abstractmethod

class Notification(ABC):
  def __init__(self, notification_id, created_on, content):
    self.__notification_id = notification_id
    self.__created_on = created_on
    self.__content = content

  # person here refers to an instance of the Person class 
  @abstractmethod
  def send_notification(self, person):
    pass

class EmailNotification(Notification):
  def __init__(self, notification_id, created_on, content):
    super().__init__(notification_id, created_on, content)

  # person here refers to an instance of the Person class 
  def send_notification(self, person):
    # functionality
    pass

class PhoneNotification(Notification):
  def __init__(self, notification_id, created_on, content):
    super().__init__(notification_id, created_on, content)

  # person here refers to an instance of the Person class 
  def send_notification(self, person):
    # functionality
    pass

class Booking: 
  # Data members
  def __init__(self, booking_id, amount, total_seats, created_on, status, payment, show):
    self.__booking_id = booking_id
    self.__amount = amount
    self.__total_seats = total_seats
    self.__created_on = created_on
    self.__status = status # BookingStatus enum
    
    # Instances of classes
    self.__payment = payment
    self.__show = show
    self.__tickets = [] # List of movie tickets
    self.__seats = [] # List of seats
    
from abc import ABC, abstractmethod

class Search(ABC):
  # Returns list of movie titles
  def search_movie_title(self, title):
    pass

  # Returns list of movie languages
  def search_movie_language(self, language):
    pass
    
  # Returns list of movie genres
  def search_movie_genre(self, genre):
    pass

  # Returns list of movie release dates
  def search_movie_release_date(self, date):
    pass


class Catalogue(Search):
  def __init__(self):
    self.__movie_titles = {}
    self.__movie_languages = {}
    self.__movie_genres = {}
    self.__movie_release_dates = {}

  # Returns list of movie titles
  def search_movie_title(self, title):
    # functionality
    pass

  # Returns list of movie languages
  def search_movie_language(self, language):
    # functionality
    pass

  # Returns list of movie genres
  def search_movie_genre(self, genre):
    # functionality
    pass

  # Returns list of movie release dates
  def search_movie_release_date(self, date):
    # functionality
    pass