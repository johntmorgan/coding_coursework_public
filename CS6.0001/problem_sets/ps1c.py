#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:00:10 2022

@author: johnmorgan
"""

portion_down_payment = 0.25
home_cost = 1000000.0
down_payment = home_cost * portion_down_payment
current_savings = 0.0
month = 0
semi_annual_raise = .07
bisection_steps = 0
low = 0.0
portion_saved = 0.5
high = 1.0
accuracy = 100.0
impossible = False

annual_salary = float(input("Enter the starting salary: "))

while abs(down_payment - current_savings) > accuracy:
    current_savings = 0.0
    current_salary = annual_salary
    for month in range(36):
        new_savings = current_salary * portion_saved / 12.0
        investment_income = current_savings * .04 / 12.0
        current_savings += new_savings + investment_income
        if (month + 1) % 6 == 0:
            current_salary += (current_salary * semi_annual_raise)
    if down_payment > current_savings:
        low = portion_saved
    else:
        high = portion_saved
    portion_saved = (low + high) / 2
    bisection_steps += 1
    if abs(1.0 - portion_saved) < .001:
        impossible = True
        break

if impossible == True:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: ", str(portion_saved))
    print("Steps in bisection search: ", str(bisection_steps))