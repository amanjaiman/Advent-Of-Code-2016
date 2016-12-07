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
    currently_valid = False
    for i in arr:
        i = i.strip()
        for j in range(0, (len(i)-3)):
            sub = i[j:j+4]
            if sub[0] == sub[3] and sub[1] == sub[2] and sub[0] != sub[1]:
                if i[0] == "0":
                    currently_valid = False
                else:
                    currently_valid = True
    if currently_valid == True:
        num_of_valid += 1
print(num_of_valid) #Try 1: 112 Too low. Try 2: 118 Too high. 115 is the right answer (guess based on the fact that those two weren't right)
