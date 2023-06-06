#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:49:40 2023

@author: johnmorgan
"""

import random


class RandomPickWithWeight:

    def __init__(self, w):
        self.running_sums = []
        for index in range(len(w)):
            if self.running_sums == []:
                self.running_sums.append(w[index])
            else:
                self.running_sums.append(w[index] + self.running_sums[index - 1])

    def pick_index(self):
        num = random.randrange(self.running_sums[len(self.running_sums) - 1])
        low = 0
        high = len(self.running_sums) - 1
        while low <= high:
            mid = (low + high) // 2
            if mid < len(self.running_sums) - 1:
                if self.running_sums[mid] <= num and self.running_sums[mid + 1] > num:
                    return mid + 1
            if mid == len(self.running_sums) - 1:
                return len(self.running_sums) - 1
            if self.running_sums[mid] <= num:
                low = mid + 1
            else:
                high = mid - 1
        return mid

# weights = [10, 20, 30, 40, 50]
# sol = RandomPickWithWeight(weights)
# index = sol.pick_index()
# print(sol.running_sums)
# print(index)

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
