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


pyperclip.copy("""Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=16)
day = day.l()
flow = [0 for _ in range(len(day))]
near = [[] for _ in range(len(day))]
order = []
for x in day:
    order.append(x[6:8])
for i in range(len(day)):
    places = day[i].split(",")
    flow[i] = parse_nums(places[0])[0]
    for x in places:
        near[i].append(order.index(x[-2:]))

# print(near, order, flow, sep="\n")


def iterative_bfs(graph, start, opened):
    visited = []
    fifo = []
    fifo.append(start)
    dist = [-1 for _ in range(len(day))]
    dist[start] = 0
    while fifo != []:
        node = fifo.pop(0)
        if node not in visited:
            visited.append(node)
            for next in graph[node]:
                if next not in visited:
                    fifo.append(next)
                    dist[next] = dist[node] + 1
    for x in opened:
        dist[x] = -1
    return dist


# print(iterative_bfs(near,0,[]))

def part1(day):
    best = 0
    best_path = []

    def act(current, remain, opened, s, path):
        nonlocal best, best_path
        if remain < 0 or len(opened) == len(day):
            # if s > max(best):
            pass
        else:
            to_gain = [0 for _ in range(len(day))]
            paths = iterative_bfs(near, current, opened.copy())
            for i in range(len(day)):
                if i not in opened and paths[i] != -1:
                    to_gain[i] = flow[i] * max(0, remain - (paths[i] + 1))
            if remain >= 0 and s > best:
                best = s
                best_path = path
            for dest in range(len(day)):
                if to_gain[dest] > 0:
                    act(dest, remain - (paths[dest] + 1), opened + [dest], s + to_gain[dest], path + [dest])

    act(order.index("AA"), 30, [], 0, [0])
    return best, best_path

def part1v2(day):
    best = 0

    def act(current, remain, opened, s):
        nonlocal best
        if remain <= 0 or len(opened) == len(day):
            return 0
        else:
            to_gain = [0 for _ in range(len(day))]
            paths = iterative_bfs(near, current, opened.copy())
            for i in range(len(day)):
                if i not in opened and paths[i] != -1 and flow[i]*max(0, remain - (paths[i] + 1)) !=0 :
                    to_gain[i] = flow[i] * max(0, remain - (paths[i] + 1)) + act(i, remain - (paths[i] + 1), opened + [i], s + to_gain[i])
            # print(opened,to_gain)
            best = max(best,max(to_gain))
            return max(to_gain)
    return act(order.index("AA"), 30, [], 0)

dayp2 = copy.deepcopy(day)
# (2488, [0, 26, 50, 27, 16, 33, 51, 34])
# print(iterative_bfs(near, 0, [])[26], iterative_bfs(near, 26, [])[50], iterative_bfs(near, 50, [])[27], iterative_bfs(near, 27, [])[16],
#       iterative_bfs(near, 16, [])[33], iterative_bfs(near, 33, [])[51], iterative_bfs(near, 51, [])[34],sep="\n")
print(part1v2(day))


def part2(day):
    best = 0
    def act(current,current_e, remain,remain_e, opened, s):
        nonlocal best
        if remain < 0 and remain_e<0 or len(opened) == len(day):
            # if s > max(best):
            pass
        else:
            to_gain = [0 for _ in range(len(day))]
            to_gain_e = [0 for _ in range(len(day))]
            paths = iterative_bfs(near, current, opened.copy())
            paths_e = iterative_bfs(near, current_e, opened.copy())
            for i in range(len(day)):
                if i not in opened:
                    if paths[i] != -1:
                        to_gain[i] = flow[i] * max(0, remain - (paths[i] + 1))
                    if paths_e[i] != -1:
                        to_gain_e[i] = flow[i] * max(0, remain_e - (paths_e[i] + 1))
            # print(remain, remain_e)
            if s > best:
                best = s
            for dest in list(permutations(range(len(day)),2)):
                if to_gain[dest[0]] > 0 and to_gain_e[dest[1]] > 0:
                    act(dest[0] , dest[1], remain - (paths[dest[0]] + 1),remain_e - (paths_e[dest[1]] + 1), opened + [dest[0],dest[1]], s + to_gain[dest[0]] + to_gain_e[dest[1]])

    act(order.index("AA"),order.index("AA"), 26, 26, [], 0)
    return best


# print(part2(dayp2))
