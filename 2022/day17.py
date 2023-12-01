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

t = open("day17_proofread.txt", "r").read().split("\n")
pyperclip.copy(""">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=17)
day = day.input.strip()
blocs = [[Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)],
         [Point(0, 1), Point(1, 1), Point(2, 1), Point(1, 2), Point(1, 0)],
         [Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1), Point(2, 2)],
         [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)],
         [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]]
h_mv = {"<": Point(-1, 0), ">": Point(1, 0)}


# def part1(day):
#     global blocs, h_mv
#
#     hight = [0 for _ in range(7)]
#     count = 0
#     for nb in range(2022):
#         bloc = list(map(lambda x: x + Point(2, max(hight) + 4), blocs[nb % 5]))
#         fixed = False
#         while not fixed:
#             # print(bloc)
#             prev = copy.deepcopy(bloc)
#             bloc = list(map(lambda x: x + h_mv[day[count % len(day)]], bloc))
#             for i in range(len(bloc)):
#                 if bloc[i].x == 7 or bloc[i].x == -1 or bloc[i].y == hight[bloc[i].x]:
#                     bloc = prev
#                     break
#             count+=1
#             # if count%500 == 0:
#             print(count,bloc,hight)
#             if count > 500:
#                 return None
#             prev = copy.deepcopy(bloc)
#             bloc = list(map(lambda x: x + Point(0,-1), bloc))
#             for i in range(len(bloc)):
#                 if bloc[i].y == hight[bloc[i].x]:
#                     fixed = True
#                     bloc = prev
#                     break
#         for i in range(len(bloc)):
#             hight[bloc[i].x] = max(bloc[i].y, hight[bloc[i].x])
#         # print(max(hight)== int(t[nb]))
#     # print(count)
#     return max(hight)

def part1(day):
    global blocs, h_mv

    hight = [copy.deepcopy(["#"]) for _ in range(7)]
    count = 0
    for nb in range(2022):
        hmax = 0
        for i in range(7):
            hmax = max(hmax, len(hight[i]) - 1 - hight[i][::-1].index("#"))
        # print(hmax)
        # print_grid(rotated(rotated(rotated(hight))))
        bloc = list(map(lambda x: x + Point(2, hmax + 4), blocs[nb % 5]))
        fixed = False
        while not fixed:

            for i in range(len(bloc)):
                # print(bloc[i].y, len(hight[i])-1)
                while bloc[i].y > len(hight[i]) - 1:
                    for z in range(7):
                        hight[z].append(".")
            # print_grid(hight)
            # if len(hight[0])%200 == 0:
            # print(len(hight[0]))
            # print(bloc)
            prev = copy.deepcopy(bloc)
            bloc = list(map(lambda x: x + h_mv[day[count % len(day)]], bloc))
            # print([len(hight[x]) for x in range(7)])
            # print(hight,bloc)

            for i in range(len(bloc)):
                # print(bloc[i])
                if bloc[i].x == 7 or bloc[i].x == -1 or hight[bloc[i].x][bloc[i].y] == "#":
                    bloc = prev
                    break
            count += 1
            prev = copy.deepcopy(bloc)
            bloc = list(map(lambda x: x + Point(0, -1), bloc))
            for i in range(len(bloc)):
                if hight[bloc[i].x][bloc[i].y] == '#':
                    fixed = True
                    bloc = prev
                    break
        for i in range(len(bloc)):
            hight[bloc[i].x][bloc[i].y] = "#"
    for i in range(7):
        hmax = max(hmax, len(hight[i]) - 1 - hight[i][::-1].index("#"))
    return hmax


dayp2 = copy.deepcopy(day)
print(part1(day))


def part2(day):
    global blocs, h_mv
    hight = [copy.deepcopy(["#"]) for _ in range(7)]
    count = 0
    cutted = 0
    stock = []
    possible_match = []
    for nb in range(10000):

        hmax = 0
        hmin = len(hight[0])
        for i in range(7):
            current = len(hight[i]) - 1 - hight[i][::-1].index("#")
            hmax = max(hmax, current)
            hmin = min(hmin, current)
        bloc = list(map(lambda x: x + Point(2, hmax + 4 ), blocs[nb % 5]))
        fixed = False
        stock.append(cutted+hmax)
        if nb > 0:
            # print(nb,stock)
            print(stock[nb//2]*2,stock[nb],stock[nb//2]*2==stock[nb],nb)
            if stock[nb//2]*2==stock[nb]:
                print("yeah")
                possible_match.append(nb+1)
        # if nb%2000 == 0 :
        #     return stock
            # print(nb,cutted+hmax)
        while not fixed:

            for i in range(len(bloc)):
                while bloc[i].y > len(hight[i]) - 1:
                    for z in range(7):
                        hight[z].append(".")
            prev = copy.deepcopy(bloc)
            bloc = list(map(lambda x: x + h_mv[day[count % len(day)]], bloc))

            for i in range(len(bloc)):
                if bloc[i].x == 7 or bloc[i].x == -1 or hight[bloc[i].x][bloc[i].y] == "#":
                    bloc = prev
                    break
            count += 1
            prev = copy.deepcopy(bloc)
            bloc = list(map(lambda x: x + Point(0, -1), bloc))
            for i in range(len(bloc)):
                if hight[bloc[i].x][bloc[i].y] == '#':
                    fixed = True
                    bloc = prev
                    break
        for i in range(len(bloc)):
            hight[bloc[i].x][bloc[i].y] = "#"
        if hmin>500:
            # print(nb)
            cutted+=hmin
            for col in range(7):
                hight[col] = hight[col][hmin:]
    for i in range(7):
        hmax = max(hmax, len(hight[i]) - 1 - hight[i][::-1].index("#"))
    return cutted+hmax,possible_match


print(part2(dayp2))
# _,b = part2(dayp2)
# new = []
# for i in range (len(b)):
#     if b[i]*2 in b:
#         new.append(b[i])
# print(new)