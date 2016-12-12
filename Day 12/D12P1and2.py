f = open("D12Text", "r")
letters = {"a": 0, "b": 0, "c": 0, "d":0} #For Part 2, change "c": 0 to "c": 1
arr = []
for line in f:
    arr += [line.strip().split()]

i = 0
while i < len(arr):
    change = False
    line = arr[i]
    if line[0] == "cpy":
        if line[1].isdigit():
            letters[line[2]] = int(line[1])
        else:
            letters[line[2]] = letters[line[1]]
    elif line[0] == "inc":
        letters[line[1]] += 1
    elif line[0] == "dec":
        letters[line[1]] -= 1
    elif line[0] == "jnz":
        if line[1].isdigit() and line[1] != 0:
            i += int(line[2])
            change = True
        else:
            if letters[line[1]] != 0:
                i += int(line[2])
                change = True
    if change == False:
        i += 1
    #input(line)
print(letters["a"])
