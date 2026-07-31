# """Simple terminal-based Tic-Tac-Toe game."""

# from __future__ import annotations

# BOARD_SIZE = 3


# def print_board(board: list[str]) -> None:
#     """Print the board in a human-friendly format."""
#     for row in range(0, len(board), BOARD_SIZE):
#         print(" | ".join(board[row : row + BOARD_SIZE]))
#         if row < len(board) - BOARD_SIZE:
#             print("-" * 5)


# def check_winner(board: list[str], player: str) -> bool:
#     """Return True if the given player has a winning line."""
#     win_lines = []
#     for index in range(BOARD_SIZE):
#         win_lines.append([index * BOARD_SIZE + offset for offset in range(BOARD_SIZE)])
#         win_lines.append([index + offset * BOARD_SIZE for offset in range(BOARD_SIZE)])

#     win_lines.append([0, 4, 8])
#     win_lines.append([2, 4, 6])

#     return any(all(board[position] == player for position in line) for line in win_lines)


# def make_move(board: list[str], position: int, player: str) -> None:
#     """Place a marker on the board if the move is valid."""
#     if not 1 <= position <= 9:
#         raise ValueError("Position must be between 1 and 9")

#     index = position - 1
#     if board[index] != " ":
#         raise ValueError("That position is already taken")

#     board[index] = player


# def is_draw(board: list[str]) -> bool:
#     """Return True when the board is full and nobody has won."""
#     return " " not in board and not any(check_winner(board, player) for player in ("X", "O"))


# def play_game() -> None:
#     """Run a two-player game in the terminal."""
#     board = [" "] * 9
#     current_player = "X"

#     print("Welcome to Tic-Tac-Toe!")
#     print("Choose a position from 1 to 9:")
#     print_board(board)

#     while True:
#         try:
#             choice = input(f"Player {current_player}, choose a position: ").strip()
#             position = int(choice)
#             make_move(board, position, current_player)
#         except ValueError as exc:
#             print(f"Invalid move: {exc}")
#             continue

#         print_board(board)

#         if check_winner(board, current_player):
#             print(f"Player {current_player} wins!")
#             break

#         if is_draw(board):
#             print("It's a draw!")
#             break

#         current_player = "O" if current_player == "X" else "X"


# if __name__ == "__main__":
#     play_game()
MAPSIZE = 10

a, b, c = ""

def draw_map:
    repeat 10:
       print( R1C1, "|", R1C2, "|", R1C3, "|", R1C4, "|", R1C5, "|", R1C6, "|", R1C7, "|", R1C8, "|", R1C9, "|", R1C10,)
       print( R2C1, "|", R2C2, "|", R2C3, "|", R2C4, "|", R2C5, "|", R2C6, "|", R2C7, "|", R2C8, "|", R2C9, "|", R2C10,)
       print( R3C1, "|", R3C2, "|", R3C3, "|", R3C4, "|", R3C5, "|", R3C6, "|", R3C7, "|", R3C8, "|", R3C9, "|", R3C10,)
       print( R4C1, "|", R4C2, "|", R4C3, "|", R4C4, "|", R4C5, "|", R4C6, "|", R4C7, "|", R4C8, "|", R4C9, "|", R4C10,)
       print( R5C1, "|", R5C2, "|", R5C3, "|", R5C4, "|", R5C5, "|", R5C6, "|", R5C7, "|", R5C8, "|", R5C9, "|", R5C10,)
       print( R6C1, "|", R6C2, "|", R6C3, "|", R6C4, "|", R6C5, "|", R6C6, "|", R6C7, "|", R6C8, "|", R6C9, "|", R6C10,)
       print( R7C1, "|", R7C2, "|", R7C3, "|", R7C4, "|", R7C5, "|", R7C6, "|", R7C7, "|", R7C8, "|", R7C9, "|", R7C10,)
       print( R8C1, "|", R8C2, "|", R8C3, "|", R8C4, "|", R8C5, "|", R8C6, "|", R8C7, "|", R8C8, "|", R8C9, "|", R8C10,)
       print( R9C1, "|", R9C2, "|", R9C3, "|", R9C4, "|", R9C5, "|", R9C6, "|", R9C7, "|", R9C8, "|", R9C9, "|", R9C10,)
       print( R10C1, "|", R10C2, "|", R10C3, "|", R10C4, "|", R10C5, "|", R10C6, "|", R10C7, "|", R10C8, "|", R10C9, "|", R10C10,)