from connect4 import Connect4
from typing import Tuple, List




def heuristic(game: Connect4) -> int:
    board = game.state()
    

    ROWS = len(board)
    COLS = len(board[0])

    score = 0

    def eval_board(window):
        nonlocal score # allows changes to the outside score variable

        o_count = window.count("O")
        x_count = window.count("X")
        empty = window.count(".")

        if o_count == 4: # If there is a connect4
            score += 100 # Winner winner
        elif o_count == 3 and empty == 1: #If there is a connect3 and and empty slot next to it
            score += 55
        elif o_count == 2 and empty == 2: #If there is a connect2 and and 2 empty slots next to it
            score += 2

        if x_count == 4: # same as the top, but for x instead of O
            score -= 100
        elif x_count == 3 and empty == 1:
            score -= 55
        elif x_count == 2 and empty == 2:
            score -= 2


    # horizontal
    for r in range(ROWS): #Loop through each row index. Looks through one row at a time
        for c in range(COLS - 3): # Only looks for 4 spaces, because thats all you need to win. Maybe change to 5 for better searches?
            window = [board[r][c+i] for i in range(4)] #Builds a list of 4 cells
            eval_board(window) #Scores what we have found
            

    # vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            window = [board[r+i][c] for i in range(4)] #Start at row r, and go to row r+3. C is the collumns          
            eval_board(window)
            

    # diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [board[r+i][c+i] for i in range(4)] # Top left to bottom right
            eval_board(window)
            

    # diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            window = [board[r-i][c+i] for i in range(4)] #Bottom left to top right
            eval_board(window)

            
    
    return score


def minimax(game:Connect4, player:str, max_depth:int = 5, cur_depth:int = 0, alpha: float = float("-inf"), beta: float = float("inf")) -> Tuple[int, int]:
    is_over, winner = game.is_terminal()
    if is_over:
        if winner == "O":
            return 1000, None
        elif winner == "X":
            return -1000, None
        elif winner == "Tie":
            return 0, None
        
    if cur_depth == max_depth:
        return heuristic(game), None
        
    if player == "max":
        max_eval = float("-inf")
        max_action = None

        for a in game.actions():
            sub_game = Connect4(game.state(), game.to_move())
            sub_game.make_move(a)

            c_eval, _ = minimax(sub_game, "min", max_depth, cur_depth+1, alpha, beta)
            if c_eval > max_eval:
                max_eval = c_eval
                max_action = a

            alpha = max(alpha, max_eval)

            if beta <= alpha:
                break
        return max_eval, max_action
    

    if player == "min":
        min_eval = float("inf")
        min_action = None

        for a in game.actions():
            sub_game = Connect4(game.state(), game.to_move())
            sub_game.make_move(a)

            c_eval, _ = minimax(sub_game, "max", max_depth, cur_depth+1, alpha, beta)
            if c_eval < min_eval:
                min_eval = c_eval
                min_action = a

            beta = min(beta, min_eval)

            if beta <= alpha:
                break
        return min_eval, min_action
    






    
    



