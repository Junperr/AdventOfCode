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


pyperclip.copy("""        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""")
# clip = pyperclip.paste()
# f = open("day22_input.txt","r")
# day = parsing.Day(year=2022, day=1, sample=f.read())
day = parsing.Day(year=2022, day=22)
day = day.b2d(val=" ")
print(DIRS_4)  # N,E,S,W


def part1(day):
    board = []
    for i in range(200):
        board.append(day[i][:150])
    # print_grid(board)
    instruc = []
    current = ""
    for i in range(len(day[-1])):
        if type(day[-1][i]) == int:
            current = current + str(day[-1][i])
        else:
            instruc.append(int(current))
            current = ""
            if day[-1][i] != " ":
                instruc.append(day[-1][i])
    pos = Point(50, 0)
    dir = DIRS_4[1]
    for x in instruc:
        if type(x) == int:
            for pas in range(x):
                next = pos + dir
                if next.y < 50:
                    next.x = (next.x - 50) % 100 + 50
                elif next.y < 100:
                    next.x = (next.x - 50) % 50 + 50
                elif next.y < 150:
                    next.x = next.x % 100
                else:
                    next.x = next.x % 50
                if next.x < 50:
                    next.y = (next.y - 100) % 100 + 100
                elif next.x < 100:
                    next.y = next.y % 150
                else:
                    next.y = next.y % 50
                # print(pos, next)
                if board[next.y][next.x] == "#":
                    break
                else:
                    pos = next
        else:
            if x == "R":
                dir = DIRS_4[(DIRS_4.index(dir) - 1) % 4]
            else:
                dir = DIRS_4[(DIRS_4.index(dir) + 1) % 4]
    return pos, dir


dayp2 = copy.deepcopy(day)
print(part1(day))


