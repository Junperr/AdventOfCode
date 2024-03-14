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


pyperclip.copy("""1 3 20 74 204 488 1090 2344 4898 9972 19850 38845 75167 144405 275720 522347 978623 1806489 3275240 5819188 10118814""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=9, sample=None)


def part1(day):
    trues = 0
    for l in day.l():
        l = list(map(int, l.split()))
        work = True
        for i in range(len(l)):
            if l[i] != 0:
                work = False
        keep = [l[-1]]
        while not work:
            next = []
            work = True
            for i in range(1, len(l)):
                next.append(l[i] - l[i - 1])
                if next[-1] != 0:
                    work = False
            if next:
                keep.append(next[-1])
            l = next
        trues += sum(keep)

    return trues


dayp2 = copy.deepcopy(day)
print(part1(day))


def part2(day):
    trues = 0
    for l in day.l():
        l = list(map(int, l.split()))[::-1]
        work = True
        for i in range(len(l)):
            if l[i] != 0:
                work = False
        keep = [l[-1]]
        while not work:
            next = []
            work = True
            for i in range(1, len(l)):
                next.append(l[i] - l[i - 1])
                if next[-1] != 0:
                    work = False
            if next:
                keep.append(next[-1])
            l = next
        trues += sum(keep)

    return trues

    pass


print(part2(dayp2))
