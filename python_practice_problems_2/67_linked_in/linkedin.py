#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:44:46 2023

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
  DEACTIVATED = 2
  BLOCKED = 3
  DELETED = 4

class ConnectionInviteStatus(Enum):
  PENDING = 1 
  ACCEPTED = 2
  IGNORED = 3

class JobStatus(Enum):
  OPEN = 1 
  ON_HOLD = 2
  CLOSED = 3
  
class Account:
  def __init__(self, account_id, password, username, email, status):
    self.__account_id = account_id
    self.__password = password
    self.__username = username
    self.__email = email
    self.__status = status # Refers to the AccountStatus enum

  def reset_password(self):
    pass 



class Person(ABC):
  def __init__(self, name, address, email, phone, account):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__account = account

#Admin extends Person
class Admin(Person):
  def __init__(self, name, address, email, phone, account):
    super().__init__(name, address, email, phone, account)
  
  def block_user(self, user):
    pass
  def unblock_user(self, user):
    pass
  def disable_page(self, page):
    pass
  def enable_page(self, page):
    pass
  def delete_group(self, group):
    pass

# User extends Person
class User(Person):
  def __init__(self, name, address, email, phone, account, user_id,
               date_of_joining, profile):
    self.__user_id = user_id
    self.__date_of_joining = date_of_joining
    self.__profile = profile
    self.__connections = []
    self.__follows_users = []
    self.__follows_companies = []
    self.__joined_groups = []
    self.__created_pages = []
    self.__created_groups = []
    super().__init__(name, address, email, phone, account)
  
    def send_message(self, message):
      pass
    def send_invite(self, invite):
      pass
    def cancel_invite(self, invite):
      pass
    def create_page(self, page):
      pass
    def delete_page(self, page):
      pass
    def create_group(self, group):
      pass
    def delete_group(self, group):
      pass
    def create_post(self, post):
      pass
    def delete_post(self, post):
      pass
    def create_comment(self, comment):
      pass
    def delete_comment(self, comment):
      pass
    def react(self, post):
      pass
    def request_recommendation(self, user):
      pass
    def accept_recommendation(self, user):
      pass
    def apply_for_job(self, job):
      pass

class Recommendation:
  def __init__(self, user_id, created_on, description, is_accepted):
    self.__user_id = user_id
    self.__created_on = created_on
    self.__description = description
    self.__is_accepted = is_accepted

class Achievement:
  def __init__(self, title, date_awarded, description):
    self.__title = title
    self.__date_awarded = date_awarded
    self.__description = description

class Analytics:
  def __init__(self, search_appearances, profile_views, post_impressions,
               total_connections):
    self.__search_appearances = search_appearances
    self.__profile_views = profile_views
    self.__post_impressions = post_impressions
    self.__total_connections = total_connections
    
class Experience:
  def __init__(self, title, company, location, start_date, end_date,
               description):
    self.__title = title
    self.__company = company
    self.__location = location
    self.__start_date = start_date
    self.__end_date = end_date
    self.__description = description

class Education:
  def __init__(self, school, degree, start_date, end_date, description):
    self.__school = school
    self.__degree = degree
    self.__start_date = start_date
    self.__end_date = end_date
    self.__description = description

class Skill:
  def __init__(self, name):
    self.__name = name

class Profile:
  def __init__(self, headline, about, gender, profile_picture,
               cover_photo):
    self.__headline = headline
    self.__about = about
    self.__gender = gender
    self.__profile_picture = profile_picture
    self.__cover_photo = cover_photo
    self.__experiences = []
    self.__education = []
    self.__skills = []
    self.__achievements = []
    self.__recommendations = []
    self.__analytics = Analytics(0, 0, 0, 0)
  
  def add_experience(self, experience):
    pass
  def add_education(self, education):
    pass
  def add_skill(self, skill):
    pass
  def add_achievement(self, achievement):
    pass

class Job:
  def __init__(self, job_id, job_title, date_of_posting, description, company,
               employment_type, location, status):
    self.__job_id = job_id
    self.__job_title = job_title
    self.__date_of_posting = date_of_posting
    self.__description = description
    self.__company = company
    self.__employment_type = employment_type
    self.__location = location
    self.__status = status
    
class CompanyPage:
  def __init__(self, page_id, name, description, company_type, company_size,
               created_by):
    self.__page_id = page_id
    self.__name = name
    self.__description = description
    self.__company_type = company_type
    self.__company_size = company_size
    self.__created_by = created_by
    self.__jobs = []
  
  def create_job_posting(self):
    pass
  def delete_job_posting(self, job):
    pass

class Group:
  def __init__(self, group_id, name, description, total_members, members):
    self.__group_id = group_id
    self.__name = name
    self.__description = description
    self.__total_members = total_members
    self.__members = members
  
  def update_description(self):
    pass

class Post:
  def __init__(self, post_id, post_owner, text, media):
    self.__post_id = post_id
    self.__post_owner = post_owner
    self.__text = text
    self.__media = media
    self.__total_reacts = 0
    self.__total_shares = 0
    self.__comments = []
  
  def update_text(self):
    pass

class Comment:
  def __init__(self, comment_id, comment_owner, text):
    self.__comment_id = comment_id
    self.__comment_owner = comment_owner
    self.__text = text
    self.__total_reacts = 0
    self.__comments = []
  
  def update_text(self):
    pass

class Message:
  def __init__(self, message_id, sender, recipients, text, media):
    self.__message_id = message_id
    self.__sender = sender
    self.__recipients = recipients
    self.__text = text
    self.__media = media
  
  def add_recipients(self, recipients):
    pass

class ConnectionInvitation:
  def __init__(self, sender, recipients, date_created, status):
    self.__sender = sender
    self.__recipients = recipients
    self.__date_created = date_created
    self.__status = status
  
  def accept_connection(self):
    pass

  def reject_connection(self):
    pass

class Search(ABC):
  def search_user(self, name):
    pass
  def search_company(self, name):
    pass
  def search_group(self, name):
    pass
  def search_job(self, title):
    pass

class SearchCatalog(Search):
  def __init__(self):
    self.__users = {}
    self.__companies = {}
    self.__groups = {}
    self.__jobs = {}

  def add_new_user(self, user):
    pass
  def add_new_company(self, company):
    pass
  def add_new_group(self, group):
    pass
  def add_new_job(self, job):
    pass

  def search_user(self, name):
    # functionality
    pass
  def search_company(self, name):
    # functionality
    pass
  def search_group(self, name):
    # functionality
    pass
  def search_job(self, title):
    # functionality
    pass

class Notification:
  def __init__(self, notification_id, created_on, content):
    self.__notification_id = notification_id
    self.__created_on = created_on
    self.__content = content

  # account here refers to the Account class
  def send_notification(self, account):
    pass
