#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:33:29 2023

@author: johnmorgan
"""

class RequestLogger:
    def __init__(self, time_limit):
        self.log = {}
        self.time_limit = time_limit
        
    def message_request_decision(self, timestamp, request):
        if request not in self.log:
            self.log[request] = timestamp
            return True
        else:
            last = self.log[request]
            if timestamp - last < self.time_limit:
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
