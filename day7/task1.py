import os

data = []
total = 0

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        data.append(list(line.strip()))

for i in range(1,len(data)):
    for j in range(1, len(data[0])-1):
        if data[i-1][j] == "S":
            data[i][j] = "|"

        if data[i-1][j] == "|":
            if data[i][j] == "^":
                data[i][j-1] = "|"
                data[i][j+1] = "|"
                total += 1
            elif data[i][j] == ".":
                data[i][j] = "|"

print(total)    