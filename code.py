=== app.py ===
```python
def initialize_game():
    return [[' ' for _ in range(3)] for _ in range(3)], 'X'

def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def switch_player(player):
    return 'O' if player == 'X' else 'X'

def check_game_status(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0], "Win"
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col], "Win"
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0], "Win"
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2], "Win"
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return None, "Draw"
    return None, "Continue"

def end_game(winner, status):
    if winner:
        print(f"Player {winner} wins!")
    elif status == "Draw":
        print("The game is a draw!")
    print("Game Over!")

def main():
    board, player = initialize_game()
    while True:
        display_board(board)
        row, col = map(int, input(f"Player {player}, enter your move (row col): ").split())
        if not make_move(board, row, col, player):
            print("Invalid move, try again.")
            continue
        winner, status = check_game_status(board)
        if winner or status == "Draw":
            end_game(winner, status)
            break
        player = switch_player(player)

if __name__ == "__main__":
    main()
```

=== templates/index.html ===
```

=== static/styles.css ===
```