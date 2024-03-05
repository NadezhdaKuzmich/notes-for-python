import random


def generate_data():
    for _ in range(100):
        yield random.random()


def write_data(data, filename):
    with open(filename, 'w') as file:
        for number in data:
            print(number, file=file)


def count_sum(filename):
    sum_ = 0
    with open(filename, 'r') as file:
        for line in file:
            sum_ += float(line)
    return sum_


if __name__ == '__main__':
    path = 'data/data.txt'
    gen_data = generate_data()
    write_data(gen_data, path)

    result = count_sum(path)
    print('Sum =', result)
