import parsing

day = parsing.Day(year=2022, day=10)
day = day.l()

def int_sc(l):
    if len(l) == 2:
        return [l[0], int(l[1])]
    return l

day = list(map(lambda obj: int_sc(obj.split()), day))


def part1(day):
    X = 1
    count = 1
    s = 0
    for x in day:
        if x[0] == "addx":
            if (count - 19) % 40 == 0:
                s += (count + 1) * X
            count += 1
            X = X + x[1]
        if (count - 19) % 40 == 0:
            s += (count + 1) * X
        count += 1
    return s

print(part1(day))  # 12540


def part2(day):
    X = 1
    count = 0
    tl = ""
    for x in day:
        if x[0] == "noop":
            if X - 1 <= count % 40 < X + 2:
                tl = tl + "#"
            else:
                tl = tl + "."
            count += 1
        else:
            if X - 1 <= count % 40 < X + 2:
                tl = tl + "#"
            else:
                tl = tl + "."
            count += 1
            if count % 40 == 0:
                print(tl)
                tl = ""
            if X - 1 <= count % 40 < X + 2:
                tl = tl + "#"
            else:
                tl = tl + "."
            count += 1
            X = X + x[1]
        if count % 40 == 0:
            print(tl)
            tl = ""
    pass


part2(day)  # FECZELHE

# import timeit
# nb = int(input())
# s=0
# for _ in range (nb):
#     debtime = timeit.default_timer()
#     part1(day)
#     s+=timeit.default_timer() - debtime
# print(s/nb)