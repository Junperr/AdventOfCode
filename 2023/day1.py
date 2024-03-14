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
import time

# pyperclip.copy("""""")
# clip = pyperclip.paste()

day = parsing.Day(year=2023, day=1)
deb = time.time()
def part1(day):
    s= 0
    for l in day.l():
        first , last = -1,-1
        for x in l:
            if ord(x)<58 and ord(x)>47:
                if first == -1:
                    first = int(x)
                last = int(x)
        if last != -1 and first != -1:
            s += 10*first + last
    return s
dayp2 = copy.deepcopy(day)
print(part1(day))

def part2(day):
    s = 0
    for l in day.l():
        first, last = -1, -1
        for i in range(len(l)):
            x = l[i]
            if ord(x) < 58 and ord(x) > 47:
                if first == -1:
                    first = int(x)
                last = int(x)
            else:
                num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
                for j in range(10):
                    if l[i:i+len(num[j])] == num[j]:
                        if first == -1:
                            first = j
                        last = j

        if last != -1 and first != -1:
            s += 10 * first + last
    return s


print(part2(dayp2))
print(time.time() - deb)