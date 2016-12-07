import hashlib
password = ""
starting = 0
doorID = "uqwqemis"
while len(password) < 8:
    string = doorID + str(starting)
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    md = m.hexdigest()
    if md.startswith("00000"):
        password += md[5]
    starting += 1
print(password)
