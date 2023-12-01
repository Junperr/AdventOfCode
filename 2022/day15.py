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


pyperclip.copy("""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=15)
day = day.l()
day = list(map(parse_nums, day))

def point_list(l):
    return Point(l[0], l[1]), Point(l[2], l[3])

day = list(map(point_list, day))


def part1(day, line=2000000):
    minx, maxx = day[0][0].x, day[0][0].x
    max_dist = 0
    not_possible = set()
    for x in day:
        s = x[0]
        b = x[1]
        minx = min(minx, s.x, b.x)
        maxx = max(maxx, s.x, b.x)
        dist = s.dist_manhattan(b)
        if dist>max_dist:
            max_dist = dist
        distl = s.dist_manhattan(Point(s.x,line))
        if distl<=dist:
            for j in range (s.x-(dist-distl),s.x+(dist-distl)+1):
                not_possible.add(j)

    for ind in range (len(day)):
        if day[ind][1].y==line:
            if day[ind][1].x in not_possible:
                not_possible.remove(day[ind][1].x)
    return len(not_possible)

import timeit
# nb = int(input())
# s=0
# for _ in range (nb):
#     debtime = timeit.default_timer()
#     part1(day)
#     s+=timeit.default_timer() - debtime
# print(s/nb)

dayp2 = copy.deepcopy(day)
# print(part1(day))

def gen_point(d):
    points = set()
    for i in range(d+1):
        points.add(Point(i,d-i))
        points.add(Point(i*-1, (d - i)*-1))
        points.add(Point(i , (d - i) * -1))
        points.add(Point(i * -1, (d - i) ))
    return points

def part2(day):
    for line in day:
        gen_dist = line[0].dist_manhattan(line[1])
        for new_pts in gen_point(gen_dist+1):
            cand = line[0]+new_pts
            if 0<=cand.x<=4000000 and 0<=cand.y<=4000000:
                yep = True
                for x in day:
                    s = x[0]
                    b = x[1]
                    dist = s.dist_manhattan(b)
                    if s.dist_manhattan(cand) <= dist:
                        yep = False
                        break
                if yep:
                    return cand.x * 4000000 + cand.y
    return "fail"

debtime = timeit.default_timer()
print(part2(dayp2))
print(timeit.default_timer()-debtime)