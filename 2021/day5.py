# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:37:26 2021

@author: Xtrem
"""

import numpy as np 

def coordinate(txt):
    if txt[-1]=='\n':
        l = txt[:-1].split(" ")
    else:
        l = txt.split(" ")
    l[0] = l[0].split(",")
    l[2] = l[2].split(",")
    return ((int(l[0][0]),int(l[0][1])),(int(l[2][0]),int(l[2][1])))

def radar1():
    file = open('day5_input.txt', 'r')
    map1=np.zeros([991,991])
    for line in file :
        point1,point2 = coordinate(line)
        if point1[0]==point2[0]:
            if point1[1]<=point2[1]:
                map1[point1[0],point1[1]:point2[1]+1]+=1
            if point1[1]>point2[1]:
                map1[point1[0],point2[1]:point1[1]+1]+=1
        elif point1[1]==point2[1]:
            if point1[0]<=point2[0]:
                map1[point1[0]:point2[0]+1,point1[1]]+=1
            if point1[0]>point2[0]:
                map1[point2[0]:point1[0]+1,point1[1]]+=1
    count=0
    for i in range (len(map1)):
        for j in range (len(map1[0])):
            if map1[i,j]>1:
                count+=1
    return count

def radar2():
    file = open('day5_input.txt', 'r')
    map1=np.zeros([991,991])
    count=0
    for line in file :
        count+=1
        point1,point2 = coordinate(line)
        
        if point1[0]==point2[0]:
            if point1[1]<=point2[1]:
                map1[point1[0],point1[1]:point2[1]+1]+=1
            if point1[1]>point2[1]:
                map1[point1[0],point2[1]:point1[1]+1]+=1
        elif point1[1]==point2[1]:
            if point1[0]<=point2[0]:
                map1[point1[0]:point2[0]+1,point1[1]]+=1
            if point1[0]>point2[0]:
                map1[point2[0]:point1[0]+1,point1[1]]+=1
        elif point1[0]<point2[0]:
            if point1[1]<point2[1]:
                map1[range(point1[0],point2[0]+1),range(point1[1],point2[1]+1)]+=1
            else:
                map1[range(point1[0],point2[0]+1),range(point1[1],point2[1]-1,-1)]+=1
        else:
            if point1[1]<point2[1]:
                map1[range(point1[0],point2[0]-1,-1),range(point1[1],point2[1]+1)]+=1
            else:
                print(point1[0]-point2[0],point1[1]-point2[1],count,point1,point2)
                map1[range(point1[0],point2[0]-1,-1),range(point1[1],point2[1]-1,-1)]+=1
    count=0
    for i in range (len(map1)):
        for j in range (len(map1[0])):
            if map1[i,j]>1:
                count+=1
    return count