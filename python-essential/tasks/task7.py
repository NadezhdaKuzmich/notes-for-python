def average(*numbers):
    return sum(numbers) / len(numbers)


def main():
    print(average(2, 4, 6))
    print(average(*range(20)))


if __name__ == '__main__':
    main()
