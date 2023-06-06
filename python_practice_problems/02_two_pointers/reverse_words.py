#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:43:52 2023

@author: johnmorgan
"""

def reverse_words(sentence):
    sent = [*sentence.strip()]
    sent.reverse()
    start, end = 0, 0
    while start < len(sent):
        while sent[end] != " " and end < len(sent) - 1:
            end += 1
        next_word_index = end + 1
        if next_word_index < len(sent):
            while sent[next_word_index] == " ":
                sent = sent[0:next_word_index] + sent[next_word_index + 1:len(sent)]
        if sent[end] == " ":
            end -= 1
        while end > start:
            sent[start], sent[end] = sent[end], sent[start]
            start += 1
            end -= 1
        start, end = next_word_index, next_word_index
    return "".join(sent)

# def reverse_words(sentence):
#     sent = [*sentence.strip()]
#     sent.reverse()
#     start, end = 0, 0
#     while start < len(sent) and end < len(sent):
#         if sent[end] != " ":
#             end += 1
#         else:
#             left, right = start, end - 1
#             while left < right:
#                 sent[left], sent[right] = sent[right], sent[left]
#                 left += 1
#                 right -= 1
#             if end < len(sent):
#                 end += 1
#                 while sent[end] == " ":
#                     sent = sent[:end] + sent[end + 1:]
#             start = end
#     if start != end:
#         left, right = start, end - 1
#         while left < right:
#             sent[left], sent[right] = sent[right], sent[left]
#             left += 1
#             right -= 1
#         if end < len(sent):
#             end += 1
#             while sent[end] == " ":
#                 sent = sent[:end] + sent[end + 1:]
#         start = end
#     output = "".join(sent)
#     return output

# def reverse_words_simple(sentence):
#     arr = sentence.split(" ")
#     arr[:] = [val for val in arr if val != ""]
#     arr.reverse()
#     output = " ".join(arr)
#     return output

sentence = "Hello     World"
print(reverse_words(sentence))