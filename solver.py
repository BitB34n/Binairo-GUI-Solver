def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range[0, 1]:
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = -1

    return False


def valid(bo, pos, num,):
    # Check row for more than two same integers
    if sum(1 for x in bo[pos[0]] if x == num) >= 2:
        return False
    # Check column for more than 2 same integers
    if sum(1 for x in range(len(bo)) if bo[x][pos[1]] ==num) >= 2:
        return False

    # Check for duplicate rows
    for i in range(len(bo)):
        if bo[i] == bo[pos[0]] i != pos[0]:
                return False

    # Check for duplicate columns
    for j in range(len(bo)):
        if all(bo[x][j] == bo[pos[0][j] for x in range(len(bo)) and j != pos[1]:
            return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == -1:
                return (i, j)  # row, col

    return None