def part2(day):
    board = []
    for i in range(200):
        board.append(day[i][:150])
    # print_grid(board)
    instruc = []
    current = ""
    for i in range(len(day[-1])):
        if type(day[-1][i]) == int:
            current = current + str(day[-1][i])
        else:
            instruc.append(int(current))
            current = ""
            if day[-1][i] != " ":
                instruc.append(day[-1][i])
    faces = []
    faces.append([board[y][50:100] for y in range(50)])
    faces.append([board[y][50:100] for y in range(50, 100)])
    faces.append([board[y][50:100] for y in range(100, 150)])
    faces.append([board[y][:50] for y in range(100, 150)])
    faces.append([board[y][:50] for y in range(150, 200)])
    faces.append([board[y][100:150] for y in range(50)])

    def border_handler(pos, edge, new_edge, h=50, l=50):
        # DIRS_4 = [S,E,N,W]
        next = Point(0, 0)
        ind_ne = DIRS_4.index(new_edge)
        ind_e = DIRS_4.index(edge)
        if ind_e == 0:
            if ind_ne == ind_e:  # S
                next.x = 49 - pos.x
                next.y = 49
            elif ind_ne == (ind_e + 1) % 4:  # E
                next.x = 49
                next.y = pos.x
            elif ind_ne == (ind_e + 2) % 4:  # N
                next.x = pos.x
                next.y = 0
            else:  # W
                next.x = 0
                next.y = 49 - pos.x
            new_dir = DIRS_4[(ind_ne + 2) % 4]

        elif ind_e == 1:
            if ind_ne == ind_e:  # E
                next.x = 49
                next.y = 49 - pos.y
            elif ind_ne == (ind_e + 1) % 4:  # N
                next.x = 49 - pos.y
                next.y = 0
            elif ind_ne == (ind_e + 2) % 4:  # W
                next.x = 0
                next.y = pos.y
            else:  # S
                next.x = pos.y
                next.y = 49
            new_dir = DIRS_4[(ind_ne + 2) % 4]
        elif ind_e == 2:
            if ind_ne == ind_e:  # N
                next.x = 49 - pos.x
                next.y = 0
            elif ind_ne == (ind_e + 1) % 4:  # W
                next.x = 0
                next.y = pos.x
            elif ind_ne == (ind_e + 2) % 4:  # S
                next.x = pos.x
                next.y = 49
            else:  # E
                next.x = 49
                next.y = 49 - pos.x
            new_dir = DIRS_4[(ind_ne + 2) % 4]
        elif ind_e == 3:
            if ind_ne == ind_e:  # W
                next.x = 0
                next.y = 49 - pos.y
            elif ind_ne == (ind_e + 1) % 4:  # S
                next.x = 49 - pos.y
                next.y = 49
            elif ind_ne == (ind_e + 2) % 4:  # E
                next.x = 49
                next.y = pos.y
            else:  # N
                next.x = pos.y
                next.y = 0
            new_dir = DIRS_4[(ind_ne + 2) % 4]
        return next, new_dir

    # def border_handlerv2(pos, edge, new_edge, h=50, l=50):
    #     # DIRS_4 = [S,E,N,W]
    #     next = Point(0, 0)
    #     ind_ne = DIRS_4.index(new_edge)
    #     ind_e = DIRS_4.index(edge)
    #     if ind_e%2==0:
    #         util = pos.x
    #     else:
    #         util = pos.y
    #     if ind_e%2 == 0:
    #         if ind_ne == ind_e:  # S
    #             next.x = 49 - util
    #             next.y = 49 - (49*ind_e//2)
    #         elif ind_ne == (ind_e + 1) % 4:  # E
    #             next.x = 49 - (49*ind_e//2)
    #             next.y = util
    #         elif ind_ne == (ind_e + 2) % 4:  # N
    #             next.x = util
    #             next.y = 0 + (49*ind_e//2)
    #         else:  # W
    #             next.x = 0 + (49*ind_e//2)
    #             next.y = 49 - util
    #     else:
    #         if ind_ne == ind_e:  # E
    #             next.x = 49 - (49*ind_e//2)
    #             next.y = 49 - util
    #         elif ind_ne == (ind_e + 1) % 4:  # N
    #             next.x = 49 - util
    #             next.y = 0 + (49*ind_e//2)
    #         elif ind_ne == (ind_e + 2) % 4:  # W
    #             next.x = 0 + (49*ind_e//2)
    #             next.y = util
    #         else:  # S
    #             next.x = util
    #             next.y = 49 - (49*ind_e//2)
    #     new_dir = DIRS_4[(ind_ne + 2) % 4]
    #
    #     return next, new_dir

    def border_linker(face, dir):  # DIRS_4 = [S,E,N,W]
        print(face,dir)
        dir = DIRS_4.index(dir)
        print(dir)
        match face:
            case 1:
                match dir:
                    case 0:
                        return 4, DIRS_4[0]
                    case 1:
                        return 2, DIRS_4[3]
                    case 2:
                        return 6, DIRS_4[0]
                    case 3:
                        return 5, DIRS_4[0]
            case 2:
                match dir:
                    case 0:
                        return 4, DIRS_4[3]
                    case 1:
                        return 3, DIRS_4[3]
                    case 2:
                        return 6, DIRS_4[1]
                    case 3:
                        return 1, DIRS_4[1]
            case 3:
                match dir:
                    case 0:
                        return 4, DIRS_4[2]
                    case 1:
                        return 5, DIRS_4[2]
                    case 2:
                        return 6, DIRS_4[2]
                    case 3:
                        return 2, DIRS_4[1]
            case 4:
                match dir:
                    case 0:
                        return 1, DIRS_4[0]
                    case 1:
                        return 5, DIRS_4[3]
                    case 2:
                        return 3, DIRS_4[0]
                    case 3:
                        return 2, DIRS_4[0]
            case 5:
                match dir:
                    case 0:
                        return 1, DIRS_4[3]
                    case 1:
                        return 6, DIRS_4[3]
                    case 2:
                        return 3, DIRS_4[1]
                    case 3:
                        return 4, DIRS_4[1]
            case 6:
                match dir:
                    case 0:
                        return 1, DIRS_4[2]
                    case 1:
                        return 2, DIRS_4[2]
                    case 2:
                        return 3, DIRS_4[2]
                    case 3:
                        return 5, DIRS_4[1]

    pos = Point(0, 0)
    current_face = 0
    dir = DIRS_4[1]
    for x in instruc:
        if type(x) == int:
            for pas in range(x):
                pos_next = pos + dir
                if pos_next.x > 49 or pos_next.x < 0 or pos_next.y > 49 or pos_next.y < 0:
                    next_face, next_dir = border_linker(current_face+1, dir)
                    next_face -= 1
                    next, new_dir = border_handler(pos_next, dir, next_dir)
                else:
                    next_face = current_face
                    next = pos_next
                    new_dir = dir
                print(next_face,next.y,next.x)
                if faces[next_face][next.y][next.x] == "#":
                    break
                else:
                    current_face = next_face
                    pos = next
                    dir = new_dir
        else:
            if x == "R":
                dir = DIRS_4[(DIRS_4.index(dir) - 1) % 4]
            else:
                dir = DIRS_4[(DIRS_4.index(dir) + 1) % 4]
    return pos, dir,current_face


print(part2(dayp2))
