f = open("Day4Problem1Text", "r")

'''def five_most_common(a): #NOTDONE
    most_common = []
    mc_values = []
    #put whole thing under in for i in range(0, 5):
    used_chars = []
    num = 0
    curr_char = ""
    for i in a:
        if !(i in used_chars):
            c = a.count(i)
            if c > num:
                num = c
                curr_char = i
    most_common.append(curr_char)
    mc_values.append(str(num))'''

def caesar_cipher(a):
    a = list(a)
    for i in range(0, len(a)):
        if ord(a[i]) == 122:
            a[i] == 'a'
        else:
            a[i] = chr(ord(a[i])+1)
    return ''.join(a)

#First Part:
sectorID_sum = 0
for line in f:
    #Getting the values that we need:
    arr = line.split("-")
    string = ""
    for i in range(0, len(arr)-1):
        string += arr[i]
    temp_arr = arr[len(arr)-1].split("[")
    sectorID = temp_arr[0]
    checksum = temp_arr[1]
    checksum = checksum[0:5]
    print(caesar_cipher(string))
    if "north" in caesar_cipher(string):
        print(sectorID)
    #Most common five letters:
    #most_common_letters = five_most_common(string)
#409417
