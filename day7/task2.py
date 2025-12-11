import os
import copy

data = []
total_splits = 0
split_nodes = {}

def probe_node(ni, nj):
    if split_nodes[(ni, nj)] == 0:
        timelines = 0
        # LEFT CHILD
        if nj > 0:
            timelines += propagate_direction(ni, nj, -1)
        # RIGHT CHILD
        if nj < len(data[0])-1:
            timelines += propagate_direction(ni, nj, 1)

        split_nodes[(ni, nj)] += timelines

    return split_nodes[(ni, nj)]

def propagate_direction(ni, nj, direction):
    # Direction: -1 for left, 1 for right

    data_t = copy.deepcopy(data)
    timelines = 0

    data_t[ni][nj + direction] = "|"

    for i in range(ni + 1, len(data_t)):
        for j in range(0, len(data_t[0])):

            if data_t[i - 1][j] == "|":

                # Split cell → recurse
                if data_t[i][j] == "^":
                    timelines += probe_node(i, j)

                # Empty cell → propagate
                elif data_t[i][j] == ".":
                    data_t[i][j] = "|"

                    if i == len(data_t) - 1:
                        # for x in data_t:
                        #     print(x)
                        # print("\n")
                        timelines += 1
                        break

    return timelines

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        data.append(list(line.strip()))

data_t = copy.deepcopy(data)
for i in range(1,len(data_t)):
    for j in range(1, len(data_t[0])-1):
        if data_t[i-1][j] == "S":
            data_t[i][j] = "|"

        if data_t[i-1][j] == "|":
            if data_t[i][j] == "^":
                data_t[i][j-1] = "|"
                data_t[i][j+1] = "|"
                total_splits += 1

                if len(split_nodes.keys()) == 0:
                    root = (i,j)
                split_nodes[(i,j)] = 0

            elif data_t[i][j] == ".":
                data_t[i][j] = "|"

total_timelines = probe_node(root[0], root[1])
print(total_timelines)    