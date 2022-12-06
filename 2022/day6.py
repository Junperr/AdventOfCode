import parsing

day = parsing.Day(year=2022, day=6)
day = day.input


def part1():
    for i in range(len(day) - 3):
        if len(set(day[i:i + 4])) == 4:
            return i + 4


print(part1())


def part2():
    for i in range(len(day) - 13):
        if len(set(day[i:i + 14])) == 14:
            return i + 14


print(part2())
