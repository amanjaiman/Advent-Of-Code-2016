f = open("D7P1Text", "r")

num_of_valid = 0
for line in f:
    arr = line.split("[")
    while "]" in arr[len(arr)-1]:
        for i in range(0, len(arr)):
            if "]" in arr[i]:
                temp_arr = arr[i].split("]")
                arr[i] = "0"+temp_arr[0]
                arr.insert(i+1, temp_arr[1])
    #print(arr)
    valid = False
    for j in arr:
        if j.startswith("0") == False:
            for i in range(0, len(j)-2):
                sub = j[i:i+3]
                if sub[0] == sub[2] and sub[0] != sub[1]:
                    new = sub[1] + sub[0] + sub[1]
                    for k in arr:
                        if k.startswith("0"):
                            if new in k:
                                valid = True
    if valid == True:
        num_of_valid += 1
print(num_of_valid)
#231 is the correct answer
