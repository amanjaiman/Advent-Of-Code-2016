f = open("D20Text", "r")

all_nums = set(range(0, 4294967296))

not_valid = set()
for line in f:
    l = line.split("-")
    not_valid.update(range(int(l[0]), int(l[1])+1))

print(min(list(all_nums.difference(not_valid))))
