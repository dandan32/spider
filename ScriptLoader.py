#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author: dandan<pipidingdingting@163.com>
# Created on 2018/11/9 0:58
# file: ScriptLoader.py

"""https://pymotw.com/3/sys/imports.html#importing-from-a-shelve"""


import imp
import sys
import types

"""动态加载爬虫脚本"""

source = """
import os
import sys
import math


class A:
    url = ''
    header = []
    cookies = []
    
    def hellp(self):
        print("hello")


B = 1
    
"""
print('creating a new module object for {!r}'.format("test"))
mod = sys.modules.setdefault("test",imp.new_module("test"))

# Set a few properties required by PEP 302
mod.__file__ = "test.py"
mod.__name__ = "test"
mod.__path__ = "./test.py"
mod.__loader__ = None

# PEP-366 specifies that package's set __package__ to
# their name, and modules have it set to their parent
# package (if any).
mod.__package__ = "dbscript"


print('imported as regular module')

print('execing source...')
exec(source, mod.__dict__)
print('done')
import test

a =  test.A

for each in dir(test):
    if isinstance(getattr(test, each), type):
        # TODO 判断是否为Handler的子类
        print(each, type(getattr(test, each)))



def LoadScript(name, content):
    """load spider script."""
    pass
