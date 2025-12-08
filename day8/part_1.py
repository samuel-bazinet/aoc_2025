from math import sqrt
import bisect
def euclid_dist(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)

with open('input.txt', 'r') as file:
    lines = file.readlines()
    junctions = []
    dists = []
    circuits: list[set] = []
    for line in lines:
        junctions.append(tuple(map(int, line.strip().split(','))))
    for j in junctions:
        for d in junctions:
            if j == d:
                continue
            dist = euclid_dist(j, d)
            if ((d, j), dist) not in dists:
                bisect.insort(dists, ((j, d), dist), key= lambda x: x[1])
                if len(dists) > 1000:
                        dists.pop()
    for d in dists:
        cur = d[0]
        added = -1
        idx = -1
        for j in range(len(circuits)):
            if cur[0] in circuits[j]:
                if added > 0:
                    circuits[j].update(circuits[added])
                    circuits.pop(added)
                    added = -2
                    break
                else:
                    added = j
                    idx = 1
            elif cur[1] in circuits[j]:
                if added > 0:
                    circuits[j].update(circuits[added])
                    circuits.pop(added)
                    added = -2
                    break
                else:
                    added = j
                    idx = 0
        if added == -1:
            circuits.append(set(cur))
        elif added > -1:
            circuits[added].add(cur[idx])
    lens = sorted(list(len(c) for c in circuits), reverse=True)
    print(lens[0]*lens[1]*lens[2])