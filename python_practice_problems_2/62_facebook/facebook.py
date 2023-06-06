#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:27:13 2023

@author: johnmorgan
"""

from abc import ABC, abstractmethod
from enum import Enum

class Address:
    def __init__(self, zip_code, house_no, city, state, country):
       self.__zip_code = zip_code
       self.__house_no = house_no
       self.__city = city
       self.__state = state
       self.__country = country

class AccountStatus(Enum):
    ACTIVE = 1 
    BLOCKED = 2
    DISABLED = 3
    DELETED = 4

class FriendInviteStatus(Enum):
    PENDING = 1 
    ACCEPTED = 2
    REJECTED = 3
    CANCELED = 4

class PostPrivacySettings(Enum):
    PUBLIC = 1 
    FRIENDS_OF_FRIENDS = 2
    ONLY_FRIENDS = 3
    CUSTOM = 4

class PageFunctionsByUser(ABC):
    def create_page(self, name):
        pass
    def share_page(self, page):
        pass
    def like_page(self, page):
        pass
    def follow_page(self, page):
        pass
    def unLike_page(self, page):
        pass
    def unFollow_page(self, page):
        pass
    
class GroupFunctions(ABC):
    def add_user(self, user):
        pass
    def delete_user(self, user):
        pass
    def notify_user(self, user):
        pass

    def create_group(self, name):
        pass
    def join_group(self, group):
        pass
    def leave_group(self, group):
        pass
    def send_group_invite(self, group):
        pass

class PostFunctionsByUser(ABC):
    def create_post(self, content):
        pass
    def share_post(self, post):
        pass
    def comment_on_post(self, post):
        pass
    def like_post(self, post):
        pass

class CommentFunctionsByUser(ABC):
    def create_comment(self, post, content):
        pass
    def like_comment(self, comment):
      pass

class Account:
    def __init__(self, account_id, password, username, email, status):
        self.__account_id = account_id
        self.__password = password
        self.__username = username
        self.__email = email
        self.__status = status # Refers to the AccountStatus enum

    def reset_password(self):
        pass

class Admin:  
    def block_user(self, user):
        pass
    def unblock_user(self, user):
        pass
    def enable_page(self, page):
        pass
    def disable_page(self, page):
        pass
    def delete_group(self, group):
        pass
    def change_group_privacy(self, group):
        pass

class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account

# Will be using only one interface example
class User(Person, PageFunctionsByUser):
    def __init__(self, name, address, email, phone, account, user_id,
                 date_of_joining, is_admin, profile):
        self.__name = name
        self.__user_id = user_id;
        self.__date_of_joining = date_of_joining
        self.__profile = profile
        # The following lists contain the pages and groups that a user is admin of
        self.__pages_admin = []
        self.__groups_admin = []    
        super().__init__(name, address, email, phone, account)
  
    def send_message(self, message):
        pass
    def send_recommendation(self, page, group, user):
        pass    
    def send_friend_request(self, user):
        pass
    def unfriend_user(self, user):
        pass
    def block_user(self, user):
        pass
    def follow_user(self, user):
        pass

  # The functions of the different interfaces will be present here
    def create_page(self, name):
    # functionality
        pass
    def like_page(self, page):
    # functionality
        pass
    def follow_page(self, page):
    # functionality
        pass
    def unLike_page(self, page):
    # functionality
       pass
    def unFollow_page(self, page):
    # functionality
        pass
    def share_page(self, page):
    # functionality
        pass
    
class Profile:
    def __init__(self, gender, profile_picture, cover_photo):
        self.__gender = gender
        self.__profile_picture = profile_picture
        self.__cover_photo = cover_photo
        self.__friends = []
        self.__users_followed = [];
        self.__pages_followed = [];
        self.__groups_joined = [];
        self.__work_experience = [];
        self.__education_info = [];
        self.__places = [];

    def add_work_experience(self, work):
        pass
    def add_education(self, education):
        pass
    def add_place(self, place):
        pass
    def add_profile_picture(self, image):
        pass
    def add_cover_photo(self, image):
        pass
    def add_gender(self, gender):
        pass

class Work:
    def __init__(self, title, company, location, description, start_date,
                 end_date):
        self.__title = title
        self.__company = company
        self.__location = location
        self.__description = description
        self.__start_date = start_date
        self.__end_date = end_date

class Places:
    def __init__(self, name):
        self.__name = name

class Education:
    def __init__(self, school, degree, description, start_date, end_date):
        self.__school = school
        self.__degree = degree
        self.__description = description
        self.__start_date = start_date
        self.__end_date = end_date

class Page:
    def __init__(self, page_name, page_id, description, like_count):
       self.__page_id = page_id
       self.__page_name = page_name
       self.__description = description
       self.__like_count = like_count

class Post:
    def __init__(self, post_id, content, image, like_count, share_count,
               post_owner, settings):
        self.__post_id = post_id
        self.__content = content
        self.__image = image
        self.__like_count = like_count
        self.__share_count = share_count
        self.__post_owner = post_owner
        self.__settings = settings # Refers to the PostPrivacySettings enum
  
    def change_post_visibility(self, post):
        pass

class Comment:
    def __init__(self, comment_id, content, like_count, comment_owner):
        self.__comment_id = comment_id
        self.__content = content
        self.__like_count = like_count
        self.__comment_owner = comment_owner

class ProfilePrivacy:
    def change_friends_list_visibility(self, profile):
        pass
    def lock_profile(self, profile):
        pass
    def lock_profile_picture(self, profile):
        pass

class GroupFunctions:
    def add_user(self, user):
        pass
    def delete_user(self, user):
        pass
    def notify_user(self, user):
        pass

class Group(GroupFunctions):
    def __init__(self, group_id, name, description, cover_photo, total_users,
                 is_private):
        self.__group_id = group_id
        self.__name = name
        self.__description = description
        self.__cover_photo = cover_photo
        self.__total_users = total_users
        self.__is_private = is_private
        self.__users = []

    def add_user(self, user):
        # functionality
        pass

    def delete_user(self, user):
        # functionality
        pass

    def notify_user(self, user):
        # functionality
        pass

    def update_description(self, description):
        pass

    def add_cover_photo(self, image):
        pass

class Message:
    def __init__(self, message_id, sender, content, recipient, multimedia):
        self.__message_id = message_id
        self.__sender = sender
        self.__content = content
        self.__recipient = []
        self.__multimedia = []
        
  # user here refers to a list of users
    def add_recipient(self, user):
        pass
    
class FriendRequest:
    def __init__(self, recipient, sender, status, request_sent,
                 request_status_modified):
        self.__recipient = recipient
        self.__sender = sender
        self.__status = status
        self.__request_sent = request_sent
        self.__request_status_modified = request_status_modified

    def accept_request(self, user):
        pass

    def reject_request(self, user):
        pass

class Notification:
    def __init__(self, notification_id, created_on, content):
        self.__notification_id = notification_id
        self.__created_on = created_on
        self.__content = content

  # account here refers to the Account class
    def send_notification(self, account):
        pass
    
class Search(ABC):
    def search_users(self, name):
        pass
    def search_groups(self, name):
        pass
    def search_pages(self, name):
        pass
    def search_posts(self, keywords):
      pass

class SearchCatalog(Search):
    def __init__(self):
        self.__user_names = {}
        self.__group_names = {}
        self.__page_titles = {}
        self.__posts = {}

    def add_new_user(self, user):
        pass
    def add_new_group(self, group):
        pass
    def add_new_page(self, page):
        pass
    def add_new_post(self, post):
        pass

    def search_users(self, name):
        # functionality
        pass
    def search_groups(self, name):
        # functionality
        pass
    def search_pages(self, name):
        # functionality
        pass
    def search_posts(self, keywords):
        # functionality
        pass