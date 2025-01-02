
def draw_board(board):
    """ Creates 3x3 game board """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def get_player_info():
    """ Function for entering the name and selecting the players' symbols. If the symbol is not selected,
        program assigns it automatically. """
    print("*" * 13, "WELCOME TO TIC TAC TOE GAME", "*" * 13)

    # First player's name
    player1_name: str = input("Player 1, enter your name: ").strip()
    if not player1_name:
        player1_name = "Player 1"

    # A symbol for the first player
    player1_symbol: str = input(f"{player1_name}, choose your symbol (X or O): ").upper()
    if player1_symbol not in ["X", "O"]:
        player1_symbol = "X" # default choice
        print(f"You didn't choose your symbol or your input was wrong. Your symbol: {player1_symbol}")

    # Second player's name
    player2_name: str = input("Player 2, enter your name: ").strip()
    if not player2_name:
        player2_name = "Player 2"

    # A symbol for the second player
    player2_symbol: str = "O" if player1_symbol == "X" else "X"
    print(f"{player2_name}, your symbol was assigned automatically: {player2_symbol}")

    return (player1_name, player1_symbol), (player2_name, player2_symbol)

def check_winner(board) -> bool:
    """ Checks if there is a winner """
    # Checks rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    # Checks columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != " ":
            return True

    # Checks diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def check_tie(board) -> bool:
    """ Checks if the entire board is filled (tie) """
    for row in board:
        if " " in row:
            return False

    return True

def play_x_o():
    """ The main function of the game """
    while True: # loop for replay
        # Get information about players
        player1, player2 = get_player_info()
        player1_name, player1_symbol = player1
        player2_name, player2_symbol = player2

        # Create a game board
        board: list = [[" " for _ in range(3)] for _ in range(3)]
        if player1_symbol == "X":
            current_player_name, current_symbol = player1_name, player1_symbol
            next_player_name, next_symbol = player2_name, player2_symbol
        else:
            current_player_name, current_symbol = player2_name, player2_symbol
            next_player_name, next_symbol = player1_name, player1_symbol

        while True: # The main game loop
            draw_board(board)
            print(f"Player {current_player_name}, your turn (symbol {current_symbol}).")

            # Player's move
            try:
                row: int = int(input("Enter row number (0-2): "))
                column: int = int(input("Enter column number (0-2): "))
                if board[row][column] != " ":
                    print("This cell is already filled. Try again.")
                    continue
            except ValueError as e:
                print("Invalid input, use numbers only. ", e)
                continue
            except IndexError as e:
                print("Use numbers from 0 to 2 only. ", e)
                continue

            # Set player's symbol
            board[row][column] = current_symbol

            # Checking if there is a winner
            if check_winner(board):
                draw_board(board)
                print(f"CONGRATULATIONS!!! Player {current_player_name} is a winner!!!")
                break

            # Checking if there is a tie
            if check_tie(board):
                draw_board(board)
                print("Tie!")
                break

            # Players' change
            current_player_name, current_symbol, next_player_name, next_symbol = (
                next_player_name, next_symbol, current_player_name, current_symbol
            )

        play_again: str = input("Play again? (Yes/No): ").strip().lower()
        if play_again == "Yes".strip().lower():
            continue
        else:
            print("Thank you, see you next time ;)")
            break


# Let's play the game
if __name__ == "__main__":
    play_x_o()