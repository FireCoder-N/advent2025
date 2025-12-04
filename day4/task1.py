import os

data = []
total = 0

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        data.append(["."] + [i for i in line.strip()]+ ["."])

    data.insert(0, ["." for i in range(len(data[0]))])
    data.append(["." for i in range(len(data[0]))])

    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            if data[i][j] == "@":

                if [
                    data[i-1][j-1], data[i-1][j], data[i-1][j+1],
                    data[i][j-1], data[i][j+1],
                    data[i+1][j-1], data[i+1][j], data[i+1][j+1]
                ].count("@") < 4:
                    total +=1

print(total)

