def most_common(arr):
    return max(arr, key = lambda _: arr.count(_))

f = open("D6P1Text", "r")
fc = []
sc = []
tc = []
foc = []
fic = []
sic = []
sec = []
ec = []
password = ""
for line in f:
    fc.append(line[0])
    sc.append(line[1])
    tc.append(line[2])
    foc.append(line[3])
    fic.append(line[4])
    sic.append(line[5])
    sec.append(line[6])
    ec.append(line[7])
password += most_common(fc)
password += most_common(sc)
password += most_common(tc)
password += most_common(foc)
password += most_common(fic)
password += most_common(sic)
password += most_common(sec)
password += most_common(ec)
print(password)
