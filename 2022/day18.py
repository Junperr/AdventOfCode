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


pyperclip.copy("""2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=18)
day = list(map(parse_nums,day.l()))

DIRS = [
    [0, 1, 0],  # north
    [1, 0, 0],  # east
    [0, -1, 0],  # south
    [-1, 0, 0],  # west
    [0, 0, 1],  # up
    [0, 0, -1]  # down
]
sys.setrecursionlimit(16000)
def neigh3d (g,p1):
    neigh = []
    for adj in DIRS:
        if 0 <= p1[0] + adj[0] < len(g) and 0 <= p1[1] + adj[1] < len(g[0]) and 0 <= p1[2] + adj[2] < len(g[0][0]):
            if g[p1[0]+adj[0]][p1[1]+adj[1]][p1[2]+adj[2]] == 0:
                neigh.append([p1[0]+adj[0],p1[1]+adj[1],p1[2]+adj[2]])
        else:
            neigh.append([p1[0] + adj[0], p1[1] + adj[1], p1[2] + adj[2]])

    return neigh

def part1(day,n=20):
    s=0
    g = [[copy.deepcopy([0]*n)for _ in range(n)]for _ in range (n)]
    # print(len(g),len(g[0]),len(g[0][0]))
    for p in day:
        g[p[0]][p[1]][p[2]] = 1
    for p in day:
        s+= len(neigh3d(g,p))
    return s
    pass


dayp2 = copy.deepcopy(day)
print(part1(day,25),25*25*25) #4504

def neigh3d_p2 (g,seen,p1):
    neigh = []
    for adj in DIRS:
        if 0 <= p1[0] + adj[0] < len(g) and 0 <= p1[1] + adj[1] < len(g[0]) and 0 <= p1[2] + adj[2] < len(g[0][0]):
            if (p1[0]+adj[0],p1[1]+adj[1],p1[2]+adj[2]) in seen:
                neigh.append([p1[0]+adj[0],p1[1]+adj[1],p1[2]+adj[2]])
        else:
            neigh.append([p1[0] + adj[0], p1[1] + adj[1], p1[2] + adj[2]])
    return neigh


def part2(day,n=25):
    s=0
    g = [[copy.deepcopy([0]*n)for _ in range(n)]for _ in range (n)]
    seen=set()
    for p in day:
        g[p[0]][p[1]][p[2]] = 1

    def parc(g, o):
        nonlocal seen
        # if len(seen)>30000:
        #     print("wtf")
        # if len(seen)%500==0:
        #     print(len(seen))
        seen.add(o)
        for adj in DIRS:
            if (o[0] + adj[0], o[1] + adj[1], o[2] + adj[2]) not in seen:
                if 0 <= o[0] + adj[0] < len(g) and 0 <= o[1] + adj[1] < len(g[0]) and 0 <= o[2] + adj[2] < len(g[0][0]) and g[o[0]+adj[0]][o[1]+adj[1]][o[2]+adj[2]] == 0:
                    parc(g,(o[0]+adj[0],o[1]+adj[1],o[2]+adj[2]))

    parc(g,(1,1,1))
    print(len(seen),(2,2,5)in seen)
    for p in day:
        s+= len(neigh3d_p2(g,seen,p))
    return s



print(part2(dayp2))
