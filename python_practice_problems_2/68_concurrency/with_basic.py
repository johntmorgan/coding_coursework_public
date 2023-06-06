#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:50:03 2023

@author: johnmorgan
"""

class ExampleClass(object):

    def __init__(self, val):
        print("init")
        self.val = val

    def display(self):
        print(self.val)

    def __enter__(self):
        print("enter invoked")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit invoked")


if __name__ == "__main__":
    with ExampleClass("hello world") as example:
        example.display()