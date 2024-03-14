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


def test(day):
    dayp1, dayp2 = copy.deepcopy(day), copy.deepcopy(day)
    timep1 = 0
    countp1 = 0
    while timep1 < 10 ** 9:
        countp1 += 1
        newdayp1 = copy.deepcopy(dayp1)
        deb = time.perf_counter_ns()
        part1(dayp1)
        timed = time.perf_counter_ns() - deb
        dayp1 = newdayp1
        timep1 += timed
    print(f"Part1 : runned {countp1} average of {timep1 / countp1} ns/operation")


test(day)

dayp2 = copy.deepcopy(day)
deb = time.perf_counter()

# part1(day)
# print(time.perf_counter() - deb, "time P1")
print(part1(day))
deb = time.perf_counter()


def split_inter(d, inters):
    interss = []  # les intervals mapper pour le dictionnaire d
    still = copy.deepcopy(inters)  # mes intervals actuel

    while still:  # tant que j ai des interval non mapper

        a, b = still.pop()  # je recupere les borne d' un interval pas encore mapper
        added = False  # un booleen savoir si l interval sera mapper a la fin ou reste le meme
        for a1, b1 in d.keys():  # on itere sur les intervals de mon dictionnaire
            dec = d[(a1, b1)]  # on stock la valeur auquel remapper si il faut
            if a1 <= a <= b1 and a1 <= b <= b1:  # [a,b] inclu dans [a1,b1]
                interss.append((dec + a - a1, dec + b - a1))
                added = True
                break
            elif a1 <= b <= b1:  # b inclu dans [a1,b1] mais pas a cela rajoute le segment [a,a1-1] dans les segment a traiter (ca depasse a gauche)
                interss.append((dec, dec + b - a1))
                still.append((a, a1 - 1))
                added = True
                break
            elif a1 <= a <= b1:  # a inclu dans [a1,b1] mais pas b cela rajoute le segment [b+1,b] dans les segment a traiter (ca depasse a droite)
                interss.append((dec + a - a1, dec + b1 - a1))
                still.append((b1 + 1, b))
                added = True
                break
            elif a < a1 and b > b1:  # [a1,b1] inclu dans [a,b] cela rajoute les 2 segment precedent (ce qui depasse a droite et a gauche)
                interss.append((dec, dec + b1 - a1))
                still.append((a, a1 - 1))
                still.append((b1 + 1, b))
                added = True
                break
        if not added:  # [a,b] inter [a1,b1] est vide
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


# part2(dayp2)
# print(time.perf_counter() - deb, "time P2")
print(part2(dayp2))

test(day)
