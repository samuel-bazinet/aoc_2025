
with open('input.txt', 'r') as file:
    lines = file.readlines()
    ranges = lines[0].split(',')
    result = 0
    for r in ranges:
        r = r.split('-')
        for i in range(int(r[0]), int(r[1])+1):
            i = str(i)
            l = len(i)
            if l % 2 == 0:
                if i[:l//2] == i[l//2:]:
                    result += int(i)
    print(result)