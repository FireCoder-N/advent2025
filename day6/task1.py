import os

total = 0
data = []

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        data.append([x for x in line.strip().split() if x != ""])

for i in range(len(data[0])):
    total += eval(f"{data[-1][i]}".join([data[x][i] for x in range(len(data)-1)]))

print(total)