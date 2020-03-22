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

def solve(board):
    find = find_zero(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if check_number_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False

def check_number_valid(board, number, position):
    #Check row
    for i in range(9):
        if board[position[0]][i] == number and position[1] != i:
            return False

    #Check column
    for i in range(9):
        if board[i][position[1]] == number and position[0] != i:
            return False      

    #Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True

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

def find_zero(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)

    return None


print_board(sudoku)
solve(sudoku)
print("-------------------")
print_board(sudoku)
