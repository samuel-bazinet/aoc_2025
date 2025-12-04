
with open('input.txt', 'r') as file:
    lines = file.readlines()
    grid = [[c for c in line.strip()] for line in lines]
    result = 0
    dirs = [-1, 0, 1]
    p_res = -1
    while p_res != 0:
        p_res = 0
        for iidx, line in enumerate(grid):
            for jidx, o in enumerate(line):
                if o == "@":
                    sum = 0
                    for i in dirs:
                        for j in dirs:
                            if i == 0 and j == 0:
                                continue
                            ipos = iidx + i
                            jpos = jidx + j
                            if ipos >= 0 and ipos < len(grid):
                                if jpos >= 0 and jpos < len(line):
                                    if grid[ipos][jpos] == "@":
                                        sum += 1
                        if sum >= 4:
                            break
                    if sum < 4:
                        grid[iidx][jidx] = "x"
                        p_res += 1
        result += p_res
    print(result)