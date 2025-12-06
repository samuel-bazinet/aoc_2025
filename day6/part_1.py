from functools import reduce
ops = {
    "*",
    "+"
}

with open('input.txt', 'r') as file:
    lines = file.readlines()
    cols = []
    first_line = True
    for line in lines:
        line = line.strip().split()
        for i, num in enumerate(line):
            if num in ops:
                if num == "*":
                    cols[i] = int(reduce(lambda x, y: x*y, cols[i], 1))
                elif num == "+":
                    cols[i] = sum(cols[i])
                continue
            if first_line:
                cols.append([int(num)])
            else:
                cols[i].append(int(num))
        if first_line:
            first_line = False
    print(sum(cols))
    