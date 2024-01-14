import sqlite3
from collections import OrderedDict


class ObjectDoesNotExist(Exception):
    pass


class Storage:
    # визначаємо шалони SQL коду
    __SELECT_PATTER = 'SELECT * FROM {table_name} WHERE {fields}'
    __DELETE_PATTER = 'DELETE FROM {table_name} WHERE {fields}'
    __INSERT_PATTER = 'INSERT INTO {table_name} ({fields}) ' \
                      'VALUES({values})'
    _connection = None

    def __init__(self, cls):
        # зберігаємо клас, з яким пов'язане сховище
        self.cls = cls

    @classmethod
    def bind_connection(cls, connection):
        # прив'язка з'єднання з базою даних до сховища
        cls._connection = connection

    def get_by_field(self, single=False, **kwargs):
        values = list(kwargs.values())
        # форматуємо ключі та значення зі словника до набору рядків для запиту
        # WHERE (приклад: field1 = 1 AND field2 = 30)
        params = [
            '{field} = ?'.format(field=field)
            for field in kwargs.keys()
        ]
        # збираємо рядки в загальний запит, склеюючи їх роздільником `AND`
        fields_part = ' AND '.join(params)
        # складання запиту WHERE у шаблон SELECT
        sql_row = self.__SELECT_PATTER.format(
            table_name=self.cls._metadata._table_name,
            fields=fields_part
        )
        # якщо потрібен один об'єкт, то викликаємо SQL і перевіряємо його наявність
        # якщо об'єкт не знайдено, генеруємо виняток
        if single:
            row = self.execute_sql(sql_row, values).fetchone()
            if row is None:
                raise ObjectDoesNotExist(
                    'Object does not exist: {name} ({fields})'.format(
                        name=self.cls, fields=list(kwargs.items())
                    )
                )
            else:
                return self.cls(**dict(row))
        # Якщо об'єктів кілька, то збираємо їх по черзі і
        # повертаємо список зі словників
        result = []
        for row in self.execute_sql(sql_row, values).fetchall():
            result.append(self.cls(**dict(row)))
        return result

    def insert(self, **values):
        # збираємо назви полів зі словника
        fields = ', '.join(values.keys())
        values = list(values.values())
        # збираємо шаблон виду `?,?,?` для SQL з параметрами
        values_ = ', '.join(map(lambda x: '?', values))
        # збираємо загальний шаблон INSERT
        sql_row = self.__INSERT_PATTER.format(
            table_name=self.cls._metadata._table_name,
            fields=fields,
            values=values_
        )
        # виконуємо SQL та повертаємо створений об'єкт
        cursor = self.execute_sql(sql_row, values)
        instance = self.get_by_field(id=cursor.lastrowid)[0]
        return instance

    def delete(self, **fields):
        # збираємо значення та параметри для WHERE
        values = list(fields.values())
        params = [
            '{field} = ?'.format(field=field)
            for field in fields.keys()
        ]
        fields_part = ' AND '.join(params)
        # збираємо загальний шаблон DELETE та виконуємо SQL
        sql_raw = self.__DELETE_PATTER.format(
            table_name=self.cls._metadata._table_name,
            fields=fields_part
        )
        return self.execute_sql(sql_raw, values).rowcount

    @classmethod
    def execute_sql(cls, sql_text, params=None):
        params = params or ()
        print('SQL: {sql_text} with params: {params}'.format(
            sql_text=sql_text, params=params
        ))
        return cls._connection.execute(sql_text, params)


class Metadata(object):

    def __init__(self, fields, cls):
        self._fields = fields
        # формуємо назву SQL таблиці на основі імені класу в Python
        table_name = cls.__name__.lower()
        # Закінчення назви таблиці (як правило-це множина)
        # якщо закінчення `y` - `ies`, в інших `s`.
        # `class Student` -> `students`
        # `class City` -> `cities`
        if table_name.endswith('y'):
            table_name = cls.__name__.lower()[:-1]
            suffix = 'ies'
        else:
            table_name = cls.__name__.lower()
            suffix = 's'
        # зберігаємо назву таблиці
        self._table_name = '{old_name}{suffix}'.format(old_name=table_name,
                                                       suffix=suffix)

    def get_fields(self):
        return self._fields.items()

    def get_field(self, field_name):
        # повертаємо назву та тип на SQL:
        # age = Field('INTEGER') => SQL: age INTEGER
        result = '{field_name} {field_type}'.format(
            field_name=field_name, field_type=self._fields[field_name].type
        )
        return result

    def has_field(self, field_name):
        return field_name in self._fields

    def generate_create_table_sql(self):
        """
        Генеруємо SQL-код для створення таблиці, використовуючи описані
        `get_field` метод та назва таблиці з self._table_name`.
        """
        fields_data = ', '.join([
            self.get_field(field)
            for field in self._fields.keys()
        ])
        sql = 'CREATE TABLE {table_name} ({fields})'
        return sql.format(table_name=self._table_name, fields=fields_data)


