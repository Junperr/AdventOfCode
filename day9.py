# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:32:26 2021

@author: Xtrem
"""

import numpy as np 

def heightmap1():
    file = open("day9_input.txt","r")
    line = []
    for x in file:
        l=[]
        for i in x:
           if i!="\n":
               l.append(int(i))
        line.append(l)
    line=np.array(line)
    s=0
    for i in range (100):
        for j in range (100):
            
            to_check=[True,True,True,True]
            if i==0:
                to_check[0]=False
            if j==0:
                to_check[1]=False
            if j==99:
                to_check[2]=False
            if i==99:
                to_check[3]=False
            hole=True
            if to_check[0]:
                if line[i-1,j]<=line[i,j]:
                    hole=False
            if to_check[1]:
                if line[i,j-1]<=line[i,j]:
                    hole=False
            if to_check[2]:
                if line[i,j+1]<=line[i,j]:
                    hole=False
            if to_check[3]:
                if line[i+1,j]<=line[i,j]:
                    hole=False
            if hole:
                # print(line[i,j],line[i-1,j],line[i+1,j],line[i,j-1],line[i,j+1])
                s+=line[i,j]+1
    return s

def is_low(line,i,j,check):
    hole=True
    to_check=check.copy()
    if i==0:
        to_check[0]=False
    if j==0:
        to_check[1]=False
    if j==99:
        to_check[2]=False
    if i==99:
        to_check[3]=False
    count=0
    if to_check[0]:
        if line[i-1,j]<line[i,j]:
            hole=False
        elif check[0]:
            count+=is_low(line,i-1,j,[True,True,True,False])
    if to_check[1]:
        if line[i,j-1]<line[i,j]:
            hole=False
        elif check[1]:
            count+=is_low(line,i,j-1,[True,True,False,True])
    if to_check[2]:
        if line[i,j+1]<line[i,j]:
            hole=False
        elif check[2]:
            count+=is_low(line,i,j+1,[True,False,True,True])
    if to_check[3]:
        if line[i+1,j]<line[i,j]:
            hole=False
        elif check[3]:
            count+=is_low(line,i+1,j,[False,True,True,True])
    
    if hole:
        return count+1
    return 0
        
def heightmap2():
    file = open("day9_input.txt","r")
    line = []
    for x in file:
        l=[]
        for i in x:
           if i!="\n":
               l.append(int(i))
        line.append(l)
    line=np.array(line)
    smax=[0,0,0]
    for i in range (100):
        for j in range (100):
            s=is_low(line,i,j,[True,True,True,True])
            for t in range(3):
                if s>smax[t] and smax[t]==min(smax):
                    smax[t]=s
                    break 
    return smax[0]*smax[1]*smax[2]


