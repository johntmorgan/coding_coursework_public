#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:21:04 2023

@author: johnmorgan
"""

# definition of enumerations used in library management system
class BookFormat(Enum):
  HARDCOVER = 1
  PAPERBACK = 2
  AUDIOBOOK = 3
  EBOOK = 4
  NEWSPAPER = 5
  MAGAZINE = 6
  JOURNAL = 7


class BookStatus(Enum):
  AVAILABLE = 1
  RESERVED = 2
  LOANED = 3
  LOST = 4


class ReservationStatus(Enum):
  WAITING = 1
  PENDING = 2
  CANCELED = 3
  NONE = 4


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


class Person(ABC):
  def __init__(self, name, address, email, phone):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    
# User is an abstract class
from abc import ABC, abstractmethod

class User(ABC):
  def __init__(self, id, password, person, status=AccountStatus.ACTIVE, card):
    self.__id = id
    self.__password = password
    self.__status = status
    self.__person = person
    self.__card = card

  @abstractmethod
  def reset_password(self):
    pass


class Librarian(User):
  def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
    super().__init__(id, password, person, status)

  def add_book_item(self, book_item):
    None

  def block_member(self, member):
    None

  def unblock_member(self, member):
    None

  def reset_password(self):
    pass


class Member(User):
  def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
    super().__init__(id, password, person, status)
    self.__date_of_membership = datetime.date.today()
    self.__total_books_checked_out = 0

  def reserve_book_item(self, book_item):
    None

  def increment_total_books_checked_out(self):
    None

  def checkout_book_item(self, book_item):
    None

  def check_for_fine(self, book_item_barcode):
    None

  def return_book_item(self, book_item):
    None

  def renew_book_item(self, book_item):
    None
    
  def reset_password(self):
    pass

class BookReservation:
  def __init__(self, creation_date, status, item_id, member_id):
    self.__creation_date = creation_date
    self.__status = status
    self.__item_id = item_id
    self.__member_id = member_id

  def fetch_reservation_details(self, book_item_id):
    None


class BookLending:
  def __init__(self, creation_date, due_date, book_item_id, member_id):
    self.__creation_date = creation_date
    self.__due_date = due_date
    self.__return_date = None
    self.__book_item_id = book_item_id
    self.__member_id = member_id

  def lend_book(self, item_id, member_id):
    None

  def fetch_lending_details(self, item_id):
    None


class Fine:
  def __init__(self, creation_date, book_item_id, member_id):
    self.__creation_date = creation_date
    self.__book_item_id = book_item_id
    self.member_id = member_id

  def collect_fine(self, member_id, days):
    None
    
# User is an abstract class
from abc import ABC, abstractmethod

class Book(ABC):
  def __init__(self, isbn, title, subject, publisher, language, number_of_pages, book_format):
    self.__isbn = isbn
    self.__title = title
    self.__subject = subject
    self.__publisher = publisher
    self.__language = language
    self.__number_of_pages = number_of_pages
    self.__book_format = book_format
    self.__authors = []

class BookItem(Book):
  def __init__(self, id, is_reference_only, borrowed, due_date, price, status,
               date_of_purchase, publication_date, placed_at):
    self.__id = id
    self.__is_reference_only = is_reference_only
    self.__borrowed = borrowed
    self.__due_date = due_date
    self.__price = price
    self.__status = status
    self.__date_of_purchase = date_of_purchase
    self.__publication_date = publication_date
    self.__placed_at = placed_at

  def checkout(self, member_id):
    None

class Rack:
  def __init__(self, number, location_identifier):
    self.__number = number
    self.__location_identifier = location_identifier
    
# User is an abstract class
from abc import ABC, abstractmethod

class Notification(ABC)):
  def __init__(self, notification_id, creation_date, content):
    self.__notification_id = notification_id
    self.__creation_date = creation_date
    self.__content = content

  def send_notification(self):
    None

class PostalNotification(Notification):
  def __init__(self, notification_id, creation_date, content, address):
    super().__init__(notification_id, creation_date, content)
    self.__address = address

class EmailNotification(Notification):
  def __init__(self, notification_id, creation_date, content, email):
    super().__init__(notification_id, creation_date, content)
    self.__email = email
    
from abc import ABC, abstractmethod
class Search(ABC):
  def search_by_title(self, title):
    None

  def search_by_author(self, author):
    None

  def search_by_subject(self, subject):
    None

  def search_by_publication_date(self, publish_date):
    None


class Catalog(Search):
  def __init__(self):
    self.__book_titles = {}
    self.__book_authors = {}
    self.__book_subjects = {}
    self.__book_publication_dates = {}

  def search_by_title(self, title):
    None

  def search_by_author(self, author):
    None

  def search_by_subject(self, subject):
    None

  def search_by_publication_date(self, publish_date):
    None
    
# The Library is a singleton class that ensures it will have only one active instance at a time

class __Library(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__Library, cls).__new__(cls)
    return cls.__instances

class Library(metaclass = __Library):
  def __init__(self, id, name, address):
    self.__name = name
    self.__address = address
    self.__parking_rate = parking_rate

  def get_address(self):
    None