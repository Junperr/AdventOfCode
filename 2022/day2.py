import timeit
file = open('day2_input.txt', 'r')
line = file.read().split("\n")

# Part 1
def part1():
    s = 0
    for x in line:
        if x != '':
            j1, j2 = x.split()
            j1 = ord(j1) - 65
            j2 = ord(j2) - 88
            if j2 == j1:
                s += 3 + j2 + 1
            elif j2 == (j1 + 1) % 3:
                s += j2 + 6 + 1
            else:
                s += j2 + 1
    return s

print(part1())

# x = timeit.default_timer()
# part1()
# print(timeit.default_timer() - x)

# Part 2
def part2():
    s = 0
    for x in line:
        if x != '':
            j1, v = x.split()
            j1 = ord(j1) - 65
            v = ord(v) - 88
            s += (j1 + (v - 1)) % 3 + 1 + v * 3
    return s

print(part2())

# x = timeit.default_timer()
# part2()
# print(timeit.default_timer() - x)
