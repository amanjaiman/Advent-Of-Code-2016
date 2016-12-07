def least_common(arr):
    return min(arr, key = lambda _: arr.count(_))

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
password += least_common(fc)
password += least_common(sc)
password += least_common(tc)
password += least_common(foc)
password += least_common(fic)
password += least_common(sic)
password += least_common(sec)
password += least_common(ec)
print(password)
