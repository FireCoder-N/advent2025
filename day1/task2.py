import os

head = 50
count = 0 

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        l = line.strip()
        if l.startswith("R"):
            head += int(l[1:])
        else:
            head -= int(l[1:])

        while head < 0:
            if head + int(l[1:]) != 0:
                count += 1
            head += 100

        while head > 100:
            count += 1
            head -= 100

        if head == 100:
            head = 0

        if head == 0:
            count += 1

print(count)