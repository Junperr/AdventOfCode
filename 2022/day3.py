import pyperclip
import parsing
# Ascii code : A 65,Z 90,a 97,z 122,0 48,9 57


# day  .input .l .par .b2d
s = 0

# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=1, sample=clip)
day = parsing.Day(year=2022, day=3)
lput = day.l()

def part1():
    s = 0
    for x in lput:
        for i in x[:len(x)]:
            if i in x[len(x) // 2:]:
                if ord(i) > 96:
                    s += ord(i) - 96
                else:
                    s += ord(i) - 38
                break
    return s

print(part1())

def part2():
    s = 0
    for i in range(0, len(lput) - 2, 3):
        for x in lput[i]:
            if x in lput[i+1]:
                if x in lput[i+2]:
                    if ord(x) > 96:
                        s += ord(x) - 96
                    else:
                        s += ord(x) - 38
                    break
    return s

print(part2())