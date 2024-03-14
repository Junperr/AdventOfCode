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


pyperclip.copy("""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""")
clip = pyperclip.paste()
day = parsing.Day(year=2023, day=13, sample=None)

def part1(day):

    pars = day.par()
    s = 0
    pars_r = {}
    for kk,par in enumerate(pars):
        reflect = {}
        # print(par)
        for i in range(len(par)):
            # print(par[i])
            if reflect == {}:
                for j in range(1,len(par[0])):
                    breaked = False
                    for j1 in range(min(len(par[0])-j,j)):
                        # print(i,j,j+j1,j-j1-1)
                        if par[i][j+j1] != par[i][j-j1-1]:
                            # print(j+j1,j-j1-1)
                            breaked = True
                            break
                    if not breaked:
                        reflect[j] = 1
                # print("reflect",reflect)
            else:
                for j in reflect.keys():
                    for j1 in range(min(len(par[0])-j,j)):
                        # print(i, j, j + j1, j - j1 - 1)
                        if par[i][j+j1] != par[i][j-j1-1]:
                            # print(j+j1+1,j-j1)
                            break
                    else:
                        reflect[j] += 1
                # print("reflect 2 : ",reflect,(len(par)))
        good = False
        for i,v in reflect.items():
            if v == (len(par)):
                good = True
                pars_r[kk] = i
                s += i
            # print(good)
        if not good:
            # do the same as above but with column symetry
            reflect = {}

            for j in range( len(par[0])):

                if reflect == {}:
                    for i in range(1,len(par)):
                        # print(line())
                        breaked = False
                        for i1 in range(min(len(par) - i, i)):
                            if par[i+i1][j] != par[i-i1-1][j]:
                                # print(i+i1, i-i1-1)
                                breaked = True
                                break
                        if not breaked:
                            reflect[i] = 1
                    # print("reflect", reflect)
                else:
                    for i in reflect.keys():
                        for i1 in range(min(len(par) - i, i)):
                            if par[i + i1][j] != par[i - i1-1][j]:
                                # print(i + i1 , i - i1-1)
                                # breaked = True
                                break
                        else:
                            reflect[i] += 1
                    # print("reflect 2", reflect,len(par[0]))

            good = False
            for i, v in reflect.items():
                if v == len(par[0]):
                    good = True
                    pars_r[kk] = 100*i
                    s += 100*i
            if not good:
                print("not good")
    return s,pars_r

    pass
dayp2 = copy.deepcopy(day)
a,b = part1(day)
print(part1(day))

def part2(day,b):
    pars = day.par()
    s = 0
    for kk,par in enumerate(pars):
        # print(kk)
        reflect = {}
        # print(*par)
        for i in range(len(par)):
            # print(par[i])
            if i<2 or reflect == {}:
                for j in range(1,len(par[0])):
                    breaked = False
                    for j1 in range(min(len(par[0])-j,j)):
                        # print(i,j,j+j1,j-j1-1)
                        if par[i][j+j1] != par[i][j-j1-1]:
                            # print(j+j1,j-j1-1)
                            breaked = True
                            break
                    if not breaked:
                        reflect[j] = reflect.get(j,0) + 1
                # print("reflect",reflect)
            else:
                for j in reflect.keys():
                    for j1 in range(min(len(par[0])-j,j)):
                        # print(i, j, j + j1, j - j1 - 1)
                        if par[i][j+j1] != par[i][j-j1-1]:
                            # print(j+j1+1,j-j1)
                            break
                    else:
                        reflect[j] += 1
                # print("reflect 2 : ",reflect,(len(par)))
        good = False
        for j, v in reflect.items():
            if v == (len(par) - 1):
                # diff = 0
                # for i in range(len(par)):
                #     for j1 in range(min(len(par[0]) - j, j)):
                #         if par[i][j + j1] != par[i][j - j1 - 1]:
                #             diff += 1
                # # print(j,min(len(par[0]) - j, j),v,diff)
                # if diff == 1:
                good = True
                s += i
                break

        if not good:
            # do the same as above but with column symetry
            reflect1 = reflect
            reflect = {}

            for j in range(len(par[0])):

                if j<2 or reflect == {}:
                    for i in range(1, len(par)):
                        # print(line())
                        breaked = False
                        for i1 in range(min(len(par) - i, i)):
                            if par[i + i1][j] != par[i - i1 - 1][j]:
                                # print(i + i1, i - i1 - 1)
                                breaked = True
                                break
                        if not breaked:
                            reflect[i] = reflect.get(i, 0) + 1
                    # print("reflect", reflect)
                else:
                    for i in reflect.keys():
                        for i1 in range(min(len(par) - i, i)):
                            if par[i + i1][j] != par[i - i1 - 1][j]:
                                # print(i + i1 , i - i1-1)
                                # breaked = True
                                break
                        else:
                            reflect[i] += 1
                    # print("reflect 2", reflect,len(par[0]))

            good = False
            for i, v in reflect.items():
                if v == len(par[0]) - 1:
                    # diff = 0
                    # for j in range(len(par[0])):
                    #     for i1 in range(min(len(par) - i, i)):
                    #         if par[i + i1][j] != par[i - i1 - 1][j]:
                    #             diff += 1
                    # # print(i,min(len(par) - i, i),v,diff)
                    # if diff == 1:
                    good = True
                    s += 100 * i
            if not good:
                # s += b.get(kk,0)
                print("not good")
                # pri nt(reflect,reflect1,len(par),len(par[0]),par)
        print(s,kk)
    return s
print(b)
print(part2(dayp2,b))