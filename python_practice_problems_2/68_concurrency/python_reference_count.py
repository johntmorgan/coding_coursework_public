#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:18:16 2023

@author: johnmorgan
"""

import sys

# declare a variable
some_var = "Educative"

# check reference count
print(sys.getrefcount(some_var))

# create another refrence to someVar
another_var = some_var

# verify the incremented reference count
print(sys.getrefcount(some_var))