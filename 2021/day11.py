# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:31:36 2021

@author: Xtrem
"""

import numpy as np 

def update(l,i,j,visited,count):
    visited.append((i,j))
    for ibis in range (-1,2):
        for jbis in range (-1,2):
            if ibis!=0 and ibis!=0 :
                if not((i+ibis,j+jbis) in visited):
                    l[i+ibis][j+jbis]+=1
                    if l[i+ibis][j+jbis]>8: 
                        visited.append((i+ibis,j+jbis))
                        count=[count[0]+1]
                        update(l,i+ibis,j+jbis,visited,count)

def octopus1():
    file = open("day11_input.txt", "r")
    line = np.zeros([12,12])
    count=1
    for x in file:
        l=[]
        for i in x:
           if i!="\n":
               l.append(int(i))
        line[count]=[0]+l+[0]
        count+=1
    count=[0]
    for t in range (2):
        print(line)
        visited=[(0,x) for x in range (12)]+[(11,x) for x in range(12)]+\
            [(x,0) for x in range(1,11)]+[(x,11) for x in range(1,11)]
        for i in range(1,11):
            for j in range (1,11):
                line[i][j]+=1
                if line[i][j]>8 and not((i,j) in visited):
                    count=[count[0]+1]
                    update(line,i,j,visited,count)
        for x in visited:
            line[x[0]][x[1]]=0
    return count

""" update de visited se fait trop tot il faut le faire apres que tt les adjacentes soient visitée"""
                            
                    