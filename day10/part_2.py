from dataclasses import dataclass
import cvxpy as cp
import numpy as np

@dataclass
class Machine:
    buttons: list[list[int]]
    joltage: list[int]
                

with open('practice.txt', 'r') as file:
    lines = file.readlines()
    machines: list[Machine] = []
    c_result = 0
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

    for line, m in enumerate(machines):
        alt_but = []
        for but in m.buttons:
            n_but = []
            for i in range(len(m.joltage)):
                if i in but:
                    n_but.append(1)
                else:
                    n_but.append(0)
            alt_but.append(n_but)
        A = np.array(alt_but).T

        var = cp.Variable(len(alt_but), nonneg=True, integer=True)
        target = cp.Parameter(len(m.joltage))
        target.value = np.array(m.joltage)
        objective = cp.Minimize(cp.sum(A @ var - target))
        constraints = [var <= sum(m.joltage), A @ var - target >= 0]
        prob = cp.Problem(objective, constraints)
        print(prob.solve(), m.joltage, var.value)
        print(sum(map(round, var.value)))
        c_result += sum(map(round, var.value))

    print(c_result)
    
