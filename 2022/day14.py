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


pyperclip.copy("""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=14)

def int_tuple(t):
    l = t.split(",")
    return Point(int(l[1]),int(l[0])-400)

day = day.l()
day = list(map(lambda obj: obj.split("->"), day))
day = [list(map(int_tuple, x)) for x in day]


cave = new_table(200,200,0)
lowx = 0
for line in day:
    for i in range (len(line)-1):
        deb = line[i]
        end = line[i+1]
        if deb.x == end.x:
            for y in range (0,(end-deb).y+int((end-deb).y/abs((end-deb).y)),int((end-deb).y/abs((end-deb).y))):

                rock = deb + Point(0,y)
                cave[rock.x][rock.y] = 2
                lowx = max(lowx, rock.x)


        else:
            for x in range (0,(end-deb).x+int((end-deb).x/abs((end-deb).x)),int((end-deb).x/abs((end-deb).x))):

                rock = deb + Point(x,0)
                cave[rock.x][rock.y] = 2
                lowx = max(lowx, rock.x)
# for y in range (len(cave[0])):
#     cave[lowx+2][y]=2

# cave = new_table(1000,200,0)
# lowx = 0
# for line in day:
#     for i in range (len(line)-1):
#         deb = line[i]
#         end = line[i+1]
#         if deb.x == end.x:
#             for y in range (0,(end-deb).y+int((end-deb).y/abs((end-deb).y)),int((end-deb).y/abs((end-deb).y))):
#
#                 rock = deb + Point(0,y)
#                 cave[rock.x][rock.y] = 2
#                 lowx = max(lowx, rock.x)
#
#
#         else:
#             for x in range (0,(end-deb).x+int((end-deb).x/abs((end-deb).x)),int((end-deb).x/abs((end-deb).x))):
#
#                 rock = deb + Point(x,0)
#                 cave[rock.x][rock.y] = 2
#                 lowx = max(lowx, rock.x)
# for y in range (len(cave[0])):
#     cave[lowx+2][y]=2
# print_grid(cave)
print(lowx)
def part1(day):
    count=0
    while True:
        sand = Point(0,100)
        while cave[sand.x][sand.y]==0 and sand.x<lowx:
            done = False
            for move in [Point(1,0),Point(1,-1),Point(1,1)]:
                next = sand + move
                # print(next)
                if cave[next.x][next.y] == 0:
                    sand = next
                    done = True
                    break
            if not done:
                cave[sand.x][sand.y] = 1
                count+=1
        if sand.x>=lowx:
            return count

    return count
    pass


dayp2 = copy.deepcopy(day)
print(part1(day))
print_grid(cave)

def part2(day):
    count = 0
    while True:
        print(count)
        sand = Point(0, 500)
        while cave[sand.x][sand.y] == 0 and sand.x < lowx+2:
            done = False
            for move in [Point(1, 0), Point(1, -1), Point(1, 1)]:
                next = sand + move
                # print(next)
                if cave[next.x][next.y] == 0:
                    sand = next
                    done = True
                    break
            if not done:
                cave[sand.x][sand.y] = 1
                count += 1
        if sand.x >= lowx+2:
            return count

    return count


# print(part2(dayp2))
