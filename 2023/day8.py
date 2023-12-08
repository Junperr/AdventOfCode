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


pyperclip.copy("""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=8, sample=None)


def part1(day):
    l = day.l()
    seq = l[0]
    travel = {}
    for i in range(2, len(l)):
        base, lr = l[i].split(" = ")
        left = lr[1:4]
        right = lr[6:9]
        travel[base] = (left, right)

    cur = "AAA"
    count = 0
    while cur != "ZZZ":

        if seq[count % len(seq)] == "R":
            cur = travel[cur][1]
        else:
            cur = travel[cur][0]
        count += 1
    return count



dayp2 = copy.deepcopy(day)


print(part1(day))

def part2(day):
    l = day.l()
    seq = l[0]
    travel = {}
    cur = []
    sol = set()
    for i in range(2, len(l)):
        base, lr = l[i].split(" = ")
        if base[-1] == "A":
            cur.append(base)
        if base[-1] == "Z":
            sol.add(base)
        left = lr[1:4]
        right = lr[6:9]
        travel[base] = (left, right)

    cycle = [(-1, "")] * len(cur)
    for i in range(len(cur)):

        count = 0
        while cur[i] not in sol:

            if seq[count % len(seq)] == "R":
                cur[i] = travel[cur[i]][1]
            else:
                cur[i] = travel[cur[i]][0]
            count += 1

        cycle[i] = (count, seq[count % len(seq):] + seq[:count % len(seq)])

    sol = 1
    for c in cycle:
        sol = lcm(sol, c[0])

    return int(sol)


print(part2(dayp2))
