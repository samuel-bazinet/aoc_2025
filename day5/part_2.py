
with open('input.txt', 'r') as file:
    lines = file.readlines()
    ranges = []
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            r_m = False
            break
        line = list(map(lambda x: int(x), line.split('-')))
        ranges.append([int(line[0]), int(line[1])])
    
    ranges.sort(key = lambda x: x[0])

    n_ranges = []
    for r in ranges:
        r_mod = False
        for n in n_ranges:
            if n[0] <= r[0] <= n[1] and r[1] > n[1]: # starts in and extends
                n[1] = r[1]
                r_mod = True
                break
            elif n[1] >= r[0] >= n[0] and r[1] <= n[1]: # starts in and is enclosed
                r_mod = True
                break
        if not r_mod:
            n_ranges.append(r)


    result = 0
    for r in n_ranges:
        result += r[1]-r[0] + 1
    print(result)