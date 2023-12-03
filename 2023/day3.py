import os, sys, re, math, copy, fileinput
import timeit
from string import ascii_uppercase, ascii_lowercase
from collections import Counter, defaultdict, deque, namedtuple
from itertools import count, product, permutations, combinations, combinations_with_replacement
import pyperclip
import time

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


pyperclip.copy("""467..114..
...*......
..35..633_
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=3, sample=None)



def part1(day):
    g = day.b2d()
    s = 0
    for i in range(len(g)):
        cur = 0
        work = False
        for j in range(len(g[0])):
            if type(g[i][j]) == int:
                cur = cur*10 + g[i][j]
                for i1,j1 in [(1,-1),(1,0),(1,1),(-1,0),(-1,-1),(-1,1),(0,-1),(0,1)]:
                    if 0<=i + i1 < len(g) and 0<=j + j1 < len(g[0]):
                        if type(g[i+i1][j+j1]) == str and g[i+i1][j+j1] != ".":
                            work = True
            elif work:
                s += cur
                cur = 0
                work = False
            else:
                cur = 0
                work = False
        if cur != 0 and work:
            s += cur
    return s

    pass
dayp2 = copy.deepcopy(day)
deb = time.time()
print(part1(day))
print(time.time()-deb)
def part2(day):
    g = day.b2d()
    # print(g)
    s = 0
    nums = []
    sub = {}
    for i in range(len(g)):
        cur = 0
        work = set()
        for j in range(len(g[0])):
            if type(g[i][j]) == int:

                cur = cur*10 + g[i][j]
                for i1,j1 in [(1,-1),(1,0),(1,1),(-1,0),(-1,-1),(-1,1),(0,-1),(0,1)]:
                    if 0<=i + i1 < len(g) and 0<=j + j1 < len(g[0]):
                        if type(g[i+i1][j+j1]) == str and g[i+i1][j+j1] == "*":
                            # syb[(i+i1,j+j1)] = syb.get((i+i1,j+j1),[]) + []
                            work.add((i+i1,j+j1))
                # print(work)
            elif work:
                for x in work:
                    # print(x)
                    sub[x] = sub.get(x,[]) + [cur]
                # s += cur
                # nums.append(cur)
                cur = 0
                work = set()
            else:
                cur = 0
                work = set()
        for x in work:
            sub[x] = sub.get(x,[]) + [cur]
    # print(sub)
    for key in sub.keys():
        if len(sub[key]) == 2:
            s += sub[key][0]*sub[key][1]

    return s
    pass
deb = time.time()
print(part2(dayp2))
print(time.time()-deb)
