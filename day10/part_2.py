from dataclasses import dataclass
import cvxpy as cp
import numpy as np
import z3

@dataclass
class Machine:
    buttons: list[list[int]]
    joltage: list[int]
                

with open('input.txt', 'r') as file:
    lines = file.readlines()
    machines: list[Machine] = []
    for line in lines:
        line = line.strip().split()
        m = Machine([], [])
        for s in line:
            if s[0] == '[':
                pass
            elif s[0] == '(':
                s = s[1:-1].split(',')
                li = []
                for l in s:
                    li.append(int(l))
                m.buttons.append(li)
            else:
                s = s[1:-1].split(',')
                m.joltage = list(map(int, s))
        machines.append(m)

    result = 0
    for line, m in enumerate(machines):
        solver = z3.Optimize()
        variables = []
        joltage_var = [None] * len(m.joltage)
        for name, b in enumerate(m.buttons):
            var = z3.Int(str(name))

            variables.append(var)

            solver.add(var >= 0)

            for entry in b:
                if joltage_var[entry] is None:
                    joltage_var[entry] = var
                else:
                    joltage_var[entry] = joltage_var[entry] + var
        
        for jolt_int, entry in enumerate(m.joltage):
            if joltage_var[jolt_int] is None:
                continue
            solver.add(m.joltage[jolt_int] == joltage_var[jolt_int])
        
        total_press = solver.minimize(sum(variables))

        if solver.check() == z3.sat:
            result += total_press.value().as_long()
        else:
            assert False

    print(result)
    
