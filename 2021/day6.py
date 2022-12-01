# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:00:43 2021

@author: Xtrem
"""

def fish1():
    file = open('day6_input.txt', 'r')
    line = file.readlines()
    l=[0 for x in range (9)]
    for i in range(len(line[0])):
        if 47<ord(line[0][i])<58:
            l[int(line[0][i])]+=1
    for x in range(80):
        l=[l[1],l[2],l[3],l[4],l[5],l[6],l[7]+l[0],l[8],l[0]]
    return sum(l)

def fish2():
    file = open('day6_input.txt', 'r')
    line = file.readlines()
    l=[0 for x in range (9)]
    for i in range(len(line[0])):
        if 47<ord(line[0][i])<58:
            l[int(line[0][i])]+=1
    for x in range(256):
        l=[l[1],l[2],l[3],l[4],l[5],l[6],l[7]+l[0],l[8],l[0]]
    return sum(l)