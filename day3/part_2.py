
def recurse(line: str, d: int) -> int:
    combined = 0
    l = 0
    r = -d+1
    for _ in range(d):
        max_i = 0
        nl = 0
        t_line = line[l:r] if r < 0 else line[l:]
        for ind, j in enumerate(t_line):
            if j > max_i:
                max_i = j
                nl = ind+l
        combined = (combined * 10) + max_i
        l = nl+1
        r += 1
    return combined

with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    for line in lines:
        line = list(map(int, line.strip()))
        combined = recurse(line, 12)
        result += combined
    print(result)
    
