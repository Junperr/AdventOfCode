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


# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=10)
day = day.l()
print(day)
def part1(day):
    X = 1
    res = 1
    op = [X]
    print(len(day))
    for x in day:
        x = x.split()

        if x[0] ==  "noop":
            op.append(X)
        else:
            x[1] = int(x[1])
            op.append(X)
            X = X + x[1]
            op.append(X)
    s=0

    for i in range(19,len(op),40):
        print(str((i+1)*op[i]),i)
        s += (i+1)*op[i]
    return s,op
    pass

# print(part1(day))

def part2(day):
    X = 1
    count=0
    img = ["","","","","",""]
    op = [X]
    print(len(day))
    for x in day:
        x = x.split()
        print(count)
        if x[0] == "noop":
            if X-1<=count%40<X+2:
                img[count//40] =  img[count//40] + "#"
            else:
                img[count // 40] = img[count // 40] + "."
            op.append(X)
            count+=1
        else:
            x[1] = int(x[1])
            if X-1<=count%40<X+2:
                img[count//40] =  img[count//40] + "#"
            else:
                img[count // 40] = img[count // 40] + "."
            count+=1
            op.append(X)
            if X-1<=count%40<X+2:
                img[count//40] =  img[count//40] + "#"
            else:
                img[count // 40] = img[count // 40] + "."
            count+=1
            X = X + x[1]
            op.append(X)
    s = 0
    for i in range(6):
        print(img[i])
    # for i in range(19, len(op), 40):
    #     print(str((i + 1) * op[i]), i)
    #     s += (i + 1) * op[i]
    return s, op
    pass

print(part2(day))