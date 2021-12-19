# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:05:57 2021

@author: Xtrem
"""
def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal
  
    
def rate1():
    file = open('day3_input.txt','r')
    x=file.read().split('\n')
    n=len(x[0])
    L=[0 for x in range (n)]
    for i in range (len(x)):
        for j in range (n):
            if x[i][j]=='0':
                L[j]-=1
            else:
                L[j]+=1
    t,t1="",""
    for i in range (n):
        if L[i]>0:
            t=t+"1"
            t1=t1+"0"
        else:
            t=t+"0"
            t1=t1+"1"
    return binaryToDecimal(int(t))*binaryToDecimal(int(t1))

def find_matching(x1,state):
    i=0
    n=len(x1[0])
    while len(x1)>1 and i<n:
        x1bis=[]
        count=0
        current=""
        for j in range (len(x1)):
            if x1[j][i]=='0':
                count -= 1
            else:
                count += 1
        if count>=0:
            current = "1"
        else:
            current = "0"
        for j in range (len(x1)):
            if x1[j][i]==current and state:
                x1bis.append(x1[j])
            elif x1[j][i]!=current and not(state):
                x1bis.append(x1[j])
        x1=x1bis
        i+=1
    return x1bis

def rate2():
    file = open('day3_input.txt','r')
    x=file.read().split('\n')
    x1=find_matching(x, True)
    x2=find_matching(x, False)
    return binaryToDecimal(int(x1[0]))*binaryToDecimal(int(x2[0]))
    
                
    