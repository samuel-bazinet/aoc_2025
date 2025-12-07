
with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [[c for c in line] for line in lines]
    split_loc = []
    s_loc = 0
    for col, c in enumerate(lines[0]):
            if c == 'S':
                s_loc = col

    active_c = {}
    active_c[s_loc] = 1
    for r in range(len(lines)):
        n_a = {}
        for c, v in active_c.items():
            if lines[r][c] == '^':
                if c != 0:
                    if c-1 not in n_a:
                        n_a[c-1] = v
                    else:
                         n_a[c-1] += v
                if c!= len(lines[0])-1:
                    if c+1 not in n_a:
                        n_a[c+1] = v
                    else:
                         n_a[c+1] += v
            else:
                if c not in n_a:
                    n_a[c] = v
                else:
                    n_a[c] += v
        active_c = n_a
    print(sum(active_c.values()))
            

