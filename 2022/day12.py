import os, sys, re, math, copy, fileinput
from string import ascii_uppercase, ascii_lowercase
from collections import Counter, defaultdict, deque, namedtuple
from itertools import count, product, permutations, combinations, combinations_with_replacement
import pyperclip

import parsing
from usefull import parse_line, parse_nums, mul, all_unique, factors, primes
from usefull import gcd, lcm, min_max_xy, print_grid
from usefull import new_table, transposed, rotated, firsts, lasts, n_col
from usefull import md5, sha256, VOWELS, CONSONANTS
from usefull import Point, DIRS, DIRS_4, DIRS_8, N, NE, E, SE, S, SW, W, NW

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD
# Ascii code :                                A 65,Z 90,a 97,z 122,0 48,9 57

# day  .input .l() .par() .b2d()

import copy

sys.setrecursionlimit(10**6)
pyperclip.copy("""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=12)
day = day.b2d()
day2 = copy.deepcopy(day)
# print(day, day[2][6])


def part1(day):
    to_go = new_table(len(day[0]),len(day) , 10 ** 10)

    # print(to_go[2][7])
    def path_rec(i, j, long):
        nonlocal to_go
        for dir in DIRS_4:

            if -1 < i + dir.x < len(day) and -1 < j + dir.y < len(day[0]):
                # print(i + dir.x, j + dir.y, ord(day[i + dir.x][j + dir.y]), ord(day[i][j]))
                if ord(day[i + dir.x][j + dir.y]) >=  (ord(day[i][j])-1) and to_go[i + dir.x][j + dir.y] > long:
                    to_go[i + dir.x][j + dir.y] = long
                    path_rec(i + dir.x, j + dir.y, long + 1)

    for i in range(len(day)):
        for j in range(len(day[0])):
            if day[i][j] == "S":
                day[i][j] = "a"
                s = [i, j]
            if day[i][j] == "E":
                day[i][j] = "z"
                e = [i, j]
    # print("e:", e)
    to_go[e[0]][ e[1]]=0
    path_rec(e[0], e[1], 1)
    # print(to_go)
    return to_go[s[0]][s[1]]


print(part1(day))


def part2(day):
    to_go = new_table(len(day[0]), len(day), 10 ** 10)

    # print(to_go[2][7])

    def path_rec(i, j, long):
        nonlocal to_go
        for dir in DIRS_4:

            if -1 < i + dir.x < len(day) and -1 < j + dir.y < len(day[0]):
                # print(i + dir.x, j + dir.y, ord(day[i + dir.x][j + dir.y]), ord(day[i][j]))
                if ord(day[i + dir.x][j + dir.y]) >= (ord(day[i][j]) - 1) and to_go[i + dir.x][j + dir.y] > long:
                    to_go[i + dir.x][j + dir.y] = long
                    path_rec(i + dir.x, j + dir.y, long + 1)

    a_elev = []
    for i in range(len(day)):
        for j in range(len(day[0])):
            if day[i][j] == "S":
                day[i][j] = "a"
            if day[i][j] == "E":
                day[i][j] = "z"
                e = [i, j]
            if day[i][j] == "a":
                a_elev.append([i,j])
    # print("e:", e)
    to_go[e[0]][e[1]] = 0
    path_rec(e[0], e[1], 1)
    min_path = 10**5
    for x in a_elev:
        if to_go[x[0]][x[1]]<min_path:
            min_path=to_go[x[0]][x[1]]
    return min_path

print(part2(day2))
