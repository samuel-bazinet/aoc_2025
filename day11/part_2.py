from functools import cache

with open('input.txt', 'r') as file:
    lines = file.readlines()
    conns: dict[str, tuple[str, list[str]]] = {}
    for line in lines:
        line = line.strip().split(':')
        outs = []
        for out in line[1].strip().split():
            outs.append(out)
        conns[line[0]] = (line[0], outs)

    @cache
    def process(cur: tuple[str, str], f_v: bool, d_v: bool) -> int:
        global conns
        result = 0
        for out in conns[cur][1]:
            if out == 'out':
                if f_v and d_v:
                    result += 1
            else:
                if out == 'fft':
                    result += process(out, True, d_v)
                elif out == 'dac':
                    result += process(out, f_v, True)
                else:
                    result += process(out, f_v, d_v)
        return result

    result = 0
    result += process('svr', False, False)

    print(result)