# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:13:24 2021

@author: Xtrem
"""

def fusible1():
    file=open('day8_input.txt','r')
    lines=file.readlines()
    count=0
    for x in lines:
        x1,x2=x.split('|')
        x2=x2.split()
        for i in x2:
            if len(i) in [2,3,4,7]:
                count+=1
    return count

def fusible2():
    file=open('day8_input.txt','r')
    lines=file.readlines()
    s=0
    for x in lines:
        x1,x2=x.split('|')
        x1,x2=x1.split(),x2.split()
        segments={0:None,1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None}
        uncode={'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[]}
        possible5=[]
        possible6=[]
        for seg in x1:
            long=len(seg)
            if long==2:
                segments[1]=seg
            if long==3:
                segments[7]=seg
            if long==4:
                segments[4]=seg
            if long==5:
                possible5.append(seg)
            if long==6:
                possible6.append(seg)
            if long==7:
                segments[8]=seg
                
        a,b=segments[1]
        for i in segments[7]:
            if i != a and i != b:
                uncode[i]='a'
        for i in segments[8]:
            if i in possible5[0] and i in possible5[1] and i in possible5[2]:
                if i in segments[4]:
                    uncode[i]='d'
                elif not(i in segments[7]):
                    uncode[i]='g'
        
        for x in possible6:
            if not(a in x):
                segments[6]=x
                uncode[a]='c'
                uncode[b]='f'
            if not(b in x):
                segments[6]=x
                uncode[b]='c'
                uncode[a]='f'
                
        for x in possible5:
            if a in x and b in x:
                segments[3]=x
        for i in segments[8]:
            if not(i in segments[3]):
                if i in possible6[0] and i in possible6[1] and i in possible6[2]:
                    uncode[i]='b'
                else:
                    uncode[i]='e'
        code=""
        for seg in x2:
            if len(decode(seg,uncode))==2:
                return decode(seg,uncode)
            code=code+decode(seg,uncode)
        print(code)
        s+=int(code)
    return s
        

def decode(seg,uncode):
    long=len(seg)
    if long==2:
        return '1'
    if long==3:
        return '7'
    if long==4:
        return '4'
    if long==5:
        possible5=["acdeg","acdfg","abdfg"]
        t=""
        for i in seg:
           t= t+uncode[i]
        for j in range (3):
            state=True
            for i in t:
              if not(i in possible5[j]):
                  state=False
            if state:
                if j == 2:
                    return '5'
                if j==0:
                    return "2"
                return "3"
    if long==6:
        possible6=["abcefg","abdefg","abcdfg"]
        t=""
        for i in seg:
           t= t+uncode[i]
        for j in range (3):
            state=True
            for i in t:
              if not(i in possible6[j]):
                  state=False
            if state:
                if j == 0:
                    return '0'
                if j == 1:
                    return '6'
                return '9'
    if long==7:
        return '8'
    return seg,uncode

          
                