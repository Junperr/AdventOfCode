import os, sys, re, math, copy, fileinput
from string import ascii_uppercase, ascii_lowercase
from collections import Counter, defaultdict, deque, namedtuple
from itertools import count, product, permutations, combinations, combinations_with_replacement
import pyperclip

import parsing
from usefull import parse_line, parse_nums, mul, all_unique, factors, primes
from usefull import gcd, lcm, min_max_xy, print_grid
from usefull import new_table, transposed, rotated, firsts, lasts,n_col
from usefull import md5, sha256, VOWELS, CONSONANTS
from usefull import Point, DIRS, DIRS_4, DIRS_8, N, NE, E, SE, S, SW, W, NW
# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD
# Ascii code :                                A 65,Z 90,a 97,z 122,0 48,9 57

# day  .input .l() .par() .b2d()


pyperclip.copy("""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""")

clip = pyperclip.paste()
day = parsing.Day(year=2023, day=12, sample=None)

def place (record,needed,cur):
    # print("called",record,needed)

    if not needed:
        # print("rest",record)
        for x in record:
            if "#" in x:
                # print("don't work")
                return 0,False
        return 1,True
    if not record:
        # print("don't work")
        return 0,False
    seg = []
    target = needed[0]
    min_seg = -1
    for k,x in enumerate(record):
        if x:
            seg.append(x)
            if min_seg == -1 and "#" in x:
                min_seg = len(seg)
    count = 0
    work = True
    breaked = False
    if min_seg == -1:
        min_seg = len(seg)
    for i in range(min_seg):
        if len(seg[i])>=target:
            for j in range(len(seg[i])-target):
                if seg[i][j+target] != "#":
                    # print("call 1")

                    curi = copy.deepcopy(cur)
                    curi.append(seg[i][j:j+target])
                    curi.append((j,j+target-1))
                    # print(f"current : {curi} and {count} is {breaked}")
                    countrec,work = place([seg[i][j+target+1:]]+seg[i+1:],needed[1:],curi)
                    # print(seg[i][j:j+target],[seg[i][j + target + 1:]] + seg[i + 1:],needed[1:],countrec)
                    count += countrec
                if seg[i][j] == "#":
                    breaked = True
                    # print("breaked")
                    break
            else:
                # print("call 2",seg[i][len(seg[i])-target:],seg[i+1:], needed[1:])

                curi = copy.deepcopy(cur)
                curi.append(seg[i][len(seg[i])-target:])
                curi.append((len(seg[i])-target,len(seg[i])-1))
                # print(f"current : {curi} and {count} is {breaked}")
                countrec,work = place(seg[i+1:],needed[1:],curi)
                # print(seg[i][len(seg[i])-target:],seg[i+1:], needed[1:], countrec)
                count += countrec
            if breaked:
                break
    return count,work


def part1(day):
    l = day.l()
    s = 0
    for i,line in enumerate(l):
        record,needed = line.split()
        needed = parse_nums(needed)
        record = record.split(".")
        s1,work = place(record,needed,[])
        # if int(b) !=s1:
        # print(i,s1,work,line)
        s += s1
    return s

dayp2 = copy.deepcopy(day)
print(part1(day))

def place2 (record,needed,cur,dp):
    # print((record,needed))
    if (record,needed) in dp:
        return dp[record,needed]

    if not needed:
        # print("rest",record)
        for x in record:
            if "#" in x:
                return 0,False
        return 1,True
    if not record:
        # print("don't work")
        return 0,False
    seg = []
    target = needed[0]
    min_seg = -1
    for k,x in enumerate(record):
        if x:
            seg.append(x)
            if min_seg == -1 and "#" in x:
                min_seg = len(seg)
    count = 0
    work = True
    breaked = False
    if min_seg == -1:
        min_seg = len(seg)
    for i in range(min_seg):
        if len(seg[i])>=target:
            for j in range(len(seg[i])-target):
                if seg[i][j+target] != "#":
                    # print("call 1")

                    curi = copy.deepcopy(cur)
                    curi.append(seg[i][j:j+target])
                    curi.append((j,j+target-1))
                    # print(f"current : {curi} and {count} is {breaked}")
                    countrec,work = place2(tuple([seg[i][j+target+1:]]+seg[i+1:]),needed[1:],curi,dp)
                    # print(seg[i][j:j+target],[seg[i][j + target + 1:]] + seg[i + 1:],needed[1:],countrec)
                    count += countrec
                if seg[i][j] == "#":
                    breaked = True
                    # print("breaked")
                    break
            else:
                # print("call 2",seg[i][len(seg[i])-target:],seg[i+1:], needed[1:])

                curi = copy.deepcopy(cur)
                curi.append(seg[i][len(seg[i])-target:])
                curi.append((len(seg[i])-target,len(seg[i])-1))
                # print(f"current : {curi} and {count} is {breaked}")
                countrec,work = place2(tuple(seg[i+1:]),needed[1:],curi,dp)
                # print(seg[i][len(seg[i])-target:],seg[i+1:], needed[1:], countrec)
                count += countrec
            if breaked:
                break
    dp[record,needed] = [count,work]
    return count,work

def part2(day):
    dp = {}
    l = day.l()
    s = 0
    for i, line in enumerate(l):
        record, needed = line.split()
        needed = tuple(parse_nums(needed))
        nrecord = record
        for _ in range(4):
            nrecord += "?" + record
        record = tuple(nrecord.split("."))


        nneeded = needed * 5
        # print("here")
        # print(record,nneeded)
        s1, work = place2(record, nneeded, [],dp)
        # print(i,s1,work,line)
        s += s1
    return s

print(part2(dayp2))