#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:35:57 2022

@author: johnmorgan
"""

class PriorityQueue:
    def __init__(self):
        self.A = []
    
    def insert(self, x):
        self.A.append(x)
    
    def delete_max(self):
        if len(self.A) < 1:
            raise IndexError('pop from empty priority queue')
        return self.A.pop()
    
    @classmethod
    def sort(Queue, A):
        pq = Queue()
        for x in A:
            pq.insert(x)
        out = [pq.delete_max() for _ in A]
        out.reverse()
        return out
    
class PQ_Array(PriorityQueue):
    def delete_max(self):
        n, A, m = len(self.A), self.A, 0
        for i in range(1, n):
            if A[m].key < A[i].key:
                m = i
        A[m], A[n] = A[n], A[m]
        return super().delete_max()
    
class PQ_SortedArray(PriorityQueue):
    def insert(self, *args):
        super().insert(*args)
        i, A = len(self.A) - 1, self.A
        while 0 < i and A[i + 1].key < A[i].key:
            A[i + i], A[i] = A[i], A[i + 1]
            i -= 1

def parent(i):
    p = (i - 1) // 2
    return p if 0 < i else i

def left(i, n):
    l = 2 * i + 1
    return l if l < n else i

def right(i, n):
    r = 2 * i + 2
    return r if r < n else i

def max_heapify_up(A, n, c):
    p = parent(c)
    if A[p].key < A[c].key:
        A[c], A[p] = A[p], A[c]
        max_heapify_up(A, n, p)
    
def max_heapify_down(A, n, p):
    l, r = left(p, n), right(p, n)
    c = l if A[r].key < A[l].key else r
    if A[p].key < A[c].key:
        A[c], A[p] = A[p], A[c]
        max_heapify_down(A, n, c)

def build_max_heap(A):
    n = len(A)
    for i in range(n // 2, -1, -1): # O(n) loop backward over array
        max_heapify_down(A, n, i) # O(log n - log i)) fix max heap
           
class PQ_Heap(PriorityQueue):
    def insert(self, *args): # O(log n)
        super().insert(*args) # append to end of array
        n, A = self.n, self.A
        max_heapify_up(A, n, n - 1)
    
    def delete_max(self): # O(log n)
        n, A = self.n, self.A
        A[0], A[n] = A[n], A[0]
        max_heapify_down(A, n, 0)
        return super().delete_max() # pop from end of array
    
# Heap sort in place
# Works for sorting any subclass - PQ_Array, PQ_SortedArray, PQ_Heap
class PriorityQueue:
    def __init__(self, A):
        self.n, self.A = 0, A
    
    def insert(self): 
        if not self.n < len(self.A): # absorb element A[n] into the queue
            raise IndexError('insert into full priority queue')
        self.n += 1
    
    def delete_max(self): # remove element A[n - 1] from the queue
        if self.n < 1:
            raise IndexError('pop from empty priority queue')
        self.n -= 1 # Not correct on its own

    @classmethod
    def sort(Queue, A):
        pq = Queue(A) # make empty priority queue
        for i in range(len(A)): # n x T_insert
            pq.insert()
        for i in range(len(A)): # n x T_delete_max
            pq.delete_max()
        return pq(A)