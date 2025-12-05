
with open('input.txt', 'r') as file:
    lines = file.readlines()
    r_m = True
    ranges = []
    result = 0
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            r_m = False
            continue
        if r_m:
            line = line.split('-')
            ranges.append(range(int(line[0]), int(line[1])+1))
        else:
            for r in ranges:
                if int(line) in r:
                    result += 1
                    break

    print(result)