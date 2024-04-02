import numpy

# NumPy - це розширення мови Python, що додає підтримку великих багатовимірних
# масивів і матриць, разом із великою бібліотекою високорівневих математичних
# функцій для операцій із цими масивами.

# task 1
# numpy.empty(shape, dtype=float, order='C')
# Функція empty() повертає новий масив заданої форми і типу без ініційованих
# записів:
firstArray = numpy.empty([4, 2], dtype=numpy.uint16)
print("Printing Array")
print(firstArray)

print("Printing numpy array Attributes")
# ndarray.shape - розміри масиву, його форма. Це кортеж натуральних чисел, що
# показує довжину масиву по кожній осі. Для матриці з n рядків і m стовпців,
# shape буде (n, m).
print("1> Array Shape is: ", firstArray.shape)

# ndarray.ndim - число осей (вимірів) масиву. Як уже було сказано, у світі
# Python число вимірів часто називають рангом. Кількість елементів кортежу
# shape дорівнює рангу масиву, тобто ndim.
print("2>. Array dimensions are ", firstArray.ndim)

# ndarray.itemsize - розмір кожного елемента масиву в байтах. Наприклад, для
# масиву з елементів типу float64 значення itemsize дорівнює 8 (=64/8), а для
# complex32 цей атрибут дорівнює 4 (=32/8).
print("3>. Length of each element of array in bytes is ", firstArray.itemsize)

# task 2
print("\nCreating 5X2 array using numpy.arange")
# numpy.arange(start, stop, step) - функція, яка повертає об'єкт типу ndarray,
# що містить рівномірно розташовані значення всередині заданого інтервалу.
# Наприклад, щоб згенерувати значення від 1 до 10, можна скористатися функцією
# numpy.arange(). Тут start - початок інтервалу, stop - кінець інтервалу,
# step - інтервал між значеннями (за замовчуванням дорівнює 1).
sampleArray = numpy.arange(100, 200, 10)
print(sampleArray)

# reshape() дає змогу змінювати форму масиву, тобто змінювати розміри елементів
# масиву. Зміна форми масиву допоможе змінити кількість значень, що знаходяться
# в певному вимірі. Важливо зазначити, що reshape зберігає розмір масиву, тобто
# не змінює кількість елементів масиву.
sampleArray = sampleArray.reshape(5, 2)
print(sampleArray)

# task 3
# Один із найпростіших - створити масив зі звичайних списків або кортежів,
# використовуючи функцію numpy.array(), що створює об'єкт типу ndarray:
sampleArray = numpy.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print("\nPrinting Input Array")
print(sampleArray)

print("\nPrinting array of items in the third column from all rows")
newArray = sampleArray[..., 2]
print(newArray)

# task 4
sampleArray = numpy.array([[3, 6, 9, 12], [15, 18, 21, 24],
                           [27, 30, 33, 36], [39, 42, 45, 48],
                           [51, 54, 57, 60]])
print("\nPrinting Input Array")
print(sampleArray)

print("\nPrinting array of odd rows and even columns")
newArray = sampleArray[::2, 1::2]
print(newArray)

# task 5
arrayOne = numpy.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = numpy.array([[15, 33, 24], [4, 7, 1]])

resultArray = arrayOne + arrayTwo
print("\nAddition of two arrays is:")
print(resultArray)

# Об'єкт ітератора nditer забезпечує багато гнучких способів відвідати всі
# елементи одного або декількох масивів систематичним способом.
for num in numpy.nditer(resultArray, op_flags=['readwrite']):
    num[...] = num * num
print("\nResult array after calculating the square root of all elements")
print(resultArray)

# task 6
print("\nCreating 8X3 array using numpy.arange")
sampleArray = numpy.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8, 3)
print(sampleArray)

print("\nDividing 8X3 array into 4 sub array\n")
subArrays = numpy.split(sampleArray, 4)
print(subArrays)

# task 7
print("\nPrinting Original array")
sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
arr = numpy.array([[10, 10, 10]])
print(sampleArray)

print("\nArray after deleting column 2 on axis 1")
# numpy.delete() повертає новий масив із підмасивами за видаленою віссю.
sampleArray = numpy.delete(sampleArray, 1, axis=1)
print(sampleArray)

print("\nArray after inserting column 2 on axis 1")
# numpy.insert(arr, obj, values, axis=None) вставляє значення або масив перед
# індексом (obj) уздовж осі.
sampleArray = numpy.insert(sampleArray, 1, arr, axis=1)
print(sampleArray)
