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


pyperclip.copy("""1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=25)
day = day.l()


def part1(day):
    s = 0
    for line in day:
        current = 0
        for i in range(len(line)):
            if line[len(line) - 1 - i] == "=":
                # print(-2*(5**i))
                current += -2 * (5 ** i)
            elif line[len(line) - 1 - i] == "-":
                # print(-1 * (5 ** i))
                current += -1 * (5 ** i)
            elif line[len(line) - 1 - i] == "0":
                # print(0*(5**i))
                current += 0 * (5 ** i)
            elif line[len(line) - 1 - i] == "1":
                # print(1 * (5 ** i))
                current += 1 * (5 ** i)
            else:
                # print(2 * (5 ** i))
                current += 2 * (5 ** i)
        print(line, current)
        s += current

    def dec_tos5(num):
        ans = ""
        chars = ["0", "1", "2", "=", "-"]
        while num != 0:
            next = str(num % 5)
            if next == "3":
                num += 2
            if next == "4":
                num += 1
            ans = ans + chars[int(next)]
            # print(num)
            num = num // 5
            # print(num)
        return ans[::-1]
    return dec_tos5(s)


def dec_5(num):
    ans = ""
    while num != 0:
        ans = ans + str(num % 5)
        num = num // 5
    return ans[::-1]


def dec_tos5(num):
    ans = ""
    chars = ["0", "1", "2", "=", "-"]
    while num != 0:
        next = str(num % 5)
        if next == "3":
            num += 2
        if next == "4":
            num += 1
        ans = ans + chars[int(next)]
        # print(num)
        num = num // 5
        # print(num)
    return ans[::-1]


dayp2 = copy.deepcopy(day)
print(part1(day))


def part2(day):
    pass


print(part2(dayp2))
