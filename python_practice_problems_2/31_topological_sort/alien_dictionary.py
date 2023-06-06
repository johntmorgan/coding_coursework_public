#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:39:31 2023

@author: johnmorgan
"""

from collections import defaultdict, Counter, deque

def alien_order(words):
    letter_graph = {}
    for word_index in range(len(words)):
        letter = words[word_index][0]
        later_letters = []
        same_start_words = []
        for index in range(word_index, len(words)):
            if words[index][0] != letter and words[index][0] not in later_letters:
                later_letters.append(words[index][0])
            elif words[index][0] == letter and words[word_index] != words[index]:
                same_start_words.append([words[word_index], words[index]])
        if letter in letter_graph.keys():
            for new_letter in later_letters:
                if new_letter not in letter_graph[letter]:
                    letter_graph[letter] = letter_graph[letter] + [new_letter]   
        else:
            letter_graph[letter] = later_letters
        if len(same_start_words) > 0:
            for comparison in same_start_words:
                if len(comparison[0]) > len(comparison[1]) and \
                    comparison[0][:len(comparison[1])] == comparison[1]:
                        return ""
                min_length = float('inf')
                for word in comparison:
                    if len(word) < min_length:
                        min_length = len(word)
                same_prefix, index = False, 0
                while index < min_length and same_prefix == False:
                    if comparison[0][index] == comparison[1][index]:
                        index += 1
                    else:
                        if comparison[0][index] in letter_graph:
                            if comparison[1][index] not in letter_graph[comparison[0][index]]:
                                letter_graph[comparison[0][index]] = \
                                letter_graph[comparison[0][index]] + \
                                [comparison[1][index]]
                        else:
                            letter_graph[comparison[0][index]] = \
                            [comparison[1][index]]
                        same_prefix = True
    for word in words:
        for letter in word:
            if letter not in letter_graph.keys():
                letter_graph[letter] = []
    all_letters = letter_graph.keys()
    indegrees = {}
    for key, value in letter_graph.items():
        if key not in indegrees:
            indegrees[key] = 0
        for child in value:
            if child not in indegrees:
                indegrees[child] = 1
            else:
                indegrees[child] = indegrees[child] + 1
    sources = deque()
    for key, val in indegrees.items():
        if val == 0:
            sources.append(key)
    order = []
    while len(sources) > 0:
        visit = sources.popleft()
        order += [visit]
        children = letter_graph[visit]
        for child in children:
            indegrees[child] = indegrees[child] - 1
            if indegrees[child] == 0:
                sources.append(child)
    for letter in all_letters:
        if letter not in order:
            return ""
    return "".join(order)

# Better, shorter course code
# Review
# Consider adjacent words one at a time. When they don't match, add to graph
# If all match, check if prefix of each other

# O(c) where c is the length of all words in the dictionary added together
# Space complexity O(1) - fixed number of letters can be in graph

def alien_order(words):
    adj_list = defaultdict(set)
    counts = Counter({c: 0 for word in words for c in word})
    outer = 0
    for word1, word2 in zip(words, words[1:]):
        outer += 1
        inner = 0
        for c, d in zip(word1, word2):
            inner += 1
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    counts[d] += 1
                break
        else:  
            if len(word2) < len(word1):
                return ""
    result = []
    sources_queue = deque([c for c in counts if counts[c] == 0])
    while sources_queue:
        c = sources_queue.popleft()
        result.append(c)
        for d in adj_list[c]:
            counts[d] -= 1
            if counts[d] == 0:
                sources_queue.append(d)
    if len(result) < len(counts):
        return ""
    return "".join(result)


words = ["xro","xma","per","prt","oxh","olv"]
print(alien_order(words))

words = ["mdx", "mars", "avgd", "dkae"]
print(alien_order(words))

words = ["m", "mx", "mxe", "mxer", "mxerl", "mxerlo", "mxerlos", "mxerlost", "mxerlostr", "mxerlostrpq", "mxerlostrp"]
print(alien_order(words))