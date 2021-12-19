# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:06:40 2021

@author: Xtrem
"""

import numpy as np 

def movement1():
    file = open('day4_input.txt','r')
    lines = file.readlines()
    numbers=[int(x) for x in lines[0][:-1].split(",")]
    bingo_sheet = []
    current=[]
    for i in range (2,len(lines)):
        if lines[i] == '\n':
            bingo_sheet.append(np.array(current))
            current=[]
        else:
            current2=""
            l=[]
            for j in range (len(lines[i])):
                if 47<ord(lines[i][j])<58:
                    current2= current2+lines[i][j]
                elif current2!="":
                    l.append(int(current2))
                    current2=""
            current.append(l)
        
    for t in range (len(numbers)):
        for x in range(len(bingo_sheet)):
            for i in range (5):
                for j in range (5):
                    if bingo_sheet[x][i,j]==numbers[t]:
                        bingo_sheet[x][i,j]=-1
                        if (bingo_sheet[x][i,:] == -1).all() or (bingo_sheet[x][:,j] == -1).all():
                            return sumwithout(bingo_sheet[x])*numbers[t]

def sumwithout(bingo):
    s=0
    for i in range(5):
        for j in range (5):
           if bingo[i,j]!=-1:
               s+=bingo[i,j]
    return s
            
def movement2():
    file = open('day4_input.txt','r')
    lines = file.readlines()
    numbers=[int(x) for x in lines[0][:-1].split(",")]
    bingo_sheet = []
    current=[]
    for i in range (2,len(lines)):
        if lines[i] == '\n':
            bingo_sheet.append(np.array(current))
            current=[]
        else:
            current2=""
            l=[]
            for j in range (len(lines[i])):
                if 47<ord(lines[i][j])<58:
                    current2= current2+lines[i][j]
                elif current2!="":
                    l.append(int(current2))
                    current2=""
            current.append(l)
    count=0
    for t in range (len(numbers)):
        for x in range(len(bingo_sheet)):
            for i in range (5):
                for j in range (5):
                    if bingo_sheet[x][i,j]==numbers[t]:
                        bingo_sheet[x][i,j]=-1
                        if (bingo_sheet[x][i,:] == -1).all() or (bingo_sheet[x][:,j] == -1).all():
                            count+=1
                            if count==len(bingo_sheet):
                                return sumwithout(bingo_sheet[x])*numbers[t]
                            else:
                                bingo_sheet[x]=bingo_sheet[x]*-1
