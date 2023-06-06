#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:37:06 2023

@author: johnmorgan
"""

class AccountStatus(enum.Enum):
  ACTIVE = 1 
  BLOCKED = 2
  DISABLED = 3

class QuestionStatus(enum.Enum):
  ACTIVE = 1
  CLOSED = 2
  FLAGGED = 3
  BOUNTIED = 4

class ClosingDetail(enum.Enum):
  COMMUNITY_SPECIFIC_REASON = 1
  DUPLICATE = 2
  NEEDS_CLARITY = 3 
  NEEDS_MORE_FOCUS = 4 
  OPINION_BASED = 5
  
from abc import ABC, abstractmethod

class Search(ABC):
  def search_by_tags(self, name):
    pass
  def search_by_users(self, name):
    pass
  def search_by_words(self, words):
    pass

class SearchCatalog(Search):
  def __init__(self):
    self.__questions_using_tags = {}
    self.__questions_using_users = {}
    self.__questions_using_words = {}

  def search_by_tags(self, name):
    # functionality
    pass
  def search_by_users(self, name):
    # functionality
    pass
  def search_by_words(self, words):
    # functionality
    pass
  
class Account:
  def __init__(self, account_id, password, username, name, email, phone, status):
    self.__account_id = account_id
    self.__password = password
    self.__username = username
    self.__name = name
    self.__email = email
    self.__phone = phone
    self.__status = status # Refers to the AccountStatus enum

  def reset_password(self):
    pass

from abc import ABC

class User(ABC):
  def __init__(self, reputation_points, account):
    self.__reputation_points = reputation_points;
    self.__account = account;
    self.__badges = []

  def create_question(self, question):
    pass
  def add_answer(self, answer):
    pass
  def create_comment(self, comment):
    pass
  def create_tag(self, tag):
    pass
  def flag_question(self, question):
    pass
  def flag_answer(self, answer):
    pass
  def upvote(self, id):
    pass
  def downvote(self, id):
    pass
  def vote_to_close_question(self, question):
    pass
  def vote_to_delete_question(self, question):
    pass
  def accept_answer(self, answer):
    pass

class Admin(User):
  def __init__(self, reputation_points, account):
    super().__init__(reputation_points, account)

  def block_user(self, user):
    pass
  def unblock_user(self, user):
    pass
  def award_badge(self, user, badge):
    pass

class Moderator(User):
  def __init__(self, reputation_points, account):
    super().__init__(reputation_points, account)

  def close_question(self, question):
    pass
  def reopen_question(self, question):
    pass
  def delete_question(self, question):
    pass
  def restore_question(self, question):
    pass
  def delete_answer(self, answer):
    pass

class Guest:
  def register_account(self):
    pass

class Question:
  def __init__(self, id, title, content, view_count, vote_count, score,
               upvotes, downvotes, creation_date, modification_date, status,
               closing_reason, created_by, bounty):
    self.__id = id
    self.__title = title
    self.__content = content
    self.__view_count = view_count
    self.__vote_count = vote_count
    self.__score = score
    self.__upvotes = upvotes
    self.__downvotes = downvotes
    self.__creation_date = creation_date
    self.__modification_date = modification_date
    self.__closing_reason = closing_reason
    self.__created_by = created_by
    self.__bounty = bounty
    
    self.__tags = []
    self.__comments = []
    self.__answers = []
    self.__followers = []
  
  def add_comment(self, comment):
    pass
  def add_bounty(self, bounty):
    pass

class Comment:
  def __init__(self, id, content, flag_count, upvotes, creation_date, user):
    self.__id = id
    self.__content = content
    self.__flag_count = flag_count
    self.__upvotes = upvotes
    self.__creation_date = creation_date
    self.__postedBy = user

class Answer:
  def __init__(self, id, content, flag_count, vote_count, upvotes,
               downvotes, is_available, creation_date, user):
    self.__id = id
    self.__content = content
    self.__flag_count = flag_count
    self.__vote_count = vote_count
    self.__upvotes = upvotes
    self.__downvotes = downvotes
    self.__is_accepted = False
    self.__creation_date = creation_date
    self.__postedBy = user
  
    self.__comments = []
    self.__followers = []

  def addComment(self, comment):
    pass

class Bounty:
  def __init__(self, reputation_points, expiry_date):
    self.__reputation_points = reputation_points
    self.__expiry_date = expiry_date
  
  def update_reputation_points(self, reputation):
    pass

class Badge:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

class Tag:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

class TagList:
    def __init__(self):
        self.__tags_count = {}
    
    def increment_tag_count():
        pass
    def decrement_tag_count():
        pass
    
class Notification:
  def __init__(self, notification_id, created_on, content):
    self.__notification_id = notification_id
    self.__created_on = created_on
    self.__content = content

  # account here refers to the Account class
  def send_notification(self, account):
    pass