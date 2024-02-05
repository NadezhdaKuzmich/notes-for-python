# Рекурсія - коли функція викликає саму себе (проста рекурсія) або коли вона
# викликає саму себе через іншу функцію (непряма рекурсія).
# Два найважливіші моменти в рекурсії: зміна стану та умова виходу.
# Якщо першої умови не дотримано, код втрачає логіку, якщо друга умова не
# дотримана, то буде переповнення стека та помилка.

# def iter_arr(array):
#     for elem in array:
#         print(elem)


def iter_rec(array, index=0):
    if index < len(array):
        print(array[index])
        index += 1
        iter_rec(array, index)


a = [4, 5, 1, 3, 2]
# iter_arr(a)
iter_rec(a)


# Рекурсія має свої переваги та недоліки. Перевагою є швидкість виконання
# програми. Рекурсія набагато швидше за цикли. Однак із недоліків можна
# виділити складність її розуміння (зрозуміти рекурсію складніше ніж
# зрозуміти цикли), а з технічного боку рекурсія має ліміт викликів. У
# Python він дорівнює 1000.

# def rec_counter(index):
#     print(index)
#     index += 1
#     rec_counter(index)


# => RecursionError: maximum recursion depth exceeded
# rec_counter(1)  # => 1 - 999


# Структура даних дерево - добрий приклад того, навіщо потрібна рекурсія.
# Бінарне дерево - це ієрархічна структура даних, в якій кожен вузол має
# значення (воно ж є в даному випадку і ключем) та посилання на лівого та
# правого нащадка. Вузол, що знаходиться на самому верхньому рівні (який не
# є чиїмось нащадком) називається коренем. Вузли, які мають нащадків ( обидва
# нащадка яких рівні NULL) називаються листям.

# Бінарне дерево на Python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, data):
        if data == self.data:
            print(f"{data} in tree")
            return True
        if data < self.data:
            if self.left is None:
                print(f"{data} not in tree")
                return False
            return self.left.search(data)
        if self.right is None:
            print(f"{data} not in tree")
            return False
        return self.right.search(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


a = [4, 5, 1, 3, 2, 6, 0]
for i in range(len(a)):
    if i == 0:
        root = Node(a[i])
    else:
        root.insert(a[i])

root.search(2)
root.search(9)
root.print_tree()


def values(n, current=1):
    if current <= n:
        print(current)
        values(current=current + 1, n=n)


# values(20)

def check_pow(n):
    if n == 1:
        print("YES")
    else:
        if n % 2 == 0:
            check_pow(n // 2)
        else:
            print("NO")


check_pow(16)


def sum_val(num, res=0):
    if not num:
        return res
    res += num % 10
    num //= 10
    return sum_val(num, res)


print(sum_val(345))
