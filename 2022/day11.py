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

pyperclip.copy("""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=11)
day = day.l()
day1 = []
current = []
for i in range(0, len(day), 7):
    day1.append(day[i:i + 6])
# print(day1)
#
# print(len("  Starting items: "), len("  Operation: new = "), len("  Test: divisible by "),
#       len("    If true: throw to monkey "), len("    If false: throw to monkey "))

def part1(day):
    monk = []
    monk_item = []
    count = [0 for _ in range(len(day))]
    for x in day:
        current = []
        monk_item.append(list(map(int, x[1][18:].split(","))))
        current.append(x[2][19:])
        current.append(int(x[3][21:]))
        current.append(int(x[4][29:]))
        current.append(int(x[5][30:]))
        monk.append(current)
    # print(monk, monk_item)
    for _ in range(20):
        for i in range(len(monk)):
            # print(len(monk_item[i]))
            current = monk_item[i].copy()
            for ind in range(len(monk_item[i])):
                count[i] += 1
                old = current[ind]
                new = eval(monk[i][0])//3
                # print(old,new,i)
                if new % monk[i][1] == 0: #
                    # print(monk[i][2])
                    monk_item[monk[i][2]].append(new)
                else:
                    # print(monk[i][3])
                    monk_item[monk[i][3]].append(new)
                monk_item[i].pop(0)
    #     break
    # print(monk_item)
    count.sort()
    print(count[-1]*count[-2])

    pass


print(part1(day1))


def part2(day):
    monk = []
    monk_item = []
    count = [0 for _ in range(len(day))]
    for x in day:
        current = []
        monk_item.append(list(map(int, x[1][18:].split(","))))
        current.append(x[2][19:])
        current.append(int(x[3][21:]))
        current.append(int(x[4][29:]))
        current.append(int(x[5][30:]))
        monk.append(current)
    # print(monk, monk_item)
    maxn = lcm(monk[0][1],monk[1][1])
    for z in range (2,len(monk)):
        maxn = lcm(maxn,monk[z][1])
    # print(int(maxn))
    for _ in range(10000):
        for i in range(len(monk)):
            # print(len(monk_item[i]))
            current = monk_item[i].copy()
            for ind in range(len(monk_item[i])):
                count[i] += 1
                old = current[ind]
                new = eval(monk[i][0])%maxn
                # print(old,new,i)
                if new % monk[i][1] == 0: #
                    # print(monk[i][2])
                    monk_item[monk[i][2]].append(new)
                else:
                    # print(monk[i][3])
                    monk_item[monk[i][3]].append(new)
                monk_item[i].pop(0)
    #     break
    # print(monk_item)
    count.sort()
    return count[-1]*count[-2]

    pass


print(part2(day1))
