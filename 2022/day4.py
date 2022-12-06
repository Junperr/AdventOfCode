import parsing


# day  .input .l .par .b2d


def part1():
    day = parsing.Day(year=2022, day=4)
    s = 0
    day = day.l()
    for x in day:
        e1, e2 = x.split(",")
        e1 = list(map(int, e1.split("-")))
        e2 = list(map(int, e2.split("-")))
        if (e1[0] <= e2[0] and e1[1] >= e2[1]) or (e1[0] >= e2[0] and e1[1] <= e2[1]):
            s += 1
    return s


print(part1())


def part2():
    day = parsing.Day(year=2022, day=4)
    s = 0
    day = day.l()
    for x in day:
        e1, e2 = x.split(",")
        e1 = list(map(int, e1.split("-")))
        e2 = list(map(int, e2.split("-")))
        if e1[0] <= e2[0] <= e1[1] or e1[1] >= e2[1] >= e1[0] or e2[0] <= e1[0] <= e2[1] or e2[1] >= e1[1] >= e2[0]:
            s += 1
    return s


print(part2())

# def bad_part2():
#     day = parsing.Day(year=2022, day=4)
#     s = 0
#     day = day.l()
#     for x in day:
#         e1, e2 = x.split(",")
#         e1 = list(map(int, e1.split("-")))
#         e2 = list(map(int, e2.split("-")))
#         e1 = list(range(e1[0], e1[1] + 1))
#         e2 = list(range(e2[0], e2[1] + 1))
#         done = False
#         for x1 in e1:
#             if not done:
#                 if x1 in e2:
#                     s += 1
#                     done = True
#                     break
#
#         for x2 in e2:
#             if not done:
#                 if x2 in e1:
#                     s += 1
#                     done = True
#                     break
#
#     return s
#     pass
