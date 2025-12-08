import os

total = 0
data = []
numbers = []
op_index = -1

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        data.append(line[:-1])

op = data[-1].split()
data = data[:-1]
for i in range(-1, -len(data[0])-1, -1):
    col = [data[x][i] for x in range(len(data))]

    if len(set(col)) == 1 and col[0] == " ":
        total += eval(f"{op[op_index]}".join(numbers))
        numbers = []
        op_index -= 1
    else:
        numbers.append("".join([x for x in col if x != " "]))

total += eval(f"{op[op_index]}".join(numbers))
print(total)