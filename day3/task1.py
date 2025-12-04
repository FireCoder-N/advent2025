import os

totalj = 0

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        maxj1_index = 0
        for i in range(1, len(line)-1):
            if line[i] > line[maxj1_index]:
                maxj1_index = i

        maxj2_index = maxj1_index + 1
        for i in range(maxj1_index+2, len(line)):
            if line[i] > line[maxj2_index]:
                maxj2_index = i
        
        t= int(f"{line[maxj1_index]}{line[maxj2_index]}")
        totalj += t

print(totalj)