board = [
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

def print_board(sudoku):

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(9):
            if j % 3 == 0 and j!= 0:
                print(" | ", end="")

            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")

print_board(board)
