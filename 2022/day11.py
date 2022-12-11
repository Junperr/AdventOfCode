import parsing
from usefull import lcm

day = parsing.Day(year=2022, day=11)
day = day.l()
day1 = []
current = []
for i in range(0, len(day), 7):
    day1.append(day[i:i + 6])

monk = []
monk_item = []
monk_itemp2 = []
for x in day1:
    current = []
    monk_item.append(list(map(int, x[1][18:].split(","))))
    monk_itemp2.append(list(map(int, x[1][18:].split(","))))
    current.append(x[2][19:])
    current.append(int(x[3][21:]))
    current.append(int(x[4][29:]))
    current.append(int(x[5][30:]))
    monk.append(current)


def both_p(monk, monk_item, divider, round=20, op=0):
    count = [0 for _ in range(len(monk))]

    for _ in range(round):  # iterate on round
        for i in range(len(monk)):
            current = monk_item[i].copy()
            for ind in range(len(monk_item[i])):
                count[i] += 1
                old = current[ind]  # old is the name on the expresison inside eval
                new = divmod(eval(monk[i][0]), divider)[op]
                if new % monk[i][1] == 0:
                    monk_item[monk[i][2]].append(new)
                else:
                    monk_item[monk[i][3]].append(new)
                monk_item[i].pop(0)
    count.sort()
    return count[-1] * count[-2]


# Part1
print(both_p(monk, monk_item.copy(), 3))  # 78960

# Part2
maxn = lcm(monk[0][1], monk[1][1])
for z in range(2, len(monk)):
    maxn = lcm(maxn, monk[z][1])
# maxn is the lowest common multiple of all monk is divisible by test

print(both_p(monk, monk_itemp2, maxn, 10000, 1))  # 14561971968

# Execution time

# import timeit
# nb = int(input())
# s=0
# for _ in range (nb):
#     debtime = timeit.default_timer()
#     both_p(monk, monk_item.copy(), 3)
#     s+=timeit.default_timer() - debtime
# print(s/nb)

# nb = int(input())
# s=0
# for _ in range (nb):
#     debtime = timeit.default_timer()
#     both_p(monk, monk_itemp2, maxn,10000,1)
#     s+=timeit.default_timer() - debtime
# print(s/nb)
