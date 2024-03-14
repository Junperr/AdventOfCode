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


pyperclip.copy("""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=11, sample=None)

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def part1(day):
    g = day.b2d()
    empl = set()
    points = []
    for i in range(len(g)):
        empty = True
        for j in range(len(g[0])):
            if g[i][j] == "#":
                empty = False
                points.append((i,j))
        if empty:
            empl.add(i)
    empc = set()
    for i in range(len(g[0])):
        empty = True
        for j in range(len(g)):
            if g[j][i] == "#":
                empty = False

                break
        if empty:
            empc.add(i)
    print(empc,empl)
    mapy = {}
    dec = 0
    for i in range(len(g)):
        if i in empl:
            dec += 1
        else:
            mapy[i] = i + dec
    mapx = {}
    dec = 0
    for i in range(len(g[0])):
        if i in empc:
            dec += 1
        else:
            mapx[i] = i + dec
    print(mapx,mapy)
    s = 0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            # print(points[i],points[j])
            s +=manhattan((mapy[points[i][0]],mapx[points[i][1]]),(mapy[points[j][0]],mapx[points[j][1]]))

    return s
    pass
dayp2 = copy.deepcopy(day)
print(part1(day))

def part2(day):
    g = day.b2d()
    empl = set()
    points = []
    for i in range(len(g)):
        empty = True
        for j in range(len(g[0])):
            if g[i][j] == "#":
                empty = False
                points.append((i,j))
        if empty:
            empl.add(i)
    empc = set()
    for i in range(len(g[0])):
        empty = True
        for j in range(len(g)):
            if g[j][i] == "#":
                empty = False

                break
        if empty:
            empc.add(i)
    print(empc,empl)
    mapy = {}
    dec = 0
    for i in range(len(g)):
        if i in empl:
            dec += 1
        else:
            mapy[i] = i + dec *(10**6-1)
    mapx = {}
    dec = 0
    for i in range(len(g[0])):
        if i in empc:
            dec += 1
        else:
            mapx[i] = i + dec *(10**6-1)
    print(mapx,mapy)
    s = 0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            # print(points[i],points[j])
            s +=manhattan((mapy[points[i][0]],mapx[points[i][1]]),(mapy[points[j][0]],mapx[points[j][1]]))

    return s
    pass

import time

deb = time.perf_counter()

print(part2(dayp2))
print(time.perf_counter()-deb)