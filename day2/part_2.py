
with open('input.txt', 'r') as file:
    lines = file.readlines()
    ranges = lines[0].split(',')
    result = set()
    for r in ranges:
        r = r.split('-')
        for i in range(int(r[0]), int(r[1])+1):
            i = str(i)
            l = len(i)
            for j in range(1,l//2+1):
                if l%j == 0:
                    if i[:j]*(l//j) == i:
                        result.add(int(i))
    result = sum(result)
    print(result)