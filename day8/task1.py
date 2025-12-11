import os
import heapq

data = []
total = 1
circuits = []
connections = []

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        data.append([int(i) for i in line.strip().split(",")])

for i in range(len(data)):
    for j in range(i+1, len(data)):
        dist = ((data[i][0]-data[j][0])**2 + (data[i][1]-data[j][1])**2 + (data[i][2]-data[j][2])**2)**0.5
        heapq.heappush(connections, (dist, i, j))

for _ in range(1000):
    _, i, j = heapq.heappop(connections)

    ci = None
    cj = None
    for idx_c, c in enumerate(circuits):
        if i in c:
            ci = idx_c
        if j in c:
            cj = idx_c
    
    if ci is None and cj is None:
        circuits.append([i,j])

    elif ci is None:
        circuits[cj].append(i)

    elif cj is None:
        circuits[ci].append(j)

    elif ci == cj:
        continue
    
    else:
        # ci != cj
        circuits[ci] += circuits[cj]
        del circuits[cj]

circuits.sort(key=lambda x:[len(x), x[0]], reverse=True)

for i in range(min(3, len(circuits))):
    total *= len(circuits[i])

print(total)