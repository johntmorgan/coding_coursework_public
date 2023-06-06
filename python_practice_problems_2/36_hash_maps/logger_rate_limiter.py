#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:03:25 2023

@author: johnmorgan
"""

# O(1) time complexity - hash maps!
# O(n) - number of incoming requests to store

class RequestLogger:
    def __init__(self, time_limit):
        self.log = {}
        self.time_limit = time_limit

    # This function decides whether the message request should be accepted or rejected
    def message_request_decision(self, timestamp, request):
        if request in self.log.keys():
            if timestamp - self.log[request] >= self.time_limit:
                self.log[request] = timestamp
                return True     
            else:
                return False
        else:
            self.log[request] = timestamp
            return True

rl = RequestLogger(7)
print(rl.message_request_decision(1, "good morning"))
print(rl.message_request_decision(5, "good morning"))
print(rl.message_request_decision(9, "i need coffee"))
print(rl.message_request_decision(10, "hello world"))
print(rl.message_request_decision(11, "good morning"))
print(rl.message_request_decision(15, "i need coffee"))
print(rl.message_request_decision(17, "hello world"))
print(rl.message_request_decision(25, "i need coffee"))