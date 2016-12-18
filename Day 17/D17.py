import hashlib

def check(a, b):
    return a == 4 and b == 4

my_input = "ulqzkmiv"#"veumntbg"

queue = [["", 1, 1]]
full_paths = []
while len(queue) > 0:
    current = queue[0]
    path = current[0]
    h = (hashlib.md5((my_input+path).encode('utf-8')).hexdigest())[:4]
    if h[0] in "bcdef" and current[2] != 1:
        if check(current[1], current[2]):
            full_paths.append(path)
        else:
            queue.append([path+"U", current[1], current[2]-1])
    if h[1] in "bcdef" and current[2] != 4:
        if check(current[1], current[2]):
            full_paths.append(path)
        else:
            queue.append([path+"D", current[1], current[2]+1])
    if h[2] in "bcdef" and current[1] != 1:
        if check(current[1], current[2]):
            full_paths.append(path)
        else:
            queue.append([path+"L", current[1]-1, current[2]])
    if h[3] in "bcdef" and current[1] != 4:
        if check(current[1], current[2]):
            full_paths.append(path)
        else:
            queue.append([path+"R", current[1]+1, current[2]])
    queue.pop(0)
shortest = full_paths[0]
print(full_paths)
for i in full_paths:
    if len(i) < len(shortest):
        shortest = i

print(shortest)
