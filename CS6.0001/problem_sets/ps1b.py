#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:54:45 2022

@author: johnmorgan
"""

portion_down_payment = 0.25
current_savings = 0.0
month = 0

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion saved: "))
home_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

current_salary = annual_salary
down_payment = home_cost * portion_down_payment

while current_savings < down_payment:
    new_savings = current_salary * portion_saved / 12
    investment_income = current_savings * .04 /12
    current_savings = current_savings + new_savings + investment_income
    month = month + 1
    if month % 6 == 0:
        current_salary = current_salary + current_salary * semi_annual_raise

print("Number of months: ", str(month))