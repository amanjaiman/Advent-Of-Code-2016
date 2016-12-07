def most_common(arr):
    return max(arr, key = lambda _: arr.count(_))

f = open("D6P1Text", "r")
arr = [[], [], [], [], [], [], [], []]
password = ""
for line in f:
    for i in range(0, 8):
        arr[i].append(line[i])
for i in range(0, 8):
    password += most_common(arr[i])
print(password)
