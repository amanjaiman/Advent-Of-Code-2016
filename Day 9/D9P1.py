f = open("D9Text", "r")

line = f.readline()
#print(len(line))
i = 0
new_string = ""

while i < len(line):
    exp = ""
    string = ""
    if line[i] == "(":
        i += 1
        while line[i] != ")":
            exp += line[i]
            i += 1
    exp = exp.split("x")
    #print(exp)
    #input()
    char_num = int(exp[0]) #The number of characters we need
    multiple = int(exp[1]) #How many times we multiply it
    i += 1
    while len(string) != char_num:
        string += line[i]
        i += 1
    for a in range(0, multiple):
        new_string += string
    print(len(new_string))
