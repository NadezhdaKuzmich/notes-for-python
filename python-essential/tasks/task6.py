# __iter__(self) - отримання ітератора для перебору об'єкта;
# __next__(self) - перехід до наступного значення і його зчитування.
class Reversed:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        # To prevent the iteration from going on forever, we can use the
        # StopIteration statement.
        value = self.sequence[self.index]
        self.index -= 1
        return value


def my_reversed(sequence):
    index = len(sequence) - 1

    while index >= 0:
        yield sequence[index]
        index -= 1


def main():
    my_list = [1, 2, 3, 4, 5]
    for i in Reversed(my_list):
        print(i)
    print()

    for i in my_reversed(my_list):
        print(i)


if __name__ == '__main__':
    main()
