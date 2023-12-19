# Успадкування (англ. inheritance) — концепція об'єктно-орієнтованого програмування, згідно з якою абстрактний
# тип даних може успадковувати дані та функціональність деякого існуючого типу, сприяючи повторному використанню
# компонентів програмного забезпечення.
# ● Спадкування є простою ідеєю. Ви можете створити ієрархію класів, де є материнські (від яких успадковуються) та
# дочірні класи (які успадковуються від материнських).
# ● Ключова ідея успадкування така сама, як і в біології. Дочірні класи-спадкоємці “переймають” від материнських їхні
# атрибути та методи. Тобто вам не потрібно їх заново прописувати. Але який сенс успадкування того самого без змін?
# Ніякого. Якщо ви використовуєте успадкування, завжди повинні в дочірніх класах щось змінювати або додавати.

# Види наслідування:
# Просте
class Human:
    def __init__(self, age):
        self.age = age

    def say_hello(self):
        print(F"Hello, I am {self.age}")


human = Human(age=27)
human.say_hello()  # => Hello, I am 27


class HumanExtended(Human):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

    def say_hello(self):
        print(f"Hello, I am {self.name} and I am {self.age}")


human2 = HumanExtended(age=56, name='John')
human2.say_hello()  # => Hello, I am John and I am 56


# Множинне
class A:
    def __init__(self):
        self.a = 10


class B:
    def __init__(self):
        self.b = 5


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


c = C()
print(c.a)  # => 10
print(c.b)  # => 5


class Doctor:
    @staticmethod
    def can_cure():
        print('Я лікар, я вмію лікувати')

    def can_build(self):
        print('Я архітектор, я трохи вмію будувати')


class Architect:
    def can_build(self):
        print('Я архітектор, я вмію будувати')


class Person(Doctor, Architect):
    def can_build(self):
        print('Я людина, я теж вмію будувати')


person = Person()
person.can_cure()
person.can_build()
print(Person.__mro__)


class Car:
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume

    @staticmethod
    def drive_forward():
        print("Drive forward")

    @staticmethod
    def drive_backward():
        print("Drive backward")


class Car2(Car):
    @staticmethod
    def turn_left():
        print('Turn left')

    @staticmethod
    def turn_right():
        print('Turn right')


car = Car2('Audi', 'white', 3.5)
car.turn_left()
car.drive_backward()
car.turn_right()
car.drive_forward()


class Airplane:
    def __init__(self, model):
        self.airplane_model = model

    @staticmethod
    def up():
        print("Going up")

    @staticmethod
    def land():
        print("Landing")


class FlyingCar(Car2, Airplane):
    def __init__(self, brand, color, volume, model):
        Car2.__init__(self, brand, color, volume)
        Airplane.__init__(self, model)


fc = FlyingCar(brand='Tesla', color='Black', volume=10, model='F')
fc.up()
fc.drive_forward()
fc.turn_left()
fc.drive_backward()
fc.land()
