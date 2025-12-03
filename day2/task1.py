import os

count = 0

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        ranges = line.strip().split(",")
        for r in ranges:
            bounds = r.split("-")
            for number in range(int(bounds[0]), int(bounds[1])+1):
                n = str(number)
                if len(n) % 2 == 0 and n[:len(n)//2] == n[len(n)//2:]:
                    count += number

print(count)