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

clip = ""
pyperclip.copy("""inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2""")
# clip = pyperclip.paste()
day = parsing.Day(year=2021, day=24, sample=clip)


def isvar(b):
    vars = set()
    vars.add("w")
    vars.add("x")
    vars.add("y")
    vars.add("z")
    return b in vars


def part1(day):
    register = {"w": 0, "x": 0, "y": 0, "z": 0}
    for i in range(10**14,10**13,-1):
        inputval = str(i)
        count = 0
        for line in day.l():
            print(register)
            if line[:3] == "inp":
                ins, var = line.split()
                register[var] = int(inputval[count])
                count += 1
            else:
                ins, a, b = line.split()
                if ins == "add":
                    if isvar(b):
                        register[a] = register[a] + register[b]
                    else:
                        register[a] = register[a] + int(b)
                elif ins == "mul":
                    if isvar(b):
                        register[a] = register[a] * register[b]
                    else:
                        register[a] = register[a] * int(b)
                elif ins == "div":
                    if isvar(b):
                        register[a] = register[a] // register[b]
                    else:
                        register[a] = register[a] // int(b)
                elif ins == "mod":
                    if isvar(b):
                        register[a] = register[a] % register[b]
                    else:
                        register[a] = register[a] % int(b)
                elif ins == "eql":
                    if isvar(b):
                        register[a] = int(register[a] == register[b])
                    else:
                        register[a] = int(register[a] == int(b))
            if register["z"]==0:
                return i
    return register


dayp2 = copy.deepcopy(day)
print(part1(day))


def part2(day):
    pass


print(part2(dayp2))
