# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:12:22 2021

@author: Xtrem
"""



def part1 ():
    file = open("day1_input.txt","r")
    count=0
    prev=None
    for line in file:
        if prev == None:
            prev = int(line)
        else:
            if int(line)>prev:
                count+=1
        prev=int(line)
    print(prev)
    file.close
    return count

def part2 ():
    file = open("day1_input.txt","r")
    count=0
    prev=[]
    for line in file:
        if len(prev)<=3:
            prev.append(int(line))
        else:
            if sum(prev[:3])<sum(prev[1:]):
                count+=1
        prev.pop(0)
        prev.append(int(line))
    file.close
    return count