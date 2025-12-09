
def dist(a: tuple[int, int], b: tuple[int, int]) -> int:
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

with open('input.txt', 'r') as file:
    lines = file.readlines()
    coords = []
    for line in lines:
        line = line.strip().split(',')
        coords.append((int(line[0]), int(line[1])))
    maxi = 0
    for coord in coords:
        for c2 in coords:
            if coord == c2:
                continue
            d = dist(coord, c2) 
            if d > maxi:
                maxi = d

    print(maxi)