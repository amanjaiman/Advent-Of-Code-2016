def test_cases(a, b, c):
    if a == "^" and b == "^" and c == ".":
        return "^"
    elif a == "." and b == "^" and c == "^":
        return "^"
    elif a == "^" and b == "." and c == ".":
        return "^"
    elif a == "." and b == "." and c == "^":
        return "^"
    return "."

floor = [".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."]
floor_len = len(floor[0])
count = 0
for i in range(399999):
    s = ""
    for j in range(floor_len):
        if j == 0:
            s += test_cases(".", floor[i][j], floor[i][j+1])
        elif j == floor_len-1:
            s += test_cases(floor[i][j-1], floor[i][j], ".")
        else:
            s += test_cases(floor[i][j-1], floor[i][j], floor[i][j+1])
    floor.append(s)
    #print(s)
    count += s.count(".")
print(count+floor[0].count("."))
