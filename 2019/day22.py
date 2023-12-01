import copy
import parsing

day = parsing.Day(year=2019, day=22).l()


def part1(day, size):
    pos = 2019
    for i in range(len(day)):
        print(day[i])
        current = day[i].split()
        if current[1] == "into":
            pos = (size - pos - 1) % size
        elif current[0] == "cut":
            print(pos,current[1])
            pos = (pos - int(current[1])) % size
        else:
            print(pos,pos//int(current[3]),pos%int(current[3]))
            pos = (pos * int(current[3])) % size
        print(pos)
    return pos


dayp2 = copy.deepcopy(day)
print(part1(day, 10007))


def part2(day, size):
    pos = 2020
    for _ in range (101741582076661):
        for i in range(len(day)-1,-1,-1):
            current = day[i].split()
            if current[1] == "into":
                pos = (size - pos - 1) % size
            elif current[0] == "cut":
                print(pos, current[1])
                pos = (pos + int(current[1])) % size
            else:
                last = int(size/current[3])

    pass


print(part2(dayp2, 119315717514047))


def show(size, increment):
    l = [0 for _ in range(size)]
    for i in range(size):
        l[(i * increment) % size] = i
    return [((i // increment + 1) + increment * (size - (i % increment)) - 1) % size for i in range(size)], l, [
        ((i // increment + 1) + increment * (increment - (i % increment))) % size for i in range(size)], [
        (increment * i) % size for i in range(size)]


print(show(10, 1))
print(show(10, 3))
print(show(10, 7))
print(show(10, 11))
print(show(10, 13))
print(show(10, 17))
