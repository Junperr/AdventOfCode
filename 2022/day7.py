import pyperclip
import timeit

import parsing
from usefull import NonBinTree, Leaf

# day  .input .l() .par() .b2d()

# pyperclip.copy("""$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k""")
# clip = pyperclip.paste()
# day = parsing.Day(year=2022, day=7, sample=clip)
day = parsing.Day(year=2022, day=7)
day = day.input.split("$")[1:]
for i in range(len(day)):
    day[i] = day[i].strip().split("\n")

def part1_2(day):
    tree = NonBinTree("/")
    path = ["/"]
    for x in day:
        if len(x) == 1 and x != "ls":
            dir = x[0].split()[1]
            if dir == "/":
                path = ["/"]
            elif dir == "..":
                path = path[:-1]
            else:
                path.append(dir)
        else:
            current = tree
            for y in path:
                for i in range(len(current.c)):
                    if current.c[i].x == y:
                        current = current.c[i]
                        break
            for cmd in x[1:]:
                c1, c2 = cmd.split()
                if c1 == "dir":
                    if c2 not in current.list_c_values():
                        current.add_node(c2)
                else:
                    if c2 not in current.list_c_values():
                        current.add_node([int(c1), c2])

    size = {}

    def taille(tree, path):
        nonlocal size
        if type(tree) == Leaf:
            return tree.x
        else:
            t = 0
            for child in tree.c:
                t += taille(child, path + tree.x + "/")
            size[path + tree.x] = t
            return t

    taille(tree, "")
    to_find = 30000000 - (70000000 - size["/"])
    mini = size["/"]
    s = 0
    for x in size.keys():
        if size[x] < 100000:
            s += size[x]
        if size[x] > to_find and size[x] < mini:
            mini = size[x]
#     print(f"""Partie 1 : {s}
# Partie 1 : {mini}""")
    return s,mini
nb = int(input())
s=0
for _ in range (nb):
    debtime = timeit.default_timer()
    part1_2(day)
    s+=timeit.default_timer() - debtime
print(s/nb)

# def part2(day):
#     tree = NonBinTree("/")
#     path = ["/"]
#     for x in day:
#         if len(x) == 1 and x != "ls":
#             dir = x[0].split()[1]
#             if dir == "/":
#                 path = ["/"]
#             elif dir == "..":
#                 path = path[:-1]
#             else:
#                 path.append(dir)
#         else:
#             current = tree
#             for y in path:
#                 for i in range(len(current.c)):
#                     if current.c[i].x == y:
#                         current = current.c[i]
#                         break
#             for cmd in x[1:]:
#                 c1, c2 = cmd.split()
#                 if c1 == "dir":
#                     if c2 not in current.list_c_values():
#                         current.add_node(c2)
#                 else:
#                     if c2 not in current.list_c_values():
#                         current.add_node([int(c1), c2])
#
#     size = {}
#     x = timeit.default_timer()
#     def taille(tree, path):
#         nonlocal size
#         if type(tree) == Leaf:
#             return tree.x
#         else:
#             t = 0
#             for child in tree.c:
#                 t += taille(child, path + tree.x + "/")
#             size[path + tree.x] = t
#             return t
#
#     taille(tree, "")
#     print(timeit.default_timer() - x)
#     to_find = 30000000 - (70000000 - size["/"])
#     mini = size["/"]
#     for x in size.keys():
#         if size[x] > to_find and size[x] < mini:
#             mini = size[x]
#     return mini


# print(part2(day))