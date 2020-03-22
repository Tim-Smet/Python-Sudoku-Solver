sudoku = [
    [0,7,0,0,0,9,8,0,2],
    [6,8,0,0,5,0,1,3,0],
    [0,2,0,0,1,0,0,6,0],
    [0,0,6,1,8,0,2,0,3],
    [7,3,0,5,9,6,4,0,0],
    [0,0,0,0,7,0,0,0,0],
    [8,0,0,0,3,0,9,2,0],
    [0,9,3,0,0,0,5,4,1],
    [0,4,7,9,0,5,0,8,6]
]

def print_board(board):

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(9):
            if j % 3 == 0 and j!= 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

print_board(sudoku)

def find_zero(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)

