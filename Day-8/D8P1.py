from collections import deque
f = open("D8Text", "r")

#Initialize the grid:
arr = []
for i in range(0, 6):
    cur_arr = []
    for j in range(0, 50):
        cur_arr.append(" ")
    arr.append(cur_arr)
#Run through the data + see what to do:
for line in f:
    if line.startswith("rect"):
        l = line.split()
        width = int(l[1].split("x")[0])
        height = int(l[1].split("x")[1])
        for i in range(0, height):
            for j in range(0, width):
                arr[i][j] = "."
    else:
        l = line.split()
        if l[1] == "row": #Row stuff
            loc = int(l[2].split("=")[1])
            amount = int(l[4])
            items = deque(arr[loc])
            items.rotate(amount)
            for i in range(0, 50):
                arr[loc][i] = items[i]
        else: #Column stuff
            loc = int(l[2].split("=")[1])
            amount = int(l[4])
            items = []
            for i in range(0, 6):
                items.append(arr[i][loc])
            items = deque(items)
            items.rotate(amount)
            for i in range(0, 6):
                arr[i][loc] = items[i]
count_of_dots = 0
for i in arr:
    for j in i:
        if j == ".":
            count_of_dots += 1
for i in arr:
    print(i)
print(count_of_dots)
