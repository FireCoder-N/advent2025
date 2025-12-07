import os

# This algorithm should be really fast, but it is impractical due to large amount of data :(

fresh_ids = set()
toggleOp = True # True for fresh ranges, false for ingredient ID
total = 0 

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        if line == "\n":
            toggleOp = False

        elif toggleOp:
            r = [int(x) for x in line.strip().split("-")]
            for i in range(r[0], r[1]+1):
                fresh_ids.add(i)

        else:
            if int(line.strip()) in fresh_ids:
                total +=1

print(total)

