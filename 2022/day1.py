file = open('day1_input.txt', 'r')
line = file.read().split("\n")
# Part 1
maxs = 0
s = 0
for x in line :
    if x == "":
        if s > min(maxs):
            maxs = s
        s=0
    else:
        s+= int(x)
print(maxs)
# Part 2
maxs = [0,0,0]
s = 0
for x in line :
    if x == "":
        if s > min(maxs):
            maxs[maxs.index(min(maxs))] = s # we update the smallest value of maxs
        s=0
    else:
        s+= int(x)
print(sum(maxs))