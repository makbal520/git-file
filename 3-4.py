# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:56:23 2019

@author: 15299
"""
l=[]
m=[]
w=input().lower()
l=list(w)
for i in range(l.count(' ')):
    l.remove(' ')
l1=set(l)
d=len(l1)
w=w.split()
l1=["and","of"]
for j in range(len(w)-1,-1,-1):
    if w[j] in l1:
        w.remove(w[j])
for i in w:
    m.append(i[0])
w=''.join(m)
print(d)
print(w.upper())