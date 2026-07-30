"""Simple terminal-based Tic-Tac-Toe game."""

from __future__ import annotations

BOARD_SIZE = 3


def print_board(board: list[str]) -> None:
    """Print the board in a human-friendly format."""
    for row in range(0, len(board), BOARD_SIZE):
        print(" | ".join(board[row : row + BOARD_SIZE]))
        if row < len(board) - BOARD_SIZE:
            print("-" * 5)


def check_winner(board: list[str], player: str) -> bool:
    """Return True if the given player has a winning line."""
    win_lines = []
    for index in range(BOARD_SIZE):
        win_lines.append([index * BOARD_SIZE + offset for offset in range(BOARD_SIZE)])
        win_lines.append([index + offset * BOARD_SIZE for offset in range(BOARD_SIZE)])

    win_lines.append([0, 4, 8])
    win_lines.append([2, 4, 6])

    return any(all(board[position] == player for position in line) for line in win_lines)


def make_move(board: list[str], position: int, player: str) -> None:
    """Place a marker on the board if the move is valid."""
    if not 1 <= position <= 9:
        raise ValueError("Position must be between 1 and 9")

    index = position - 1
    if board[index] != " ":
        raise ValueError("That position is already taken")

    board[index] = player


def is_draw(board: list[str]) -> bool:
    """Return True when the board is full and nobody has won."""
    return " " not in board and not any(check_winner(board, player) for player in ("X", "O"))


def play_game() -> None:
    """Run a two-player game in the terminal."""
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Choose a position from 1 to 9:")
    print_board(board)

    while True:
        try:
            choice = input(f"Player {current_player}, choose a position: ").strip()
            position = int(choice)
            make_move(board, position, current_player)
        except ValueError as exc:
            print(f"Invalid move: {exc}")
            continue

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
