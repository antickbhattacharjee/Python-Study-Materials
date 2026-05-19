# tic-tac-tow game Player vs Player

def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9) 
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (row and column, e.g., 1 2): ")
        try:
            row, col = map(int, move.split())
            if board[row][col] == " ":
                board[row][col] = current_player
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f"Player {winner} wins! 🎉")
                    break
                if is_board_full(board):
                    print_board(board)
                    print("It's a draw! 🤝")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe! 🎮")
    play_game()