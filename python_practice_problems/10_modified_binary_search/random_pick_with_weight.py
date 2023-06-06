#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:50:11 2023

@author: johnmorgan
"""

import random


class RandomPickWithWeight:

    def __init__(self, w):
        self.rsum = [w[0]]
        for w_index in range(1, len(w)):
            self.rsum.append(self.rsum[w_index - 1] + w[w_index])
        

    def pick_index(self):
        target = random.randint(1, self.rsum[len(self.rsum) - 1])
        low = 0
        high = len(self.rsum) - 1
        while low <= high:
            mid = (low + high) // 2
            if mid > 0 and (self.rsum[mid] > target and self.rsum[mid - 1] <= target):
                return mid
            if mid == 0 and target <= self.rsum[0]:
                return mid
            if self.rsum[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return 0

# Driver code


def main():
    counter = 900
    weights1 = [1, 2, 3, 4, 5]
    weights2 = [1, 12, 23, 34, 45, 56, 67, 78, 89, 90]
    weights3 = [10, 20, 30, 40, 50]
    weights4 = [1, 10, 23, 32, 41, 56, 62, 75, 87, 90]
    weights5 = [12, 20, 35, 42, 55]
    weights6 = [10, 10, 10, 10, 10]
    weights7 = [10, 10, 20, 20, 20, 30]
    weights8 = [1, 2, 3]
    weights9 = [10, 20, 30, 40]
    weights10 = [5, 10, 15, 20, 25, 30]
    weights = [weights1, weights2, weights3, weights4, weights5,
                weights6, weights7, weights8, weights9, weights10]
    dict = {}
    for i in range(len(weights)):
        print(i + 1, ".\tInput: ", weights[i], ", pick_index() called ", counter, " times", "\n", sep="")
        [dict.setdefault(l, 0) for l in range(len(weights[i]))]
        for j in range(counter):
            sol = RandomPickWithWeight(weights[i])
            index = sol.pick_index()
            dict[index] += 1
        print("-"*95)
        print("{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<15}{:<5}{:<15}".format( \
            "Indexes", "|", "Weights", "|", "Occurences", "|", "Frequency", "|", "Expected Frequency"))
        print("-"*95)
        for key, value in dict.items():

            print("{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<15}{:<5}{:<15}".format(key, "|", weights[i][key], "|", value, "|", \
                str(round((value/counter)*100, 2)) + "%", "|", str(round(weights[i][key]/sum(weights[i])*100, 2))+"%"))
        dict = {}
        print("\n", "-"*100, "\n", sep="")


if __name__ == '__main__':
    main()