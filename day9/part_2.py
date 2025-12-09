from shapely.geometry  import Point
from shapely.geometry.polygon import Polygon

def dist(a: tuple[int, int], b: tuple[int, int]) -> int:
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

with open('input.txt', 'r') as file:

    lines = file.readlines()
    coords: list[tuple[int, int]] = []
    for line in lines:
        line = line.strip().split(',')
        x = int(line[0])
        y = int(line[1])
        coords.append((x, y))

    poly = Polygon(coords)

    maxi = 0
    for s in coords:
        for e in coords:
            if s == e:
                continue
            s_x = s[0]
            s_y = s[1]
            e_x = e[0]
            e_y = e[1]
            c = (s_x, e_y)
            p = (e_x, s_y)
            rec = Polygon([s, c, e, p])
            if poly.contains(rec):
                d = dist(s, e)
                if d > maxi:
                    maxi = d

    print(maxi)