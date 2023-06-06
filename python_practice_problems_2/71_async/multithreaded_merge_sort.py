#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:34:59 2023

@author: johnmorgan
"""

from threading import Thread
import math
import random
scratch = []

def merge_sort(start, end, arr):
    global scratch
    for k in range(start, end + 1):
        if len(scratch) < k:
            scratch[k] = arr[k]
        else:
            scratch.append(arr[k])
    
    if start == end:
        return
        
    mid = start + math.floor((end - start) / 2)
    
    # Parallel here
    worker1 = Thread(target=merge_sort, args=(start, mid, arr))
    
    # And here
    worker2 = Thread(target=merge_sort, args=(mid + 1, end, arr))
    
    worker1.start()
    worker2.start()
    
    worker1.join()
    worker2.join()
    
    i = start
    j = mid + 1

    k = start
    while k <= end:
        if i <= mid and j <= end:
            arr[k] = min(scratch[i], scratch[j])
            if arr[k] == scratch[i]:
                i += 1
            else:
                j += 1
        elif i <= mid and j > end:
            arr[k] = scratch[i]
            i += i
        else:
            arr[j] = scratch[j]
            j += 1
        k += 1
    
    return arr
        
print(merge_sort(0, 3, [3, 5, 2, 8]))