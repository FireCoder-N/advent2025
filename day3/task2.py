import os

totalj = 0

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        indices = []
        for i in range(12):
            if indices == []:
                temp = 0
            else:
                temp = indices[-1]+1

            for i in range(temp+1, len(line)-11+len(indices)):
                if line[i] > line[temp]:
                    temp = i
            indices.append(temp)

        totalj += int("".join([line[i] for i in indices]))

print(totalj)