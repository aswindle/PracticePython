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

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

print(check_winner(winner_is_2))

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]
print(check_winner(winner_is_1))

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]
print(check_winner(winner_is_also_1))

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]
print(check_winner(no_winner))

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]
print(check_winner(also_no_winner))