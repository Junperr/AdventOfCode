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


pyperclip.copy("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=4, sample=None)

def part1(day):
    s=0
    for l in day.l():
        _,a = l.split(":")
        obj,cur = a.split("|")
        obj = set(map(int,obj.split()))
        cur = set(map(int,cur.split()))
        count = 0
        for x in cur:
            if x in obj:
                count+=1
        # print(obj,cur,count,2**(count-1))
        if count != 0:
            s+= 2**(count-1)
    return s
    pass
dayp2 = copy.deepcopy(day)
print(part1(day))

def part2(day):
    lines = day.l()
    dp = [0]*len(lines)
    for i in range(len(lines)-1,-1,-1):
        l = lines[i]
        _,a = l.split(":")
        obj,cur = a.split("|")
        obj = set(map(int,obj.split()))
        cur = set(map(int,cur.split()))
        count = 0
        for x in cur:
            if x in obj:
                count+=1
        count2 = 1
        for j in range(i+1,i+1+count):
            count2+= dp[j]
            dp[i] += dp[j]
        dp[i] +=1
    return sum(dp)


print(part2(dayp2))