class Field(object):
    """
    Проста абстракція над полем.
    """

    def __init__(self, field_type, default=None):
        self.type = field_type
        self.default = default


class BaseMeta(type):

    # @classmethod
    # def __prepare__(mcs, name, bases, **kwargs):
    #     print('Prepared', name, bases, kwargs)
    #     return OrderedDict()

    @staticmethod
    def __new__(mcs, name, bases, attrs):
        print('mcs', mcs)
        new_attrs = OrderedDict()
        fields = OrderedDict()
        # якщо в атрибутах є Field, ми їх збираємо в окремий словник
        # `fields` і прокидаємо в metadata.
        for key, value in attrs.items():
            # умова для Field
            if isinstance(value, Field):
                fields.setdefault(key, value)
            else:
                new_attrs[key] = value
        print(fields)
        # викликаємо базову поведінку, але без fields
        new_cls = super().__new__(mcs, name, bases, new_attrs)
        # доповнюємо клас екземпляром Storage, передаючи в Storage створений
        # клас для таблиці
        new_cls.storage = Storage(new_cls)
        # доповнюємо клас метаданими, використовуючи екземпляр класу `Metadata`
        # в нього ми прокидаємо поля та клас таблиці
        new_cls._metadata = Metadata(fields=fields, cls=new_cls)
        return new_cls


# використовуємо створений метаклас
class BaseModel(metaclass=BaseMeta):

    def __init__(self, **kwargs):

        # передані в конструктор значення перевіряємо на наявність
        # полів у fields, якщо передали щось зайве, то видаємо помилку
        for item in kwargs:
            assert self._metadata.has_field(item), \
                'Field "{}" does not exist'.format(item)
            setattr(self, item, kwargs.get(item))
            # self.age = 10
            # self.first_name = "Dmitry"

        # прив'язка значень за замовчуванням, якщо якесь із полів не
        # передали до конструктора
        for item in self._metadata._fields:
            if not hasattr(self, item):
                value = self._metadata._fields[item].default
                # якщо значення за замовчуванням функція, то викликаємо її
                # і беремо результат. Приклад: value = datetime.datetime.now()
                if callable(value):
                    value = value()
                setattr(self, item, value)


class User(BaseModel):
    # трохи SQL
    id = Field('INTEGER PRIMARY KEY AUTOINCREMENT')
    age = Field('INTEGER')
    first_name = Field('VARCHAR(30)', default='')
    last_name = Field('VARCHAR(30)', default='')


class Country(BaseModel):
    name = Field('VARCHAR(30)')


# preparing
DATABASE = ':memory:'
connection = sqlite3.connect(DATABASE)
connection.row_factory = sqlite3.Row

# прив'язка з'єднання до Storage.
Storage.bind_connection(connection)
# створення таблиць - перша ініціалізація.
# Оскільки сховище :memory:, то таблиці повинні створюватися при кожному запуску.
# Враховуємо, що при використанні файлу на диску створення таблиць буде
# запускатися тільки один раз.
Storage.execute_sql(User._metadata.generate_create_table_sql())
Storage.execute_sql(Country._metadata.generate_create_table_sql())

# executing select/insert/delete
user = User.storage.insert(
    first_name='John',
    last_name='Test',
    age=10
)
print('ID', user.id)

user = User.storage.insert(
    first_name='John',
    last_name='Test',
    age=10
)
print('ID', user.id)

print(User.storage.get_by_field(first_name='John'))
print(User.storage.delete(first_name='John'))
print(User.storage.get_by_field(first_name='John'))

try:
    print(User.storage.get_by_field(first_name='John', single=True))
except ObjectDoesNotExist as e:
    print(e)
