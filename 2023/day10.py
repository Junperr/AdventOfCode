import os, sys, re, math, copy, fileinput
import time
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


pyperclip.copy(""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=10, sample=None)


def part1(day):
    g = day.b2d()
    adj = {}
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == "S":
                o = (i, j)
            adj[(i, j)] = []
            if g[i][j] == "-":
                for i1, j1 in [(0, 1), (0, -1)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))
            elif g[i][j] == "|":
                for i1, j1 in [(1, 0), (-1, 0)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))
            elif g[i][j] == "J":
                for i1, j1 in [(-1, 0), (0, -1)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))

            elif g[i][j] == "F":
                for i1, j1 in [(1, 0), (0, 1)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))

            elif g[i][j] == "L":
                for i1, j1 in [(-1, 0), (0, 1)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))

            elif g[i][j] == 7:
                for i1, j1 in [(1, 0), (0, -1)]:

                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))

            elif g[i][j] == "S":
                for i1, j1 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))
    trueadj = {}
    for key, v in adj.items():
        trueadj[key] = []
        for i in range(len(v)):
            if key in adj[v[i]]:
                trueadj[key].append(v[i])
        if len(trueadj[key]) == 0:
            del trueadj[key]
    print("graph")

    stack = deque()
    stack.append((o, 0))
    d = {o: 0}
    seen = set(o)
    while stack:
        cur, dist = stack.popleft()
        for next in trueadj[cur]:

            if next not in seen:
                seen.add(next)

                stack.append((next, dist + 1))
                d[next] = min(dist + 1, d.get(next, 1000000))
    maxd = 0
    for key, v in d.items():
        maxd = max(maxd, v)
    return maxd
    pass

deb = time.perf_counter()
part1(day)
print(time.perf_counter()-deb)
dayp2 = copy.deepcopy(day)
print(part1(day))


def getpoints(g, point, cur, seen):
    stack = [point]
    while stack:
        point = stack.pop()
        for i1, j1 in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= point[0] + i1 < len(g) and 0 <= point[1] + j1 < len(g[0]) and (
                    point[0] + i1, point[1] + j1) not in seen and g[point[0] + i1][point[1] + j1] == ",":
                seen.add((point[0] + i1, point[1] + j1))
                cur.append((point[0] + i1, point[1] + j1))
                stack.append((point[0] + i1, point[1] + j1))
    return cur


def part2(day):
    g = day.b2d()
    adj = {}
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == "S":
                o = (i, j)
            adj[(i, j)] = []
            if g[i][j] == "-":
                for i1, j1 in [(0, 1), (0, -1)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))
            elif g[i][j] == "|":
                for i1, j1 in [(1, 0), (-1, 0)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))
            elif g[i][j] == "J":
                for i1, j1 in [(-1, 0), (0, -1)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))

            elif g[i][j] == "F":
                for i1, j1 in [(1, 0), (0, 1)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))

            elif g[i][j] == "L":
                for i1, j1 in [(-1, 0), (0, 1)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))

            elif g[i][j] == 7:
                for i1, j1 in [(1, 0), (0, -1)]:

                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))

            elif g[i][j] == "S":
                for i1, j1 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + i1 < len(g) and 0 <= j + j1 < len(g[0]) and g[i + i1][j + j1] != ".":
                        adj[(i, j)].append((i + i1, j + j1))
    trueadj = {}
    for key, v in adj.items():
        trueadj[key] = []
        for i in range(len(v)):
            if key in adj[v[i]]:
                trueadj[key].append(v[i])
        if len(trueadj[key]) == 0:
            del trueadj[key]
    print("graph")

    stack = deque()
    stack.append((o, 0))
    d = {o: 0}
    seen = set(o)
    while stack:
        cur, dist = stack.popleft()
        for next in trueadj[cur]:

            if next not in seen:
                seen.add(next)

                stack.append((next, dist + 1))
                d[next] = min(dist + 1, d.get(next, 1000000))
    maxd = 0
    for key, v in d.items():
        maxd = max(maxd, v)
    g2 = new_table(len(g[0]) * 2, len(g) * 2, ".")
    for i in range(1, len(g2), 2):
        for j in range(len(g2[0])):
            g2[i][j] = "#"
    for i in range(len(g2)):
        for j in range(1, len(g2[0]), 2):
            g2[i][j] = "#"
    print("new grid")
    for key, v in d.items():
        for i1, j1 in [(-2, 0), (0, 2), (2, 0), (0, -2)]:
            if 0 <= key[0] * 2 + i1 < len(g2) and 0 <= key[1] * 2 + j1 < len(g2[0]):
                if type(g2[key[0] * 2 + i1][key[1] * 2 + j1]) == int:
                    if abs(g2[key[0] * 2 + i1][key[1] * 2 + j1] - v) != 1:
                        g2[key[0] * 2 + i1 // 2][key[1] * 2 + j1 // 2] = ","
                    else:
                        g2[key[0] * 2 + i1 // 2][key[1] * 2 + j1 // 2] = "+"
        g2[key[0] * 2][key[1] * 2] = v
    for key in d.keys():
        g2[key[0] * 2][key[1] * 2] = "0"
    print("g2 init")
    g2bis = copy.deepcopy(g2)
    for i in range(len(g2)):
        for j in range(len(g2[0])):
            if g2bis[i][j] == ",":
                for i1, j1 in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    if 0 <= i + i1 < len(g2) and 0 <= j + j1 < len(g2[0]) and g2bis[i + i1][j + j1] == "#":
                        g2[i + i1][j + j1] = ","
            elif g2bis[i][j] == ".":
                for i1, j1 in [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]:
                    if 0 <= i + i1 < len(g2) and 0 <= j + j1 < len(g2[0]):
                        g2[i + i1][j + j1] = ","
            elif type(g2[i][j]) == int:
                g2[i][j] = "0"
    for i in range(len(g2)):
        g2[i][-1] = ","
    seen = set()
    inside = set()
    # print_grid(g2)
    print("grid done")
    for i in range(len(g2)):
        for j in range(len(g2[0])):
            if (i, j) not in seen and g2[i][j] == ",":
                seen.add((i, j))
                cur = getpoints(g2, (i, j), [(i, j)], seen)
                touch = False
                for x, y in cur:
                    if x == 0 or y == 0 or x == len(g2) - 1 or y == len(g2[0]) - 1:
                        touch = True
                if touch:
                    for x, y in cur:
                        g2[x][y] = "O"
                else:
                    for x, y in cur:
                        if x % 2 == 0 and y % 2 == 0:
                            g2[x][y] = "I"
                            inside.add((x, y))
    g3 = new_table(len(g[0]), len(g), ".")
    for x, y in inside:
        g3[x // 2][y // 2] = "I"
    for key, v in d.items():
        g3[key[0]][key[1]] = 0

    # print_grid(g3)
    return len(inside)
    pass
deb = time.perf_counter()
part2(dayp2)
print(time.perf_counter()-deb)

print(part2(dayp2))
