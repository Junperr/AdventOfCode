from string import ascii_uppercase, ascii_lowercase

import parsing
from usefull import parse_line, parse_nums, chunks, mul, all_unique, factors, primes


def part1():
    day = parsing.Day(year=2022, day=5)
    day = day.par()
    # print(day[0])
    # for x in day[0]:
    # print (len(x))
    rows = parse_nums(day[0][-1])
    t = rows[-1]
    # print(t)
    tab = []
    for x in day[0][:-1]:

        current = ["" for i in range(t)]
        # dec = n-len(lines[i])
        dec = 0
        j = 0
        work = 0
        for j in range(t):
            # while j < len(x) and work<t:
            #     if x[j] in ascii_uppercase or x[j]==" ":
            #         current[work]= x[j]
            #         work+=1
            #     j += 1
            for x1 in x[4 * j:4 * j + 4]:
                if x1 in ascii_uppercase:
                    current[j] = x1

        tab.append(current)
    # print(tab)
    tab2 = []
    for i in range(t):
        current = []
        for j in range(t - 2, -1, -1):
            if tab[j][i] != "":
                current.append(tab[j][i])
        tab2.append(current)
    # print(tab2)
    # print(day[1])
    count = 0
    inst = []
    for r in range(1, len(day)):
        # if len(day[r])>1:
        for j in range(len(day[r])):
            inst.append(day[r][j])
        # else:
        #     inst.append(day[r])
    # print(len(inst))
    # print(inst)
    inst = inst[:-1]
    for line in inst:
        # print(count)
        count += 1
        # print(line)
        ls = line.split()
        tup = [int(ls[1]), int(ls[3]), int(ls[5])]
        # print(tup)
        # print(list(map(len, tab2)))
        tamp = []
        for z in range(tup[0]):
            tab2[tup[2] - 1].append(tab2[tup[1] - 1].pop())

    res = ""
    # print(tab2)
    for x in (tab2):
        if x != []:
            res += x[-1]
        else:
            res += " "
    # print(res)
    # print(len(day),day)
    print(res)


part1()


def part2():
    day = parsing.Day(year=2022, day=5)
    day = day.par()

    rows = parse_nums(day[0][-1])
    t = rows[-1]
    tab = []
    for x in day[0][:-1]:
        current = ["" for i in range(t)]
        dec = 0
        j = 0
        work = 0
        for j in range(t):
            for x1 in x[4 * j:4 * j + 4]:
                if x1 in ascii_uppercase:
                    current[j] = x1

        tab.append(current)
    tab2 = []
    for i in range(t):
        current = []
        for j in range(t - 2, -1, -1):
            if tab[j][i] != "":
                current.append(tab[j][i])
        tab2.append(current)
    count = 0
    inst = []
    for r in range(1, len(day)):
        for j in range(len(day[r])):
            inst.append(day[r][j])
    inst = inst[:-1]
    for line in inst:
        count += 1
        ls = line.split()
        tup = [int(ls[1]), int(ls[3]), int(ls[5])]
        tamp = []
        for z in range(tup[0]):
            tamp.append(tab2[tup[1] - 1].pop())
        tab2[tup[2] - 1] = tab2[tup[2] - 1] + tamp[::-1]

    res = ""
    for x in (tab2):
        if x != []:
            res += x[-1]
        else:
            res += " "
    print(res)


part2()
