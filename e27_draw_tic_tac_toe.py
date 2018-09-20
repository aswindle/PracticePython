def draw_border():
    line = "  "
    for c in range(0, 3):
        line+= "-" + str(c) + "- "
    print(line)
    
def draw_row(board, r):
    line = str(r) + "|"
    for c in range(0,3):
        element = board[r][c]
        if element == 0:
            line += "   |"
        elif element == 1:
            line+= " X |"
        else:
            line += " O |"
    print(line)
    
def draw_board(board):
    draw_border()
    for r in range(0, 3):
        draw_row(board, r)
    draw_border()
    
def check_rows(board):
    for r in range(0, 3):
        if board[r][0]!=0 and board[r][0]==board[r][1]==board[r][2]:
            return board[r][0]
    return 0

def check_cols(board):
    for c in range(0, 3):
        if board[0][c]!=0 and board[0][c]==board[1][c]==board[2][c]:
            return board[0][c]
    return 0

def check_diags(board):
    if board[0][0]!=0 and board[0][0] == board[1][1] == board [2][2]:
        return board[0][0]
    elif board[0][2]!=0 and board[0][2] == board[1][1] == board [2][0]:
        return board[0][0]
    return 0

def check_winner(board):
    if check_rows(board)!= 0: return check_rows(board)
    elif check_cols(board)!= 0: return check_cols(board)
    elif check_diags(board)!= 0: return check_diags(board)
    else: return 0

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
draw_board(board)
moves = 0
while(moves<9):
    x_play_string = input("Player 1 (X) enter row, column: ").split(",")
    x_row = int(x_play_string[0].strip())
    x_col = int(x_play_string[1].strip())
    while board[x_row][x_col]!=0:
        x_play_string = input("Player 1 (X) enter row, column: ").split(",")
        x_row = int(x_play_string[0].strip())
        x_col = int(x_play_string[1].strip())
    board[x_row][x_col]=1
    moves +=1
    
    draw_board(board)
    if check_winner(board)==1:
        print("Player 1 wins!")
        break
    if moves==9:
        print("The game is a draw.") 
        break
    
    o_play_string = input("Player 2 (O) enter row, column: ").split(",")
    o_row = int(o_play_string[0].strip())
    o_col = int(o_play_string[1].strip())
    while board[o_row][o_col]!=0:
        o_play_string = input("Player 2 (O) enter row, column: ").split(",")
        o_row = int(o_play_string[0].strip())
        o_col = int(o_play_string[1].strip())
    board[o_row][o_col]=2
    moves +=1
    
    draw_board(board)
    if check_winner(board)==2:
        print("Player 2 wins!")
        break
print("Game Over")