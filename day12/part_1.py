#from functools import cache
from copy import deepcopy
import numpy as np

default = np.array([[False, False, False],[False, False, False],[False, False, False]])

def fits(idx: int, dim: tuple[int, int], grid: list[list[bool]], shape_c: list[int]) -> bool:
    if shape_c[idx] <= 0:
        idx += 1
    if idx >= len(shape_c):
        return True
    shape_c[idx] -= 1
    shape = np.array(shapes[idx][1])
    for _ in range(4):
        for i in range(dim[0]):
            for j in range(dim[1]):
                s_fits = True
                s_dim = shape.shape
                if i+s_dim[0] > dim[0] or j+s_dim[1] > dim[1]:
                    continue
                for x in range(s_dim[0]):
                    for y in range(s_dim[1]):
                        if shape[x,y] and not (grid[i+x,j+y] != shape[x,y]):
                            s_fits = False
                            break
                    if not s_fits:
                        break
                if s_fits:
                    grid[i:i+s_dim[0], j:j+s_dim[1]] = shape
                    r = fits(idx, dim, grid, shape_c)
                    if r:
                        return True
                    else:
                        grid[i:i+s_dim[0], j:j+s_dim[1]] = default


        np.rot90(shape)
    return False
                
def calculate_area(s: list[list[bool]]) -> int:
    a = 0
    for r in s:
        for v in r:
            if v:
                a += 1
    return a

with open('input.txt', 'r') as file:
    lines = file.readlines()
    shapes_l = lines[:30]
    areas_l = lines[30:]
    shapes: list[tuple[int, list[list[bool]]]] = []
    cur_shape = []
    for l in shapes_l:
        l = l.strip()
        if len(l) > 0:
            if l[-1] == ":" :
                if cur_shape != []:
                    shapes.append((calculate_area(cur_shape), cur_shape))
                cur_shape = []
            else:
                cur_shape.append([c == '#' for c in l])
    shapes.append((calculate_area(cur_shape), cur_shape))

    counter = 0
    for a in areas_l:
        a = a.strip().split(':')
        dim = tuple(map(int, a[0].split('x')))
        shape_c = list(map(int, a[1].split()))
        needed = 0

        for idx, num in enumerate(shape_c):
            needed += num*shapes[idx][0]
        if dim[0]*dim[1]-needed >= 0:
            grid = np.array([[False for _ in range(dim[1])] for _ in range(dim[0])])
            if fits(0, dim, grid, shape_c):
                counter += 1
    
    print(counter)
