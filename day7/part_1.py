
with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [[c for c in line] for line in lines]
    split_loc = []
    s_loc = 0
    for col, c in enumerate(lines[0]):
            if c == 'S':
                s_loc = col

    hit = set()
    active_c = set()
    active_c.add(s_loc)
    for r in range(len(lines)):
        n_a = set()
        for c in active_c:
            if lines[r][c] == '^':
                hit.add((r, c))
                if c != 0:
                    n_a.add(c-1)
                if c!= len(lines[0])-1:
                     n_a.add(c+1)
            else:
                 n_a.add(c)
        active_c = n_a
    print(len(hit))
            

