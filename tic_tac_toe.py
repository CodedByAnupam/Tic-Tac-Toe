board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def print_board(board):
    for i in range(3):
        for j in range(3):
            print(f"{board[i][j]} ", end="")
        print()


def user_input():
    pos = int(input(f"Enter a number 1 through 9: "))
    return pos - 1  # because list indexes are from 0-8 in the board


def place_pos(pos, player):
    row = pos // 3
    column = pos % 3
    board[row][column] = player
    return 1


def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                return
            else:
                continue
    print()
    print_board(board)
    print()
    print("The game is tied!")
    print()

    quit()

def check_column(j):
    x = 0
    o = 0
    for i in range(3):
        if board[i][j] == "X":
            x += 1
        elif board[i][j] == "O":
            o += 1
    if x == 3:
        print("X has won!")
        print()
        quit()
    elif o == 3:
        print("Y has won")
        print()
        quit()


def check_row(i):
    x = 0
    o = 0
    for j in range(3):
        if board[i][j] == "X":
            x += 1
        elif board[i][j] == "Y":
            o += 1
    if x == 3:
        print("X has won!")
        print()
        quit()
    elif o == 3:
        print("O has won!")
        print()
        quit()


def check_diagonal(a, b, c):
    diag = [a, b, c]
    x = 0
    o = 0
    for i in diag:
        if i == "X":
            x += 1
        elif i == "O":
            o += 1
    if x == 3:
        print("X has won!")
        print()
        quit()
    elif o == 3:
        print("O has won!")
        print()
        quit()


def main():
    turn = 0
    game_on = True

    while game_on:
        print()
        if turn % 2 == 0:
            player = "X"
        else:
            player = "O"
        print_board(board)
        print()
        pos = user_input()
        turn += place_pos(pos, player)
        check_tie(board)
        print()

        for j in range(3):
            check_column(j)
            check_row(j)
            check_diagonal(board[0][0], board[1][1], board[2][2])
            check_diagonal(board[0][2], board[1][1], board[2][0])


if __name__ == "__main__":
    main()

    # play_again()


# def play_again():
#     again = input("Do you want to play again? Y/N ")
#     if again.lower == "y":
#         return True
#     else:
#         return False
