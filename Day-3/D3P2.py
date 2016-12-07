def check(arr):
    a = int(arr[0])
    b = int(arr[1])
    c = int(arr[2])
    if a+b > c and a+c > b and b+c > a:
        return "1"
    return "0"

total = 0
possible_triangle1 = []
possible_triangle2 = []
possible_triangle3 = []
for line in open("Day3Problem1Text", "r"):
    triangles = line.split()
    possible_triangle1.append(triangles[0])
    possible_triangle2.append(triangles[1])
    possible_triangle3.append(triangles[2])
    if len(possible_triangle1) == 3:
        three_values = []
        three_values += check(possible_triangle1)
        three_values += check(possible_triangle2)
        three_values += check(possible_triangle3)
        total += three_values.count("1")
        possible_triangle3 = []
        possible_triangle2 = []
        possible_triangle1 = []
print(total)
#1577
