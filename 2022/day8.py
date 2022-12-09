import pyperclip

import parsing
from usefull import parse_line, parse_nums, mul, all_unique, factors, primes

from usefull import new_table, transposed, rotated, firsts, lasts,n_col


pyperclip.copy("""30373
25512
65332
33549
35390""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=8)
day = day.b2d()

def part1(day):
    l,h = len(day[0]),len(day)
    maxd = [new_table(len(day[0]),len(day),0) for _ in range (4)]
    first = [new_table(len(day[0]), len(day), False) for _ in range(4)]
    s=0
    for i in range (1,h-1):
        for j in range (1,l-1):
            if day[i][j]>max(maxd[3][i][j-1],day[i][j-1]):
                first[3][i][j]= True
            maxd[3][i][j] = max (maxd[3][i][j-1],day[i][j],day[i][j-1])
    for i in range (1,h-1):
        for j in range (l-2,0,-1):
            if day[i][j]>max(maxd[1][i][j+1],day[i][j+1]):
                first[1][i][j]= True
            maxd[1][i][j] = max (maxd[1][i][j+1],day[i][j],day[i][j+1])
    for j in range(1, l-1):
        for i in range (1,h-1):
            if day[i][j]>max(maxd[2][i-1][j],day[i-1][j]):
                first[2][i][j]= True
            maxd[2][i][j] = max (maxd[2][i-1][j],day[i][j],day[i-1][j])
    for j in range(1, l-1):
        for i in range (h-2,0,-1):
            if day[i][j]>max(maxd[0][i+1][j],day[i+1][j]):
                first[0][i][j]= True
            maxd[0][i][j] = max (maxd[0][i+1][j],day[i][j],day[i+1][j])
    for i in range (1,h-1):
        for j in range (1,l-1):
            seen = False
            for z in range(4):
                if maxd[z][i][j] < day[i][j] or (maxd[z][i][j] == day[i][j] and first[z][i][j]):
                    seen = True
            if seen:
                s += 1
    return s + 2*h + 2*(l-2)

print(part1(day))

def part2(day):
    l, h = len(day[0]), len(day)
    max_scenic = 0
    for i in range(0, h ):
        for j in range(0, l ):
            tree_seen = [0,0,0,0]
            for j1 in range (j+1,l):
                if day[i][j]>day[i][j1]:
                    tree_seen[1] +=1
                else:
                    tree_seen[1] += 1
                    break
            for j1 in range(j-1,-1,-1):
                if day[i][j] > day[i][j1]:
                    tree_seen[3] += 1
                else:
                    tree_seen[3] += 1
                    break
            for i1 in range(i+1, h):
                if day[i][j] > day[i1][j]:
                    tree_seen[2] += 1
                else:
                    tree_seen[2] += 1
                    break
            for i1 in range(i-1,-1,-1):
                if day[i][j] > day[i1][j]:
                    tree_seen[0] += 1
                else:
                    tree_seen[0] += 1
                    break
            max_scenic = max(mul(tree_seen),max_scenic)
            # print(max_scenic,tree_seen,i,j)

    return max_scenic
import timeit
nb = int(input())
s=0
for _ in range (nb):
    debtime = timeit.default_timer()
    part1(day)
    s+=timeit.default_timer() - debtime
print(s/nb)
print(part2(day))