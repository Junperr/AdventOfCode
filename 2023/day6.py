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


pyperclip.copy("""Time:      7  15   30
Distance:  9  40  200""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=6, sample=None)

def part1(day):
    t,d= day.l()
    t = list(map(int,t.split()[1:]))
    d = list(map(int,d.split()[1:]))

    s = 1
    for i in range(len(t)):
        cur = 0
        for j in range(t[i]):
            if j * (t[i]- j)>d[i]:
                cur +=1
        s *= cur
    return s
    pass
dayp2 = copy.deepcopy(day)
print(part1(day))

def part2(day):
    t,d= day.l()
    t = t.split()[1:]
    d = d.split()[1:]
    t1 = ""
    d1 = ""
    s = 1
    for i in range(len(t)):
        t1 = t1 + t[i]
        d1 = d1 + d[i]

    t1 = int(t1)
    d1 = int(d1)
    deb,end = 0,0
    for j in range(t1):
        if j * (t1- j)>d1:
            deb = j
            break
    for j in range(t1,deb-1,-1):
        if j * (t1- j)>d1:
            end = j
            break

    return end-deb +1
    pass

print(part2(dayp2))