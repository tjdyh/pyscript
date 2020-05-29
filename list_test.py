#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
这个脚本用于测试os模块各功能
"""

import os

#当前文件所在目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(os.path)
print(os.name)
print(os.curdir)
print(os.pardir)
print(BASE_DIR)

#递归查询传参目录下所有文件，包括子目录下文件
def list_all_files(rootdir):
    _files = []
    list_file = os.listdir(rootdir)
    # print(list_file)
    for i in list_file:
        path = os.path.join(rootdir,i)
        # print(path)
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files

files = list_all_files(BASE_DIR)
# print(files)
for i  in files:
    print(i)