import timeit
file = open('day1_input.txt', 'r')
line = file.read().split("\n")

# Part 1

def part1():
    maxs = 0
    s = 0
    for x in line :
        if x == "":
            if s > maxs:
                maxs = s
            s=0
        else:
            s+= int(x)
    return maxs

print(part1())

# x = timeit.default_timer()
# part1()
# print(timeit.default_timer() - x)

# Part 2
def part2():
    maxs = [0,0,0]
    s = 0
    for x in line :
        if x == "":
            if s > min(maxs):
                maxs[maxs.index(min(maxs))] = s # we update the smallest value of maxs
            s=0
        else:
            s+= int(x)
    return sum(maxs)

print(part2())


# x = timeit.default_timer()
# part2()
# print(timeit.default_timer() - x)