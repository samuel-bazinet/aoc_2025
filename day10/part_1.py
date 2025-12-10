from dataclasses import dataclass
from itertools import combinations

@dataclass
class Machine:
    target_light: int
    buttons: list[int]

with open('input.txt', 'r') as file:
    lines = file.readlines()
    machines: list[Machine] = []
    result = 0
    for line in lines:
        line = line.strip().split()
        m = Machine(0, [])
        for s in line:
            if s[0] == '[':
                s = s[1:-1]
                for i, l in enumerate(s):
                    if l == "#":
                        m.target_light += (1 << i)
            elif s[0] == '(':
                s = s[1:-1].split(',')
                n = 0
                for l in s:
                    n += 1 << int(l)
                m.buttons.append(n)
        machines.append(m)
    for m in machines:
        found = False
        for i in range(1, len(m.buttons)):
            opts = list(combinations(m.buttons, i))
            for opt in opts:
                init = 0
                for op in opt:
                    init ^= op
                if init == m.target_light:
                    found = True
                    result += i
                    break
            if found:
                break
    print(result)
    
