#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:42:22 2023

@author: johnmorgan
"""

class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_path(self, file_path, value):
        path_arr = file_path.split("/")
        curr_dir = self.root
        for directory in path_arr[:-1]:
            if directory:
                if directory in curr_dir.subdirectories:
                    curr_dir = curr_dir.subdirectories[directory]
                else:
                    return False
        curr_dir.subdirectories[path_arr[-1]] = Directory(path_arr[-1])
        curr_dir.files[path_arr[-1]] = value
        return True

    def get(self, file_path):
        path_arr = file_path.split("/")
        curr_dir = self.root
        for directory in path_arr[:-1]:
            if directory:
                if directory in curr_dir.subdirectories:
                    curr_dir = curr_dir.subdirectories[directory]
                else:
                    return -1
        if path_arr[-1] in curr_dir.files:
            return curr_dir.files[path_arr[-1]]
        else:
            return -1
            
class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = {}
        self.files = {}

fs = FileSystem()
print(fs.create_path("/a", 1))
print(fs.get("/a"))
print(fs.create_path("/a/b", 2))
print(fs.get("/a/b"))
print(fs.get("/a/b/c"))
print(fs.create_path("/a/b/c/d", 4))