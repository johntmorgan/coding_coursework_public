#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:17:11 2023

@author: johnmorgan
"""

class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def respond_invitation(self, invite):
        pass

class Interval:
    def __init__(self, start_time, end_time):
        self.__start_time = start_time
        self.__end_time = end_time

class MeetingRoom:
    def __init__(self, id, capacity, is_available):
        self.__id = id
        self.__capacity = capacity
        self.__is_available = is_available
        self.__booked_intervals = []
    
class Calendar:
    def __init__(self):
        self.__meetings = []
    
class Meeting:
    def __init__(self, id, participants_count, interval, room, subject):
        self.__id = id
        self.__participants_count = participants_count
        self.__participants = []
        self.__interval = interval
        self.__room = room
        self.__subject = subject
      
    def add_participants(self, participants):
        pass
    
class __MeetingScheduler(object):
    __instances = None

  # Scheduler is a singleton class that ensures it will have only one active instance at a time
    def __new__(cls):
        if cls.__instances is None:
            cls.__instances = super(__MeetingScheduler, cls).__new__(cls)
        return cls.__instances

class MeetingScheduler(metaclass=__MeetingScheduler):
    def __init__(self, organizer, calendar):
        self.__organizer = organizer
        self.__calendar = calendar
        self.__rooms = []

    def schedule_meeting(self, users, interval):
        pass
    def cancel_meeting(self, users, interval):
        pass
    def book_room(self, room, number_of_persons, interval):
        pass
    def release_room(self, room, interval):
        pass
    def check_rooms_availability(self, number_of_persons, interval):
        pass
    
class Notification:
    def __init__(self, notification_id, content, creation_date):
        self.__notification_id = notification_id
        self.__content = content
        self.__creation_date = creation_date
    def send_notification(self, user):
        pass
    def cancel_notification(self, user):
        pass