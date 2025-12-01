
with open('input.txt', 'r') as file:
    lines = file.readlines()
    cur = 50
    res = 0
    for line in lines:
        v = int(line[1:])
        if line[0] == "L":
            #print(f"left, {v}")
            cur -= v
            while cur < 0:
                cur += 100
        else:
            #print(f"right, {v}")
            cur += v
            while cur > 99:
                cur -= 100
        if cur ==0:
            res += 1

    print(res)

