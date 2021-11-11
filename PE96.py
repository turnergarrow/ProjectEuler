from euler import *

def load_file(filename):
    boards = []
    with open(filename, 'r') as data:
        for line in data:
            if line[:4] == "Grid":
                rows = []
                boards.append(rows)
                continue
            strp = line.strip('\n')
            col = []
            for i in strp:
                col.append(np.array(int(i)))
            rows.append(np.array(col))
    return np.array(boards)

def check_vertical(board, p, n):
    y = p[0]
    x = p[1]
    for i in range(9):
        if board[i, x] == n:
            return False
    return True

def check_horizontal(board, p, n):
    y = p[0]
    x = p[1]
    for i in range(9):
        if board[y, i] == n:
            return False
    return True

def check_subsquare(board, p, n):
    y = p[0]
    x = p[1]

    sub_x = x//3
    sub_y = y//3
    for i in range(9):
        x_i = 3*sub_x + i%3
        y_i = 3*sub_y + i//3
        if board[y_i, x_i] == n:
            return False
    return True

def is_valid(board, p, n):
    return check_vertical(board, p, n) and check_horizontal(board, p, n) and check_subsquare(board, p, n)

def find_next(board):
    for x in range(9):
        for y in range(9):
            if board[y, x] == 0:
                return x, y
    return -1, -1

def get_possibilities(board, p):
    poss = []
    for n in range(1, 10):
        if is_valid(board, p, n):
            poss.append(n)
    return poss

def simple_solve(board):
    for x in range(9):
        for y in range(9):
            if board[y, x] == 0:
                poss = get_possibilities(board, [y, x])
                if len(poss) == 0:
                    return False
                if len(poss) == 1:
                    board[y, x] = poss[0]
                    simple_solve(board)
    return True

def solve(board):
    # rollback = cp.deepcopy(board)
    # if not simple_solve(rollback):
    #     return False
    # else:
    #     simple_solve(board)
    x, y = find_next(board)
    if x == -1:
        return True
    for n in range(1, 10):
        if is_valid(board, [y, x], n):
            board[y, x] = n
            if solve(board):
                return True
            else:
                board[y, x] = 0
    return False

@timer
def main():
    m = load_file('p096_sudoku.txt')
    tot = 0
    for board in m:
        tf = solve(board)
        v = board[0, 0]*100+board[0, 1]*10+board[0, 2]
        tot += v

    print(tot)



if __name__ == "__main__":
    main()
