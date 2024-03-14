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


pyperclip.copy("""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=14, sample=None)

def rot(g):
    ng = []
    for i in range(len(g[0])):
        ng.append(["."]*len(g))
    for i in range(len(g)):
        for j in range(len(g[0])):
            ng[j][len(g)-i-1] = g[i][j]
    return ng

def move(d):
    for _ in range(100):
        d = map(lambda s: s.replace('.O', 'O.'), d)
    return d

def tilt(d):
    return map(''.join, zip(*d))

def load(d):
    return sum(i*(c=='O') for col in d
        for i,c in enumerate(col[::-1], 1))



def part1(day):
    g = day.b2d()
    for i in range(len(g)):
        print(*g[i],sep="")
    print("rot\n\n")
    print(*list(tilt(g)),sep="\n")
    print(load(move(tilt(g))))
    #
    # ng = []
    # for i in range(len(g)):
    #     ng.append(["."]*len(g[0]))
    # s = 0
    # h = len(g)
    # rotg = rot(g)
    # for i in range(len(rotg)):
    #     print(*rotg[i],sep="")
    # for j in range(len(g[0])):
    #     last = 0
    #     count = 0
    #     for i in range(len(g)):
    #         if g[i][j] == "#":
    #             # print(j,i,last,count)
    #             for i1 in range(last,last+count):
    #                 if last == 0:
    #                     ng[i1][j] = "O"
    #                     s += h - i1
    #                 else:
    #                     ng[i1 + 1][j] = "O"
    #                     s += h - (i1 + 1)
    #             ng[i][j] = "#"
    #             last = i
    #             count = 0
    #         elif g[i][j] == "O":
    #             count += 1
    #     if count > 0:
    #
    #         for i1 in range(last, last + count):
    #             if last == 0:
    #                 ng[i1][j] = "O"
    #                 s += h - i1
    #             else:
    #                 ng[i1 + 1][j] = "O"
    #                 s += h - (i1+1)
    #
    # for i in range(len(g)):
    #     print(*ng[i],sep="")
    # # print(*ng,sep="\n")
    # s2 = 0
    # for i in range(len(g)):
    #     print(i,h-i)
    #     for j in range(len(g[0])):
    #         if ng[i][j] == "O":
    #             s2 += h-i
    # return s,s2
    pass

dayp2 = copy.deepcopy(day)
print(part1(day))

def part2(day):

    pass

print(part2(dayp2))