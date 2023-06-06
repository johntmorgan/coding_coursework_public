#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:18:17 2022

@author: johnmorgan
"""

# Copied core edit distance code
# Added code to maintain parent pointers & output edits
def edit_distance(A, B):
    x = [[None] * len(A) for _ in range(len(B))]
    x[0][0] = 0
    parent = [[None] * len(x[0]) for _ in x]
    for i in range(1, len(A)):
        x[i][0] = x[i - 1][0] + 1
    for j in range(1, len(B)):
        x[0][j] = x[0][j - 1] + 1
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i] == B[j]:
                x[i][j] = x[i - 1][j - 1]
                parent[i][j] = (i - 1, j - 1)
            else:
                ed_del = 1 + x[i - 1][j]
                ed_ins = 1 + x[i][j - 1]
                ed_rep = 1 + x[i - 1][j - 1]
                x[i][j] = min(ed_del, ed_ins, ed_rep)
                if min(ed_del, ed_ins, ed_rep) == ed_del:
                    parent[i][j] = (i - 1, j)
                elif min(ed_del, ed_ins, ed_rep) == ed_ins:
                    parent[i][j] = (i, j - 1)
                else:
                    parent[i][j] = (i - 1, j - 1)
    loc = (len(A) - 1, len(B) - 1)
    while loc != None:
        next_loc = parent[loc[0]][loc[1]]
        # print(loc, next_loc)
        if next_loc != None:
            if next_loc[0] == loc[0] - 1 and next_loc[1] == loc[1] - 1:
                if x[loc[0]][loc[1]] != x[next_loc[0]][next_loc[1]]:
                    print("Replace {} with {}".format(A[loc[0]], B[loc[0]]))
            elif next_loc[0] == loc[0] - 1:
                print("Delete {}".format(A[loc[0]]))
            else:
                print("Insert {}".format(B[loc[0]]))
        loc = next_loc
    return x[len(A) - 1][len(B) - 1]
    
A = "Hello their"
B = "Helli there"
print(edit_distance(A, B))  