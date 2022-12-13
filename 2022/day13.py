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


pyperclip.copy("""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=13)
day = day.l()
sys.setrecursionlimit(10000)

# print(day)


def part1(day):
    count = 1
    s = 0
    for i in range(0, len(day), 3):
        # print(i)
        # print(day[i],day[i+1])
        left = eval(day[i])
        right = eval(day[i + 1])

        def are_good(left, right):
            nonlocal count, s
            for j in range(len(left)):
                if j >= len(right):
                    # print(left[j],"right no elem")
                    return False
                elif type(left[j]) == type(right[j]):
                    if type(left[j]) == int:
                        if left[j] < right[j]:
                            # print(left[j], right[j])
                            return True
                        elif left[j] > right[j]:
                            # print(left[j],right[j])
                            return False
                    else:
                        # print(left[j], right[j])
                        r = are_good(left[j], right[j])
                        if r == -1:
                            continue
                        else:
                            return r
                else:
                    if type(left[j]) == int:
                        r = are_good([left[j]], right[j])
                        if r == -1:
                            continue
                        else:
                            return r
                    else:
                        r = are_good(left[j], [right[j]])
                        if r == -1:
                            continue
                        else:
                            return r
            if len(right)==len(left):
                # print("oups")
                return -1
            # print("left no elem")
            return True
        if are_good(left, right):
            # print(count)
            s += count
            count += 1
        else:
            count += 1
    return s


dayp2 = copy.deepcopy(day)
print(part1(day))


def part2(day):
    def are_good(left, right):
        for j in range(len(left)):
            if j >= len(right):
                # print(left[j],"right no elem")
                return False
            elif type(left[j]) == type(right[j]):
                if type(left[j]) == int:
                    if left[j] < right[j]:
                        # print(left[j], right[j])
                        return True
                    elif left[j] > right[j]:
                        # print(left[j],right[j])
                        return False
                else:
                    # print(left[j], right[j])
                    r = are_good(left[j], right[j])
                    if r == -1:
                        continue
                    else:
                        return r
            else:
                if type(left[j]) == int:
                    r = are_good([left[j]], right[j])
                    if r == -1:
                        continue
                    else:
                        return r
                else:
                    r = are_good(left[j], [right[j]])
                    if r == -1:
                        continue
                    else:
                        return r
        if len(right) == len(left):
            # print("oups")
            return -1
        # print("left no elem")
        return True

    packet = []
    for i in range(len(day)):
        if day[i] != "":
            packet.append(eval(day[i]))
    packet.append([[2]])
    packet.append([[6]])
    for i in range (len(packet)):
        for j in range (i+1,len(packet)):
            # print(i, j,packet[i],packet[j])
            # print(are_good(packet[i],packet[j]))
            if not are_good(packet[i],packet[j]):

                packet[i],packet[j] = packet[j],packet[i]
                # print(i,j)
    return (packet.index([[2]])+1) * (packet.index([[6]])+1)


print(part2(dayp2))
