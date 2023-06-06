#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:55:21 2023

@author: johnmorgan
"""

# O(nlogn) cheese - JM

def convertMax(maxHeap):
    maxHeap.sort()
    return maxHeap

# O(n) - rebuild min_heap

def percolate_up(minHeap, index):
    parent = (index-1)//2
    if index <= 0:
        return
    elif minHeap[parent] > minHeap[index]:
        tmp = minHeap[parent]
        minHeap[parent] = minHeap[index]
        minHeap[index] = tmp
        percolate_up(minHeap, parent)

def convertMax(maxHeap):
    minHeap = []
    for elem in maxHeap:
        minHeap.append(elem)
        percolate_up(minHeap, len(minHeap) - 1)
    return minHeap

# O(n) course solution - min heapify all parent nodes

def minHeapify(heap, index):
    left = index * 2 + 1
    right = index * 2 + 2
    smallest = index
    if len(heap) > left and heap[smallest] > heap[left]:
        smallest = left
    if len(heap) > right and heap[smallest] > heap[right]:
        smallset = right
    if smallest != index:
        tmp = heap[smallest]
        heap[smallest] = heap[index]
        heap[index] = tmp
        minHeapify(heap, smallest)
    return heap

def convertMax(maxHeap):
    for i in range((len(maxHeap))//2, -1, -1):
        maxHeap = minHeapify(maxHeap, i)
    return maxHeap

maxHeap = [9,4,7,1,-2,6,5]
print(convertMax(maxHeap))