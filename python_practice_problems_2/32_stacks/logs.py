#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 18:04:48 2023

@author: johnmorgan
"""

class Log:
    def __init__(self, content):
        content = content.replace(' ', '')
        content = content.split(":")
        self.id = int(content[0])
        self.is_start = content[1] == "start"
        self.time = int(content[2])