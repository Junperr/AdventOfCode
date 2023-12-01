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


pyperclip.copy("""root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=21)
day = day.l()


def recup_data(l):
    a, b = l.split(":")
    b = b[1:].split()
    return [a] + b


day = list(map(lambda x: recup_data(x), day))
# print(day)


def part1(day):
    monkey = {}
    while monkey.get("root",True) == True:
        for i in range(len(day) - 1, -1, -1):
            if len(day[i]) == 4 and monkey.get(day[i][1], False) != False and monkey.get(day[i][3], False) != False:
                if day[i][2] == "*":
                    monkey[day[i][0]] = monkey[day[i][1]] * monkey[day[i][3]]
                elif day[i][2] == "-":
                    monkey[day[i][0]] = monkey[day[i][1]] - monkey[day[i][3]]
                elif day[i][2] == "+":
                    monkey[day[i][0]] = monkey[day[i][1]] + monkey[day[i][3]]
                elif day[i][2] == "/":
                    monkey[day[i][0]] = monkey[day[i][1]] / monkey[day[i][3]]
            elif len(day[i])==2:
                monkey[day[i][0]] = int(day[i][1])
        # print(monkey)
    return monkey["root"],monkey



dayp2 = copy.deepcopy(day)
# print(part1(day)[0])

dayp2v2 = {}
for x in dayp2:
    dayp2v2[x[0]] = x[1:]
# print(dayp2v2)
def part2(day,dayv1):
    monkey = part1(dayv1)[1]
    op = ""
    to_calc = set()
    to_calc.add("humn")
    prev=0
    while prev!=len(to_calc):
        prev = len(to_calc)
        for x in day.keys():
            if len(day[x])==3:
                if day[x][0] in to_calc:

                    if len(day[day[x][0]])==3:
                        print(eval(f"({day[day[x][0]][0]} {day[day[x][0]][1]} {day[day[day[x][0]][2]]})"))
                        day[x][0] = eval(f"({day[day[day[x][0]][0]]} {day[day[x][0]][1]} {day[day[day[x][0]][2]]})")
                    else:
                        # print(f"{day[day[x][0]][0]}")
                        day[x][0] = f"{day[day[x][0]][0]}"
                    to_calc.add(x)

                elif day[x][2] in to_calc:
                    if len(day[day[x][2]]) == 3:
                        print(eval(f"({day[day[x][2]][0]} {day[day[x][2]][1]} {day[day[day[x][2]][2]]})"))
                        day[x][2] = eval(f"({day[day[day[x][2]][0]]} {day[day[x][2]][1]} {day[day[day[x][2]][2]]})")
                    else:
                        # print(f"{day[day[x][2]][0]}")
                        day[x][2] = f"{day[day[x][2]][0]}"
                    to_calc.add(x)
                # print(x,day[x])
    for x in day.keys():
        if x not in to_calc:
            day[x] = monkey[x]

    print(day["root"])

    return to_calc


print(part2(dayp2v2,dayp2))
