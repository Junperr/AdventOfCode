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
import time

pyperclip.copy("""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=5, sample=None)
dayp2 = copy.deepcopy(day)
deb = time.perf_counter_ns()


def get_dict(par):
    d = {}
    for line in par.split("\n")[1:]:
        if line != "":
            valb, keyb, rangeb = map(int, line.split())
            d[(keyb, keyb + rangeb)] = valb
    return d


def find_me(d, x):
    for a, b in d.keys():
        if a <= x <= b:
            return d[(a, b)] + x - a
    return x


def part1(day):
    input = day.input
    par = input.split("\n\n")
    seeds = list(map(int, par[0].split()[1:]))
    stos = get_dict(par[1])
    stof = get_dict(par[2])
    ftow = get_dict(par[3])
    wtol = get_dict(par[4])
    ltot = get_dict(par[5])
    ttoh = get_dict(par[6])
    htol = get_dict(par[7])
    pos = []

    for x in seeds:
        cur = find_me(stos, x)
        cur = find_me(stof, cur)
        cur = find_me(ftow, cur)
        cur = find_me(wtol, cur)
        cur = find_me(ltot, cur)
        cur = find_me(ttoh, cur)
        cur = find_me(htol, cur)
        pos.append(cur)

    return min(pos)


part1(day)
print(time.perf_counter_ns() - deb, "time P1")
print(part1(day))
deb = time.perf_counter_ns()


def split_inter(d, inters):
    interss = []
    still = copy.deepcopy(inters)

    while still:

        a, b = still.pop()
        added = False
        for a1, b1 in d.keys():
            dec = d[(a1, b1)]
            if a1 <= a <= b1 and a1 <= b <= b1:
                interss.append((dec + a - a1, dec + b - a1))
                added = True
            elif a1 <= b <= b1:
                interss.append((dec, dec + b - a1))
                still.append((a, a1 - 1))
                added = True
            elif a1 <= a <= b1:
                interss.append((dec + a - a1, dec + b1 - a1))
                still.append((b1 + 1, b))
                added = True
            elif a < a1 and b > b1:
                interss.append((dec, dec + b1 - a1))
                still.append((a, a1 - 1))
                still.append((b1 + 1, b))
                added = True
        if not added:
            interss.append((a, b))

    return interss


def part2(day):
    input = day.input
    par = input.split("\n\n")

    seeds = []
    seedy = list(map(int, par[0].split()[1:]))
    for i in range(0, len(seedy), 2):
        seeds.append((seedy[i], seedy[i] + seedy[i + 1]))

    stos = get_dict(par[1])
    stof = get_dict(par[2])
    ftow = get_dict(par[3])
    wtol = get_dict(par[4])
    ltot = get_dict(par[5])
    ttoh = get_dict(par[6])
    htol = get_dict(par[7])

    seeds = split_inter(stos, seeds)
    seeds = split_inter(stof, seeds)
    seeds = split_inter(ftow, seeds)
    seeds = split_inter(wtol, seeds)
    seeds = split_inter(ltot, seeds)
    seeds = split_inter(ttoh, seeds)
    seeds = split_inter(htol, seeds)

    return min(seeds)[0]


part2(dayp2)
print(time.perf_counter_ns() - deb, "time P2")
print(part2(dayp2))
