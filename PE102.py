from euler import *

def get_triangles(filename):
    triangles = []

    with open(filename, 'r') as data:
        for line in data:
            strp = line.strip('\n')
            splt = strp.split(',')
            points = [{'x':int(splt[0]),
                       'y':int(splt[1])},
                      {'x':int(splt[2]),
                       'y':int(splt[3])},
                      {'x':int(splt[4]),
                       'y':int(splt[5])}]
            triangles.append(points)

    return triangles

def get_area(triangle):
    A = triangle[0]
    B = triangle[1]
    C = triangle[2]
    return abs((A['x']*(B['y']-C['y'])+B['x']*(C['y']-A['y'])+C['x']*(A['y']-B['y']))/2)

def get_area_sum(triangle):
    A = cp.deepcopy(triangle)
    A[0]['x'] = 0
    A[0]['y'] = 0
    B = cp.deepcopy(triangle)
    B[1]['x'] = 0
    B[1]['y'] = 0
    C = cp.deepcopy(triangle)
    C[2]['x'] = 0
    C[2]['y'] = 0

    return get_area(A)+get_area(B)+get_area(C)

def includes_origin(triangle):
    area = get_area(triangle)
    area_sum = get_area_sum(triangle)
    return m.isclose(area, area_sum, rel_tol=1e-9)


if __name__ == "__main__":
    triangles = get_triangles('p102_triangles.txt')
    tot = 0
    for triangle in triangles:
        if includes_origin(triangle):
            tot += 1
    print(tot)
