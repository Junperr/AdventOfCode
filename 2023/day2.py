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


pyperclip.copy("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=2, sample=None)

def part1(day):
    s = 0
    count = 1
    for l in day.l():
        # print(count)
        _,r = l.split(":")
        round = r.split(";")
        mr, mb, mg = 0, 0, 0
        for i in range(len(round)):
            cur = {}
            types = round[i].split(",")
            for t in types:
                val,name = t.split()
                cur[name] = cur.get(name,0) + int(val)
                if "red" in cur:
                    mr = max(mr,cur["red"])
                if "blue" in cur:
                    mb = max(mb,cur["blue"])
                if "green" in cur:
                    mg = max(mg,cur["green"])
                # print(t,i,cur,mr,mb,mg)
        if mr<=12 and mb<=14 and mg<=13:
            # print(count,mr,mb,mg)
            s += count
        count+=1
    return s


    pass
dayp2 = copy.deepcopy(day)
print(part1(day))

def part2(day):
    s = 0
    count = 1
    for l in day.l():
        # print(count)
        _,r = l.split(":")
        round = r.split(";")
        mr, mb, mg = 0, 0, 0
        for i in range(len(round)):
            cur = {}
            types = round[i].split(",")
            for t in types:
                val,name = t.split()
                cur[name] = cur.get(name,0) + int(val)
                if "red" in cur:
                    mr = max(mr,cur["red"])
                if "blue" in cur:
                    mb = max(mb,cur["blue"])
                if "green" in cur:
                    mg = max(mg,cur["green"])
                # print(t,i,cur,mr,mb,mg)

            # print(count,mr,mb,mg)
        s += mr*mb*mg
        count+=1
    return s
    pass

print(part2(dayp2))