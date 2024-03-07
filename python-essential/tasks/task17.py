def print_horizontal_line(size):
    print(" ---" * size)


def print_vertical_line(size):
    print("|   " * (size + 1))


if __name__ == "__main__":
    board_size = int(input("What size of game board? "))

    for index in range(board_size):
        print_horizontal_line(board_size)
        print_vertical_line(board_size)

    print_horizontal_line(board_size)
