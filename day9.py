# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:32:26 2021

@author: Xtrem
"""

import numpy as np
import matplotlib.pyplot as plt

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
        
def heightmap2(add_plots):

    file = open("day9_input.txt", "r")
    line = []
    for x in file:
        l = []
        for i in x:
            if i != "\n":
                l.append(int(i))
        line.append(l)
    line = np.array(line)
    count=0
    tmax=[0,0,0]
    if add_plots:
        cave_map = np.zeros([100, 100])
        cave_border = np.zeros([100,100])
        fig,ax = plt.subplots(1,2)
    for i in range (100):
        for j in range (100):
            if add_plots and line[i,j]==9:
                cave_border[i,j]=1
            to_check = [True, True, True, True]
            if i == 0:
                to_check[0] = False
            if j == 0:
                to_check[1] = False
            if j == 99:
                to_check[2] = False
            if i == 99:
                to_check[3] = False
            hole = True
            if to_check[0]:
                if line[i - 1, j] <= line[i, j]:
                    hole = False
            if to_check[1]:
                if line[i, j - 1] <= line[i, j]:
                    hole = False
            if to_check[2]:
                if line[i, j + 1] <= line[i, j]:
                    hole = False
            if to_check[3]:
                if line[i + 1, j] <= line[i, j]:
                    hole = False
            if hole:
                count+=1

                if add_plots:
                    t, to_show = search_bassin(i, j, line)
                    for (a,b) in to_show:
                        cave_map[a,b] = count
                else:
                    t=search_bassin(i,j,line)[0]
                if t > min(tmax):
                    tmax[tmax.index(min(tmax))] = t
    if add_plots:
        ax[0].imshow(cave_map)
        ax[1].imshow(cave_border)
        plt.show()
    return tmax[0]*tmax[1]*tmax[2]



def search_bassin(i,j,line):
    stock = []

    def expand (i,j,to_check,line):

        nonlocal stock
        stock.append((i,j))
        if i == 0:
            to_check[0] = False
        if j == 0:
            to_check[1] = False
        if j == 99:
            to_check[2] = False
        if i == 99:
            to_check[3] = False
        count = 0
        if to_check[0]:
            if (i - 1, j) not in stock and line[i - 1, j] < 9:
                expand ( i - 1, j, [True, True, True, False],line)
        if to_check[1]:
            if (i , j-1) not in stock and line[i , j-1] < 9:
                expand ( i , j-1, [True, True, False,True],line)
        if to_check[2]:
            if (i , j+1) not in stock and line[i , j+1] < 9:
                expand ( i , j+1, [True, False, True, True],line)
        if to_check[3]:
            if (i + 1, j) not in stock and line[i + 1, j] < 9:
                expand ( i + 1, j, [False,True, True, True],line)
    expand(i,j,[True,True,True,True],line)
    return len(stock),stock


print(heightmap1())
print(heightmap2(False))
print(heightmap2(True))
