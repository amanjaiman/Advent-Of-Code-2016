elves = 3014603
arr = []
for i in range(1, elves+1):
    arr.append(str(i))

while len(arr) > 1:
    new = []
    if len(arr) % 2 == 1:
        for i in range(2, len(arr), 2):
            new.append(arr[i])
    else:
        for i in range(0, len(arr), 2):
            new.append(arr[i])
    arr = new
print(arr)

'''i = 0
while len(arr) > 1:
    arr.pop((i+len(arr)//2) % len(arr))
    if i == len(arr)-1:
        i = 0
    else:
        i += 1
print(arr)'''

import collections
def solve_parttwo():
    ELF_COUNT = 3014603
    left = collections.deque()
    right = collections.deque()
    for i in range(1, ELF_COUNT+1):
        if i < (ELF_COUNT // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]
print(solve_parttwo())
