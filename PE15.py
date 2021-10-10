n = 20

grid = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(len(grid)):
    grid[0][i] = 1

for i in range(len(grid)):
    for j in range(len(grid)):
        grid[j][0] = 1

for i in range(1, len(grid)):
    for j in range(1, len(grid)):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid[n][n])
