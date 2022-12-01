# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:57:00 2021

@author: Xtrem
"""

def crab1():
    file = open('day7_input.txt', 'r')
    pos = [int(x) for x in file.readline().split(",")]
    s=0
    smin=sum(pos)
    for i in range (min(pos),max(pos)+1):
        for x in pos:
            s+=abs(x-i)
        if s<smin:
            smin=s
        s=0
    return smin

def crab2():
    file = open('day7_input.txt', 'r')
    pos = [int(x) for x in file.readline().split(",")]
    s=0
    smin=10**10
    for i in range (min(pos),max(pos)+1):
        for x in pos:
            n = abs(x-i)
            s+=n*(n+1)/2
        if s<smin:
            smin=s
        s=0
    return smin