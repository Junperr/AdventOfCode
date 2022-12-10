import parsing
from usefull import Point, DIRS_4

day = parsing.Day(year=2022, day=9)
day = day.l()


def part1(day):
    pos = set()
    h = Point(0, 0)
    t = Point(0, 0)
    pos.add(t)
    dirs = ["U", "R", "D", "L"]
    for x in day:
        x = x.split()
        x[1] = int(x[1])
        for i in range(x[1]):
            prev = h
            h += DIRS_4[dirs.index(x[0])]
            if h.dist_manhattan(t) > 1 and t not in h.neighbours_8():
                t = prev
                pos.add(t)
    return len(pos)


print(part1(day))  # 6044


def part2(day):
    pos = set()
    h = Point(0, 0)
    t = [Point(0, 0) for _ in range(9)]
    pos.add(t[8])
    dirs = ["U", "R", "D", "L"]
    for x in day:
        x = x.split()
        x[1] = int(x[1])
        for i in range(x[1]):
            prev = h
            h += DIRS_4[dirs.index(x[0])]
            if h.dist_manhattan(t[0]) > 1 and t[0] not in h.neighbours_8():
                move = prev - t[0]
                prevt = t[0]
                t[0] = prev

            for ind in range(1, 9):
                if t[ind - 1].dist_manhattan(t[ind]) > 1 and t[ind] not in t[ind - 1].neighbours_8():
                    if t[ind - 1].dist_manhattan(t[ind]) == 2 and (
                            t[ind - 1].dist_manhattanx(t[ind]) == 2 or t[ind - 1].dist_manhattany(t[ind]) == 2):
                        prevt = t[ind]
                        move = (t[ind - 1] + t[ind]).div(2).int() - t[ind]
                        t[ind] = (t[ind - 1] + t[ind]).div(2).int()
                    else:
                        test = t[ind] + move
                        if min(t[ind - 1].dist_manhattan(test), t[ind - 1].dist_manhattan(prevt)) == t[
                            ind - 1].dist_manhattan(prevt):
                            move = prevt - t[ind]
                            t[ind], prevt = prevt, t[ind]

                        else:
                            prevt = t[ind]
                            t[ind] += move
            pos.add(t[8])
    return len(pos)


print(part2(day))  # 2384
