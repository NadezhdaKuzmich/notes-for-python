from operator import neg, mul, le
from functools import reduce, partial

# Модуль operator містить функції, які відповідають стандартним операторам.
# Таким чином, замість lambda x, y: x + y можна використовувати вже готову
# функцію operator.add

# Функція модуля operator               Аналогічна лямбда-функція
# add                                      lambda x, y: x + y
# gt                                       lambda x, y: x > y
# neg                                         lambda x: -x

# Зробити числа списку від'ємними
print(list(map(neg, [2, 4, 8, 9, 1])))

# Обчислити добуток елементів списку
print(reduce(mul, [3, 4, 5]))

# Залишити тільки числа, більші або рівні п'яти (використовується оператор <=,
# оскільки як за допомогою функції partial застосовується перший аргумент,
# тобто умова виглядає як 5 <= x).
print(list(filter(partial(le, 5), [5, 4, 8, 1, 3, 10])))
