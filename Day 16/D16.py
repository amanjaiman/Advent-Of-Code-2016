def generate_data(a, n):
    while len(a) < n:
        b = a[::-1]
        b = b.translate(str.maketrans({"0":"1","1":"0"}))
        #Replace 0's and 1's
        a = a + "0" + b
    return a[:n]

def generate_checksum(a):
    checksum = a
    count = 0
    while len(checksum) % 2 == 0 or count == 0:
        checksum = ""
        for i in range(0, len(a), 2):
            pair = a[i]+a[i+1]
            if pair[0] == pair[1]:
                checksum += "1"
            else:
                checksum += "0"
        a = checksum
        count += 1
    return a

print(generate_checksum(generate_data("10111011111001111", 35651584)))
#Part 1: String of binary, 272
#Part 2: Same string, 35651584
