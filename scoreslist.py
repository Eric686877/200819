# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:01:15 2020

@author: USER
"""

s=[]
z=[]
maxs=0
mins=100
to=0
index=0
index2=0
for i in range(5):
    y=input('學生名:')
    n=int(input('成績:'))
   
    s.append(n)
    z.append(y)
    
    if n>maxs:
        maxs=n
        index=i
    if n<mins:
        mins=n
        index2=i
    to=to+n

x=to/len(s)
print('總分:',to)
print('平均:',x)
print('最高分:',z[index])
print('最低分:',z[index2])