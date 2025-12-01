
with open('input.txt', 'r') as file:
    lines = file.readlines()
    cur = 50
    res = 0
    for line in lines:
        started_at_0 = cur == 0
        v = int(line[1:])
        if line[0] == "L":
            #print(f"left, {v}")
            cur -= v
            while cur < 0:
                if not started_at_0:
                    #print("passed 0")
                    res += 1
                cur += 100
                started_at_0 = False
            if cur == 0:
                #print("at 0")
                res += 1
            
        else:
            #print(f"right, {v}")
            cur += v
            while cur > 99:
                #print("passed 0")
                res += 1
                cur -= 100
            if cur == 100:
                cur = 0
        #print(cur)

    print(res)

