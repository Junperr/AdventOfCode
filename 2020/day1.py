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


# day  .input .l .par .b2d
tot = 0
res = []

# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2020, day=1)
lines = day.l(True)
stock = []
for i in range (len(lines)):
    if lines[i] in stock:
        print(lines[i]*(2020-lines[i]))
    stock.append(2020-lines[i])

for i in range(len(lines)):
        for j in range(len(lines)):
            if i!=j:
                if 2020-lines[i]-lines[j] in lines :
                    idexes = [ind for ind, x in enumerate(lines) if x == 2020-lines[i]-lines[j]]
                    if i in idexes : lim = 1
                    else : lim = 0
                    if j in idexes : lim += 1
                    if len(idexes)> lim:
                        print( (2020-lines[i]-lines[j])*lines[i]*lines[j])

######bad solution but the first one i got :

# for i in permutations([i for i in range (len(lines))], 3):
#     s = 0
#     for x in i:
#         s+= lines[x]
#     if s == 2020:
#         p=1
#         for x in i:
#             p *= lines[x]
#         print(p)