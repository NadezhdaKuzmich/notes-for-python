# Об'єктно-орієнтоване програмування (ООП):
# Поняття ООП — методологія програмування, заснована на представленні програми у вигляді сукупності об'єктів,
# кожен із яких є екземпляром певного класу, а класи утворюють ієрархію спадкування.
# Ключовими поняттями в ООП є клас та об'єкт класу. Клас - загальне поняття (рослина, предмет меблів), а об'єкт чи
# об'єкт класу - це вже конкретне поняття (кульбаба (рослина), стілець (предмет меблів)). Ця концепція є основою ООП.
# ООП будується на 4 основних принципах: успадкування, інкапсуляція, поліморфізм та абстракція.
class Human:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age_and_name(self):
        return self.get_name(), self.age


human_1 = Human(age=25, name='John', gender='male')
print(human_1.age)  # => 25
print(human_1.get_name())  # => John
print(human_1.get_age_and_name())  # => ('John', 25)
