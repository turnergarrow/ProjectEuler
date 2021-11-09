from euler import *

def candidates(node, costs, dim):
    c = []
    x = node[0]
    y = node[1]
    if x+1 < dim and costs[x+1, y] > 1e10:
        c.append((x+1, y))
    if x-1 >= 0 and costs[x-1, y] > 1e10:
        c.append((x-1, y))
    if y+1 < dim and costs[x, y+1] > 1e10:
        c.append((x, y+1))
    if y-1 >= 0 and costs[x, y-1] > 1e10:
        c.append((x, y-1))
    return c

def cost(m, inds):
    return m[inds[0], inds[1]]

def dijkstra(m):
    dim = len(m)
    visited = [(0, 0)]
    costs = np.ones((len(m[0]),len(m)))*np.inf
    costs[0, 0] = m[0, 0]
    last = (len(m)-1, len(m)-1)
    next = (0, 0)
    while next != last:
        minn = np.inf
        for n in visited:
            cs = candidates(n, costs, dim)
            for c in cs:
                cst = cost(costs, n)+cost(m, c)
                if cst < minn:
                    minn = cst
                    next = c
        visited.append(next)
        costs[next[0], next[1]] = minn
    out = int(costs[-1, -1])
    return out

def load_matrix(filename):
    rows = []
    with open(filename, 'r') as data:
        for line in data:
            col = []
            strp = line.strip('\n')
            splt = strp.split(',')
            for i in splt:
                col.append(int(i))
            rows.append(col)

    return np.array(rows)

@timer
def main():
    m = load_matrix('p083_matrix.txt')
    print(dijkstra(m))

if __name__ == "__main__":
    main()
