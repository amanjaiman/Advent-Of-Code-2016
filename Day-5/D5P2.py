import hashlib
password = list("--------")
starting = 0
doorID = "uqwqemis"
while password.count("-") > 0:
    string = doorID + str(starting)
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    md = m.hexdigest()
    if md.startswith("00000"):
        if md[5].isdigit() == True and int(md[5]) < 8 and password[int(md[5])] == "-":
            password[int(md[5])] = md[6]
    starting += 1
print(''.join(password))
