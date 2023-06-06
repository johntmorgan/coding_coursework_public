#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:22:30 2023

@author: johnmorgan
"""

class FileSystem:
    def __init__(self):
        self.root = Directory("/")
        
    def ls(self, path):
        dir_arr = path.split("/")
        curr_dir = self.root
        for dir_name in dir_arr:
            if dir_name:
                if dir_name in curr_dir.children:
                    curr_dir = curr_dir.children[dir_name]
                else:
                    return "Invalid path"
        output = []
        if curr_dir.children:
            output += list(curr_dir.children.keys())
        if curr_dir.files:
            output += list(curr_dir.files.keys())
        return output
                
    def mkdir(self, path):
        dir_arr = path.split("/")
        curr_dir = self.root
        for dir_name in dir_arr:
            if dir_name:
                if dir_name in curr_dir.children:
                    curr_dir = curr_dir.children[dir_name]
                else:
                    new_dir = Directory(dir_name)
                    curr_dir.children[dir_name] = new_dir
                    curr_dir = curr_dir.children[dir_name]
                
    def add_content_to_file(self, file_path, content):
        path_arr = file_path.split("/")
        curr_dir = self.root
        for dir_name in path_arr[:-1]:
            if dir_name:
                if dir_name in curr_dir.children:
                    curr_dir = curr_dir.children[dir_name]
                else:
                    return "Invalid path"
        file_name = path_arr[-1]
        if file_name in curr_dir.files:
            curr_dir.files[file_name].content += content
        else:
            new_file = File(file_name, content)
            curr_dir.files[file_name] = new_file
            
    def read_content_from_file(self, file_path):
        path_arr = file_path.split("/")
        curr_dir = self.root
        for dir_name in path_arr[:-1]:
            if dir_name:
                if dir_name in curr_dir.children:
                    curr_dir = curr_dir.children[dir_name]
                else:
                    return "Invalid path"
        file_name = path_arr[-1]
        if file_name in curr_dir.files:
            return curr_dir.files[file_name].content
        else:
            return "Invalid file name"
        
class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.files = {}
        
class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content


fs = FileSystem()
print(fs.ls("/"))
        
# class FileSystem:
#     def __init__(self):
#         self.root = Directory("/")

#     def ls(self, path):
#         dir_arr = path.split("/")
#         curr_dir = self.root
#         for directory in dir_arr:
#             if directory:
#                 if directory in curr_dir.children:
#                     curr_dir = curr_dir[directory]
#                 else:
#                     return "Invalid path"
#         if curr_dir.children.keys():
#             return list(curr_dir.children.keys())
#         else:
#             return []

#     def mkdir(self, path):
#         dir_arr = path.split("/")
#         curr_dir = self.root
#         for directory in dir_arr:
#             if directory:
#                 curr_dir.children[directory] = Directory(directory)
#                 curr_dir = curr_dir.children[directory]

#     def add_content_to_file(self, file_path, content):
#         dir_arr = file_path.split("/")
#         curr_dir = self.root
#         for directory in dir_arr[:-1]:
#             if directory:
#                 if directory in curr_dir.children:
#                     curr_dir = curr_dir.children[directory]
#                 else:
#                     return "Invalid path"
#         file = File(dir_arr[-1], content)
#         curr_dir.files[dir_arr[-1]] = file

#     def read_content_from_file(self, file_path):
#         dir_arr = file_path.split("/")
#         curr_dir = self.root
#         for directory in dir_arr[:-1]:
#             if directory:
#                 if directory in curr_dir.children:
#                     curr_dir = curr_dir.children[directory]
#                 else:
#                     return "Invalid path"
#         file_name = dir_arr[-1]
#         if file_name in curr_dir.files:
#             return curr_dir.files[file_name].content
#         else:
#             return "Invalid file"
    
# class Directory:
#     def __init__(self, name):
#         self.name = name
#         self.children = {}
#         self.files = {}
    
# class File:
#     def __init__(self, name, content):
#         self.name = name
#         self.content = content