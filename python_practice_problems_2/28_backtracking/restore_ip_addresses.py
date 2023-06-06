#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:25:45 2023

@author: johnmorgan
"""

def is_valid(s, dots):
    seg1_valid, seg2_valid, seg3_valid, seg4_valid = False, False, False, False
    seg1 = s[0:dots[0]]
    seg2 = s[dots[0]:dots[1]]
    seg3 = s[dots[1]:dots[2]]
    seg4 = s[dots[2]:len(s)]
    if 0 <= int(seg1) <= 255 and seg1 != "00" and seg1 != "000" and \
        len(seg1) <= 3 and (int(seg1) == 0 or seg1[0] != "0"):
        seg1_valid = True
    if 0 <= int(seg2) <= 255 and seg2 != "00" and seg2 != "000" and \
        len(seg2) <= 3 and (int(seg2) == 0 or seg2[0] != "0"):
        seg2_valid = True
    if 0 <= int(seg3) <= 255 and seg3 != "00" and seg3 != "000" and \
        len(seg3) <= 3 and (int(seg3) == 0 or seg3[0] != "0"):
        seg3_valid = True
    if 0 <= int(seg4) <= 255 and seg4 != "00" and seg4 != "000" and \
        len(seg4) <= 3 and (int(seg4) == 0 or seg4[0] != "0"):
        seg4_valid = True
    return seg1_valid and seg2_valid and seg3_valid and seg4_valid

def str_process(s, dots):
    seg1 = s[0:dots[0]]
    seg2 = s[dots[0]:dots[1]]
    seg3 = s[dots[1]:dots[2]]
    seg4 = s[dots[2]:len(s)]
    return s[0:dots[0]] + "." + s[dots[0]:dots[1]] + "." + \
           s[dots[1]:dots[2]] +  "." + s[dots[2]:len(s)]

def ria_recurse(s, result, dots):
    if is_valid(s, dots):
        new_ip = str_process(s, dots)
        if new_ip not in result:
            result += [str_process(s, dots)]
    seg1 = s[0:dots[0]]
    seg2 = s[dots[0]:dots[1]]
    seg3 = s[dots[1]:dots[2]]
    seg4 = s[dots[2]:len(s)]
    if int(seg1) > 255 or seg1 == "00" or seg1 == "000":
        return
    elif int(seg2) > 255 or seg2 == "00" or seg2 == "000":
        ria_recurse(s, result, [dots[0] + 1, dots[1], dots[2]])
    elif int(seg3) > 255 or seg3 == "00" or seg3 == "000":
        ria_recurse(s, result, [dots[0], dots[1] + 1, dots[2]])
    elif int(seg4) > 255 or seg4 == "00" or seg4 == "000":
        if dots[2] < len(s) - 1:
            ria_recurse(s, result, [dots[0], dots[1], dots[2] + 1])
        else:
            return
    else:
        if dots[0] < 3 and dots[1] - dots[0] > 1:
            ria_recurse(s, result, [dots[0] + 1, dots[1], dots[2]])
        if  dots[2] - dots[1] > 1:
            ria_recurse(s, result, [dots[0], dots[1] + 1, dots[2]])
        if len(s) - dots[2] > 1:
            ria_recurse(s, result, [dots[0], dots[1], dots[2] + 1])

def restore_ip_addresses(s):
    result = []
    dots = [1, 2, 3]
    ria_recurse(s, result, dots)
    result.sort()
    return result

# Course solution
# Time complexity O(1), only 27 combinations to check
# Space O(1), can have 19 valid IP addresses max

def valid(segment):
    if len(segment) > 3:  # each segment's length should be less than 3
        return False
    return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1


def update_segment(s, curr_pos, segments, result):
    segment = s[curr_pos + 1:len(s)]
    if valid(segment):  # if the segment is acceptable
        segments.append(segment)  # add it to the list of segments
        result.append('.'.join(segments))
        segments.pop()  # remove the top segment


def backtrack(s, prev_pos, dots, segments, result):
    size = len(s)
    for curr_pos in range(prev_pos + 1, min(size - 1, prev_pos + 4)):
        segment = s[prev_pos + 1:curr_pos + 1]
        if valid(segment):
            segments.append(segment)
            if dots - 1 == 0:
                update_segment(s, curr_pos, segments, result)
            else:
                backtrack(s, curr_pos, dots - 1, segments, result)
            segments.pop()

def restore_ip_addresses(s):
    result, segments = [], []
    backtrack(s, -1, 3, segments, result)
    return result


ip_raw = "12121212"
print(restore_ip_addresses(ip_raw))

ip_raw = "00000000"
print(restore_ip_addresses(ip_raw))

ip_raw = "010010"
print(restore_ip_addresses(ip_raw))

ip_raw = "201023"
print(restore_ip_addresses(ip_raw))
