
with open('input.txt', 'r') as file:
    lines = file.readlines()
    conns: dict[str, tuple[str, list[str]]] = {}
    for line in lines:
        line = line.strip().split(':')
        outs = []
        for out in line[1].strip().split():
            outs.append(out)
        conns[line[0]] = (line[0], outs)
    result = 0
    stack = []
    stack.append(conns["you"])
    while len(stack) > 0:
        cur = stack.pop()
        for out in cur[1]:
            if out == 'out':
                result += 1
            else:
                stack.append(conns[out])

    print(result)