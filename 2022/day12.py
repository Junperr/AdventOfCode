import sys
import pyperclip
import copy

import parsing
from usefull import new_table
from usefull import DIRS_4



sys.setrecursionlimit(10**6)
pyperclip.copy("""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=12)
day = day.b2d()
dayp2 = copy.deepcopy(day)

def both_part(day,part=2):
    to_go = new_table(len(day[0]), len(day), 10 ** 10)

    def path_rec(i, j, long):
        nonlocal to_go
        for dir in DIRS_4:

            if -1 < i + dir.x < len(day) and -1 < j + dir.y < len(day[0]):
                if ord(day[i + dir.x][j + dir.y]) >= (ord(day[i][j]) - 1) and to_go[i + dir.x][j + dir.y] > long:
                    to_go[i + dir.x][j + dir.y] = long
                    path_rec(i + dir.x, j + dir.y, long + 1)

    a_elev = []
    for i in range(len(day)):
        for j in range(len(day[0])):
            if day[i][j] == "S":
                day[i][j] = "a"
                s = [i, j]
            if day[i][j] == "E":
                day[i][j] = "z"
                e = [i, j]
            if day[i][j] == "a":
                a_elev.append([i,j])

    to_go[e[0]][e[1]] = 0
    path_rec(e[0], e[1], 1)
    if part == 1 :
        return to_go[s[0]][s[1]]
    else:
        return min(to_go[x[0]][x[1]] for x in a_elev)
        min_path = 10**5
        for x in a_elev:
            if to_go[x[0]][x[1]]<min_path:
                min_path=to_go[x[0]][x[1]]
        return min_path

print(both_part(day,1))

print(both_part(dayp2))
