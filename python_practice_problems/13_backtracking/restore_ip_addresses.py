#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:42:41 2023

@author: johnmorgan
"""

# Review, first solution was inefficient

def is_valid(segment):
    if len(segment) > 3:
        return False
    if int(segment) > 255:
        return False
    if len(segment) > 1 and segment[0] == "0":
        return False
    return True

def test_segments(s, result, segments, curr_pos):
    last_seg = s[curr_pos + 1:]
    if is_valid(last_seg):
        segments.append(last_seg)
        result.append(".".join(segments))
        segments.pop()

def recurse_segment(s, result, segments, prev_pos, dots):
    for curr_pos in range(prev_pos + 1, min(len(s) - 1, prev_pos + 4)):
        segment = s[prev_pos + 1:curr_pos + 1]
        if is_valid(segment):
            segments.append(segment)
            if dots == 1:
                test_segments(s, result, segments, curr_pos)
            else:
                recurse_segment(s, result, segments, curr_pos, dots - 1)
            segments.pop()
        
def restore_ip_addresses(s):
    result, segments = [], []
    recurse_segment(s, result, segments, -1, 3)
    return result


s = "00000000"
print(restore_ip_addresses(s))

s = "255255255255"
print(restore_ip_addresses(s))

s = "12121212"
print(restore_ip_addresses(s))


# Wildly inefficient solution

# def valid_ip_address(s, dot_locs):
#     first_val = s[:dot_locs[0]]
#     second_val = s[dot_locs[0]:dot_locs[1]]
#     third_val = s[dot_locs[1]:dot_locs[2]]
#     fourth_val = s[dot_locs[2]:]
#     if int(first_val) > 255 or (len(first_val) > 1 and first_val[0] == "0") or \
#         len(first_val) > 3:
#         return False
#     if int(second_val) > 255 or (len(second_val) > 1 and second_val[0] == "0") or \
#         len(second_val) > 3:
#         return False
#     if int(third_val) > 255 or (len(third_val) > 1 and third_val[0] == "0")  or \
#         len(third_val) > 3:
#         return False
#     if int(fourth_val) > 255 or (len(fourth_val) > 1 and fourth_val[0] == "0")  or \
#         len(fourth_val) > 3:
#         return False
#     return True

# def convert_address(s, dot_locs):
#     first_val = s[:dot_locs[0]]
#     second_val = s[dot_locs[0]:dot_locs[1]]
#     third_val = s[dot_locs[1]:dot_locs[2]]
#     fourth_val = s[dot_locs[2]:]
#     return first_val + "." + second_val + "." + third_val + "." + fourth_val

# def recurse_string(s, result, dot_locs, counter):
#     counter[0] += 1
#     if valid_ip_address(s, dot_locs):
#         if convert_address(s, dot_locs) not in result:
#             result.append(convert_address(s, dot_locs))
#     if dot_locs[2] == len(s) and dot_locs[1] == len(s) - 1 and \
#         dot_locs[0] == len(s) - 2:
#         return
#     else:
#         if dot_locs[1] - dot_locs[0] > 1:
#             dot_locs[0] += 1
#             recurse_string(s, result, dot_locs, counter)
#             dot_locs[0] -= 1
#         if dot_locs[2] - dot_locs[1] > 1 and dot_locs[1] - dot_locs[0] < 3:
#             dot_locs[1] += 1
#             recurse_string(s, result, dot_locs, counter)
#             dot_locs[1] -= 1 
#         if dot_locs[2] < len(s) - 1 and dot_locs[2] - dot_locs[1] < 3:
#             dot_locs[2] += 1
#             recurse_string(s, result, dot_locs, counter)
#             dot_locs[2] -= 1

# def restore_ip_addresses(s):
#     result = []
#     dot_locs = [1,2,3]
#     counter = [0]
#     recurse_string(s, result, dot_locs, counter)
#     print(counter[0])
#     result.sort()
#     return result

# Review O(n) solution

def valid(segment):
    segment_length = len(segment)
    if segment_length > 3:
        return False
    return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

def update_segment(s, curr_pos, segments, result):
    segment = s[curr_pos + 1:len(s)]
    if valid(segment):
        segments.append(segment)
        result.append('.'.join(segments))
        segments.pop()

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