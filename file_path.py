# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:06:13 2020

@author: USER
"""

import os.path as os
if os.isfile('new.txt'):
    print('存在')
    file=open('new.txt','a')
    file.write('檔案94存在')
else:
    print('不存在')
    file=open('new.txt','w')
    file.write('這是新的檔案')

