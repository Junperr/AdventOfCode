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


pyperclip.copy("""1
2
-3
3
-2
0
4""")
clip = pyperclip.paste()
day = parsing.Day(year=2022, day=1, sample=clip)
# day = parsing.Day(year=2022, day=20)
day = parse_nums(day.input)

# def move_f(l, i, j):
#     for ind in range(i + 1, j + 1):
#         l[ind], l[ind - 1] = l[ind - 1], l[ind]
#     return l
#
#
# def move_b(l, i, j):
#     for ind in range(i, j, -1):
#         l[ind], l[ind - 1] = l[ind - 1], l[ind]
#     return l


# print(move_f(day, 0, 1))
# print(move_f(day, 0, 2))
# print(move_b([1, 2, -3, 0, 3, 4, -2], 5, 3))

# print(move_f([1, -3, 2, 3, -2, 0, 4],1,5))
occ = {}
for x in day:
    occ[x] = occ.get(x, 0) + 1


# print(occ)


# def part1(day):
#     n = len(day)
#     new = copy.deepcopy(day)
#     for x in day:
#         # print(new)
#         ind = new.index(x)
#         if  x >= 0:
#             if (ind + x ) % n >= ind:
#                 # print("1", ind, (ind + x) % n)
#                 new = move_f(new, ind, (ind + x ) % n)
#             else:
#                 # print("2", ind, (ind + x+1) % n)
#                 new = move_b(new, ind, (ind + x + 1) % n)
#         else:
#             if (ind + x -1) % n >= ind:
#                 # print("3", ind, (ind + x) % n)
#                 new = move_f(new, ind, (ind + x -1) % n)
#             else:
#                 # print("4", ind, (ind + x-1) % n)
#                 new = move_b(new, ind, (ind + x -1) % n)
#     ind0 = new.index(0)
#     # print(new,new[(ind0+1000)%n] , new[(ind0+2000)%n] , new[(ind0+3000)%n])
#
#     return new[(ind0+1000)%n] + new[(ind0+2000)%n] + new[(ind0+3000)%n]

def move_f(l, index, ori, i, j):
    for ind in range(i + 1, j + 1):
        id1, id2 = index.index(ind), index.index(ind - 1)
        l[ind], l[ind - 1] = l[ind - 1], l[ind]
        index[id1], index[id2] = index[id2], index[id1]

    return l


def move_b(l, index, ori, i, j):
    for ind in range(i, j, -1):
        id1, id2 = index.index(ind), index.index(ind - 1)
        l[ind], l[ind - 1] = l[ind - 1], l[ind]
        index[id1], index[id2] = index[id2], index[id1]
    return l


print(len(day))


def part1(day):
    n = len(day)
    new = copy.deepcopy(day)
    indexes = [y for y in range(len(day))]
    for i in range(len(day)):
        # print(i)
        x = day[i]
        # print(new)
        ind = indexes[i]
        show = [0 for j in range(len(day))]
        for j in range (len(day)):
            show[indexes[j]] = day[j]
        # print(indexes)
        # break
        if x >= 0:
            if (ind + x) % n >= ind:
                # print("1", x, ind, (ind + x) % n, "\n", indexes, show, new)
                new = move_f(new, indexes, day, ind, (ind + x) % n)
            else:
                # print("2", x, ind, (ind + x + 1) % n, "\n", indexes, show, new)
                new = move_b(new, indexes, day, ind, (ind + x + 1) % n)
        else:
            if (ind + x - 1) % n >= ind:
                # print("3", x, ind, (ind + x - 1) % n, "\n", indexes, show, new)
                new = move_f(new, indexes, day, ind, (ind + x - 1) % n)
            else:
                # print("4", x, ind, (ind + x ) % n, "\n", indexes, show, new)
                new = move_b(new, indexes, day, ind, (ind + x ) % n)
    ind0 = new.index(0)
    # print(new,new[(ind0+1000)%n] , new[(ind0+2000)%n] , new[(ind0+3000)%n])
    print("", indexes, new)
    return new[(ind0 + 1000) % n] + new[(ind0 + 2000) % n] + new[(ind0 + 3000) % n]


dayp2 = copy.deepcopy(day)
print(part1(day))


def part2(day):
    pass


print(part2(dayp2))
