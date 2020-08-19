# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:21:12 2020

@author: USER
"""
import numpy as n
def circle_area(x):
    num=x*x*n.pi
    return num
def circle_circum(y):
    num2=y*2*n.pi
    return num2


i=int(input('半徑:'))
a=i
i=circle_area(i)
print('圓面積等於:',i)

a=circle_circum(a)
print('圓周長等於:',a)