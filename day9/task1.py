import os

data = []
total = 1
max_area = 0

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        data.append([int(i) for i in line.strip().split(",")])

for i in range(len(data)):
    for j in range(i+1, len(data)):
        E = (1 + abs(data[j][0] - data[i][0])) * (1 + abs(data[j][1] - data[i][1]))
        if E > max_area:
            max_area = E

print(max_area)