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


pyperclip.copy("""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=7, sample=None)

def compcards(cards):
    c = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]
    return [c.index(cards[0]),c.index(cards[1]),c.index(cards[2]),c.index(cards[3]),c.index(cards[4])]
def compcardsP1(cards):
    c = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    return [c.index(cards[0]),c.index(cards[1]),c.index(cards[2]),c.index(cards[3]),c.index(cards[4])]

def part1(day):
    comps = []
    for l in day.l():
        occ = {}
        cards, score = l.split()
        score = int(score)
        cards = compcardsP1(cards)
        for c in cards:
            occ[c] = occ.get(c,0) + 1
        occI = sorted(occ.items(), key=lambda item: [item[1],item[0]], reverse=True)
        comp = sorted(list(occ.values()), reverse=True)
        comp = comp + cards + [score]
        comps.append(comp)

    comps.sort()

    s = 0
    for i in range(len(comps)):
        s += comps[i][-1]*(i+1)
    return s

dayp2 = copy.deepcopy(day)
print(part1(day))

def part2(day):
    comps = []
    for l in day.l():
        occ = {}
        cards, score = l.split()
        cardss = cards
        score = int(score)
        cards = compcards(cards)
        for c in cards:
            occ[c] = occ.get(c,0) + 1
        occI = sorted(occ.items(), key=lambda item: [item[1],item[0]], reverse=True)

        if occ.get(0,0)!=0:
            if occI[0][0] == 0 and len(occI)>1:
                occ[occI[1][0]] += occ.get(0,0)
            if len(occI) > 1:
                occ[occI[0][0]] += occ.get(0, 0)
                del occ[0]

        comp = sorted(list(occ.values()), reverse=True)
        comp = comp + cards + [score,cardss]
        comps.append(comp)

    comps.sort()

    s = 0
    for i in range(len(comps)):
        s += comps[i][-2]*(i+1)
    return s

print(part2(dayp2))