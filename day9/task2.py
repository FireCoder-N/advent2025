import os

data = []
rows = {}
cols = {}
max_area = 0

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        p = [int(i) for i in line.strip().split(",")]
        data.append(p)

        if p[0] not in cols:
            cols[p[0]] = []
        cols[p[0]].append(p[1])
        cols[p[0]].sort()

        if p[1] not in rows:
            rows[p[1]] = []
        rows[p[1]].append(p[0])
        rows[p[1]].sort()


for i in range(len(data)):
    for j in range(len(data)):
        E = (1 + abs(data[j][0] - data[i][0])) * (1 + abs(data[j][1] - data[i][1]))
        flag = True

        corners = [[data[i][0], data[j][1]], [data[j][0], data[i][1]]]
        for c in corners:
            
            if c[0] < rows[c[1]][0]:
                for l in [cols[k] for k in cols.keys() if k <= c[0]]:
                    if l[0] <= c[1] <= l[-1]:
                        break
                else:
                    flag = False
                    break

            if c[0] > rows[c[1]][-1]:
                for l in [cols[k] for k in cols.keys() if k >= c[0]]:
                    if l[0] <= c[1] <= l[-1]:
                        break
                else:
                    flag = False
                    break


            if c[1] < cols[c[0]][0]:
                for l in [rows[k] for k in rows.keys() if k <= c[1]]:
                    if l[0] <= c[0] <= l[-1]:
                        break
                else:
                    flag = False
                    break

            if c[1] > cols[c[0]][-1]:
                for l in [rows[k] for k in rows.keys() if k >= c[1]]:
                    if l[0] <= c[0] <= l[-1]:
                        break
                else:
                    flag = False
                    break

        if flag and E > max_area:
            max_area = E

print(max_area)