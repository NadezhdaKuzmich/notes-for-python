def my_reversed(sequence):
    index = len(sequence) - 1

    while index >= 0:
        yield sequence[index]
        index -= 1


def main():
    my_list = [1, 2, 3, 4, 5]
    for i in my_reversed(my_list):
        print(i)


if __name__ == '__main__':
    main()
