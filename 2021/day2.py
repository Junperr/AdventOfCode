# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:49:55 2021

@author: Xtrem
"""

def movement1():
    file = open('day2_input.txt', 'r')
    l=[0,0]
    for line in file:
        move,value = line.split(" ")
        print(move,value)
        if move == "forward":
            l[0] += int(value)
        elif move == "up":
            l[1] -= int(value)
        elif move == "down":
            l[1] += int(value)
    return l[0]*l[1]

def movement2():
    file = open('day2_input.txt', 'r')
    l=[0,0,0]
    for line in file:
        move,value = line.split(" ")
        print(move,value)
        if move == "forward":
            l[1] += int(value)
            l[2] += int(value)*l[0]
        elif move == "up":
            l[0] -= int(value)
        elif move == "down":
            l[0] += int(value)
    return l[2]*l[1]