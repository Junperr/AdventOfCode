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


pyperclip.copy("""""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=15, sample=None)


def part1(day):
    s1 = 0
    for x in day.input.strip().split(","):
        s = 0
        for k in x:
            s += ord(k)
            s = s * 17
            s = s % 256
        s1 += s
    return s1
    pass


dayp2 = copy.deepcopy(day)
print(part1(day))


def part2(day):
    boxs = {}
    for x in day.input.strip().split(","):

        if x[-1] == "-":
            s = 0
            for k in x[:-1]:
                s += ord(k)
                s = s * 17
                s = s % 256
            new = []
            for k in boxs.get(s, []):
                if k[0] != x[:-1]:
                    new.append(k)
            boxs[s] = new
        else:
            a, b = x.split("=")
            s = 0
            for k in a:
                s += ord(k)
                s = s * 17
                s = s % 256
            new = []
            switch = False
            for k in boxs.get(s, []):
                if k[0] == a:
                    new.append((a,b))
                    switch = True
                else:
                    new.append(k)
            if not switch:
                new.append((a, b))
            boxs[s] = new
    score = 0
    for a,b in boxs.items():
        for j,k in enumerate(b):
            score += (a+1) * (j+1) * int(k[1])
    # print(boxs)
    return score


print(part2(dayp2))
