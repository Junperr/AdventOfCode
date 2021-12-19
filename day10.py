# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 14:12:43 2021

@author: Xtrem
"""

def point_value(t):
    if t=='>':
        return 25137
    elif t==']':
        return 57
    elif t=='}':
        return 1197
    elif t==')':
        return 3

possible_tuple=[('(',')'),('[',']'),('{','}'),('<','>')]

def mayday1():
    file = open("day10_input.txt","r")
    lines=file.readlines()
    s=0
    for i in range (len(lines)):
        pile=[]
        for x in lines[i]:
            pile.append(x)
            # print(pile)
            if x in ['}',')',']','>']:
                try: 
                    end,op = pile.pop(),pile.pop()
                    if not((op,end) in possible_tuple):
                        print(op,end)
                        s+= point_value(end)
                        break
                
                except: 
                    pass
    return s
            
def point_value2(t):
    if t=='>':
        return 4
    elif t==']':
        return 2
    elif t=='}':
        return 3
    elif t==')':
        return 1
    
def mayday2():
    file = open("day10_input.txt","r")
    lines=file.readlines()
    scores=[]
    for i in range (len(lines)):
        pile=[]
        for x in lines[i]:
            pile.append(x)
            if x in ['}',')',']','>']:
                try: 
                    end,op = pile.pop(),pile.pop()
                    if not((op,end) in possible_tuple):
                        pile=[]
                        break
                except: 
                    pass
        if len(pile)!=0:
            score=0
            while len(pile)>0:
                op=pile.pop()
                for couple in possible_tuple:
                    if op==couple[0]:
                        score = score * 5 + point_value2(couple[1])
            scores.append(score)
    scores.sort()
    return scores[len(scores)//2]
                