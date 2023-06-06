#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:31:49 2023

@author: johnmorgan
"""

from Queue3 import MyQueue
from Stack3 import MyStack

# O(n) complexity

def reverseK(queue, k):
    if k > queue.size() or k < 0 or queue.is_empty():
        return None
    stack = MyStack()
    for _ in range(k):
        stack.push(queue.dequeue())
    for _ in range(k):
        queue.enqueue(stack.pop())
    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())
    return queue

queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
k = 5
queue = reverseK(queue, k)
for item in range(queue.size()):
    print(queue.dequeue())