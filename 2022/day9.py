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

pyperclip.copy("""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=9)
day = day.l()
print(DIRS_4,DIRS_8,DIRS)
print ((Point(0,0) +Point(2,0)).div(2))
def part1(day):
    pos = set()
    h = Point(0,0)
    t = Point(0,0)
    pos.add(t)
    dirs = ["U","R","D","L"]
    for x in day:
        x = x.split()
        x[1]= int(x[1])
        print(x)
        for i in range (x[1]):
            prev  = h
            h += DIRS_4[dirs.index(x[0])]
            if h.dist_manhattan(t)>1 and t not in h.neighbours_8():
                t = prev
                pos.add(t)
    print(len(pos))


    pass

print(part1(day))


def part2(day):
    pos = set()
    h = Point(0, 0)
    t = [Point(0, 0) for _ in range(9)]
    pos.add(t[8])
    dirs = ["U", "R", "D", "L"]
    unlock = [False for _ in range(9)]
    count = 0
    for x in day:
        count +=1
        x = x.split()
        x[1] = int(x[1])
        for i in range(x[1]):
            prev = h
            h += DIRS_4[dirs.index(x[0])]
            if h.dist_manhattan(t[0]) > 1 and t[0] not in h.neighbours_8():
                move = prev
                move -= t[0]
                prevt = t[0]
                t[0] = prev
                unlock[0] = True

            for ind in range(1,9):
                if t[ind-1].dist_manhattan(t[ind]) > 1 and t[ind] not in t[ind-1].neighbours_8():
                    if t[ind-1].dist_manhattan(t[ind]) == 2 and (t[ind-1].dist_manhattanx(t[ind]) == 2 or t[ind-1].dist_manhattany(t[ind]) == 2):
                        move = (t[ind-1] + t[ind]).div(2).int() - t[ind]
                        prevt = t[ind]
                        t[ind] = (t[ind-1] + t[ind]).div(2).int()
                    else:
                        test = t[ind]
                        test += move
                        if min(t[ind-1].dist_manhattan(test),t[ind-1].dist_manhattan(prevt)) == t[ind-1].dist_manhattan(prevt):
                            move = prevt
                            move -= t[ind]
                            t[ind],prevt = prevt,t[ind]

                        else:
                            prevt = t[ind]
                            t[ind] += move
                    unlock[ind] = True
            pos.add(t[8])
            # grid = new_table(50, 50, ".")
            # grid[0+25][0+25]="s"
            # for i in range (8,-1,-1):
            #     grid[t[i].y+25][t[i].x+25] = str(i+1)
            # grid[h.y+25][h.x+25] = "H"
            # print_grid(grid)
        # if count == 3:
        #     break
    print(len(pos))

    pass
    pass

print(part2(day))