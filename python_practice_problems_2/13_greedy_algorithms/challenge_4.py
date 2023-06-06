#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:49:17 2023

@author: johnmorgan
"""

def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of arrival Timing
    :param departure: A list of departure Timing
    :return: Minimum number of platforms required for a railway Station
    """
    time = 900
    end_time = 2000
    trains = 0
    max_trains = 0
    while time < end_time:
        if len(arrival) > 0 and arrival[0] == time:
            arrival.pop(0)
            trains += 1
        while time in departure:
            departure.pop(departure.index(time))
            trains -= 1
        if int(str(time)[-2:]) < 50:  
            time += 10
        else:
            time = int(str(int(str(time)[:-2]) + 1) + "00")
        if trains > max_trains:
            max_trains = trains
    return max_trains

# Brute force solution O(n^2)
# Review

def find_platform(arrival, departure):
    result = 0
    count = 0
    n = len(arrival)

    for index in range(n):
        count = 0
        for i in range(1, n):
            if arrival[index] <= arrival[i] <= departure[index]:
                count += 1
        if result < count:
            result = count
    return result

# O(nlogn), greedy - review!
# I wanted to avoid O(nlogn) sort - JM

def find_platform(arrival, departure):
    # Sort arrival and departure lists
    n = len(arrival) # Length of the arrival list
    arrival.sort()
    departure.sort()

    # plat_needed indicates number of platforms needed at a time
    plat_needed = 1
    result = 1
    i = 1
    j = 0

    # Similar to merge in merge sort to process all events in sorted order
    while i < n and j < n:

        # If next event in sorted order is arrival, increment count of platforms needed
        if arrival[i] < departure[j]:

            plat_needed += 1
            i += 1

            # Update result if needed
            if plat_needed > result:
                result = plat_needed

        # Else decrement count of platforms needed
        else:
            plat_needed -= 1
            j += 1

    return result

arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
print(find_platform(arrival, departure))