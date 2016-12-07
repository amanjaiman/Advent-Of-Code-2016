#0 = North, 1 = East, 2 = South, 3 = West
direction = 0
horizontalValue = 0
verticalValue = 0

the_input = "L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5"
puzzle_input = the_input.split(", ")

for i in puzzle_input:
    if i[0] == "R":
        direction -= 1
    else:
        direction += 1
    if direction == 4:
        direction = 0
    if direction == -1:
        direction = 3

    if direction == 0:
        verticalValue += int(i[1:])
    if direction == 2:
        verticalValue -= int(i[1:])
    if direction == 1:
        horizontalValue += int(i[1:])
    if direction == 3:
        horizontalValue -= int(i[1:])
print(abs(horizontalValue)+abs(verticalValue))

input()
