# solver.py
def solve(bo):
    """
    Solves a binairo board using backtracking
    :param bo: 2d list of ints
    :return: solution
    """
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,11):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, pos, num):
    """
    Returns if the attempted move is valid for Binairo
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int (0 or 1)
    :return: bool
    """
   # Check row for more than two same integers
    if sum(1 for x in bo[pos[0]] if x == num) >= 2:
        return False

    # Check column for more than two same integers
    if sum(1 for x in range(len(bo)) if bo[x][pos[1]] == num) >= 2:
        return False

    # Check for duplicate rows
    for i in range(len(bo)):
        if bo[i] == bo[pos[0]] and i != pos[0]:
            return False

    # Check for duplicate columns
    for j in range(len(bo)):
        if all(bo[x][j] == bo[pos[0]][j] for x in range(len(bo))) and j != pos[1]:
            return False

    return True

    # # Check row
    # for i in range(0, len(bo)):
    #     if bo[pos[0]][i] == num and pos[1] != i:
    #         return False

    # # Check Col
    # for i in range(0, len(bo)):
    #     if bo[i][pos[1]] == num and pos[1] != i:
    #         return False

    # # Check box

    # box_x = pos[1]//3
    # box_y = pos[0]//3

    # for i in range(box_y*3, box_y*3 + 3):
    #     for j in range(box_x*3, box_x*3 + 3):
    #         if bo[i][j] == num and (i,j) != pos:
    #             return False

    # return True


def find_empty(bo):
    """
    finds an empty space in the board
    :param bo: partially complete board
    :return: (int, int) row col
    """

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def print_board(bo):
    """
    prints the board
    :param bo: 2d List of ints
    :return: None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")

