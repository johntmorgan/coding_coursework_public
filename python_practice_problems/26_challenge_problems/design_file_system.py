#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:54:09 2023

@author: johnmorgan
"""

class FileSystem:
    def __init__(self):
        self.root = Directory("/")
    
    def create_path(self, path, content):
        path_arr = path.split("/")
        curr_dir = self.root
        for dir_name in path_arr[:-1]:
            if dir_name:
                if dir_name in curr_dir.children:
                    curr_dir = curr_dir.children[dir_name]
                else:
                    return False
        file_name = path_arr[-1]
        file = File(file_name, content)
        curr_dir.files[file_name] = file
        new_dir = Directory(file_name)
        curr_dir.children[file_name] = new_dir
        return True
    
    def get(self, path):
        path_arr = path.split("/")
        curr_dir = self.root
        for dir_name in path_arr[:-1]:
            if dir_name:
                if dir_name in curr_dir.children:
                    curr_dir = curr_dir.children[dir_name]
                else:
                    return -1
        file_name = path_arr[-1]
        if file_name in curr_dir.files:
            return curr_dir.files[file_name].content
        else:
            return -1
        
class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.files = {}

class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content