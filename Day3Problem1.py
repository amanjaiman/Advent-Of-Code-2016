total = 0
for line in open("Day3Problem1Text", "r"):
    possible_triangle = line.split()
    a = int(possible_triangle[0])
    b = int(possible_triangle[1])
    c = int(possible_triangle[2])
    if a+b > c and a+c > b and b+c > a:
        total += 1
print(total)
#862

#To combine lines 2-7:
#for l in open("Day3Problem1Text", "r"):
#    if int(l.split()[0])+int(l.split()[1]) > int(l.split()[2]) and int(l.split()[0])+int(l.split()[2]) > int(l.split()[1]) and int(l.split()[1])+int(l.split()[2]) > int(l.split()[0]):
