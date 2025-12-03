
with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    for line in lines:
        line = line.strip()
        combined = 0
        for i, c in enumerate(line):
            c = int(c)
            for j, c2 in enumerate(line[i+1:]):
                c2 = int(c2)
                t = c*10 + c2
                if t > combined:
                    combined = t
        result += combined
    print(result)
    
