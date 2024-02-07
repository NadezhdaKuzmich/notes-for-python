# ● Модуль (пакет) - це набір готових класів, функцій для вирішення певних
# завдань.

# ● Для того, щоб користуватися модулем, його потрібно імпортувати,
# використовуючи ключове слово import і вказати ім'я модуля module_name:
# import module_name
# Таким чином ви імпортуєте відразу весь модуль з усіма його класами та
# функціями.

# ● По суті, модуль - це папка, в якій можуть бути інші папки з файлами або
# файли.
# ● Якщо вам потрібно зробити кілька імпортів з одного модуля, ви можете
# просто перерахувати їх через кому:
# from my_module.functions import function_1, function_2, function_x

# ● Також у модулях підтримується alias (альтернативне ім'я). Наприклад:
# import my_long_module_name_module
# то ви можете скористатися або зробити ось так:
# import my_long_module_name_module as short_mod
# чи взагалі:
# import my_long_module_name_module as m
# і користуватися вже у коді вибраним вами ім'ям.

# Одні з найважливіших базових модулів:
# ● collections - модуль із розширеними структурами даних
# ● math - модуль готових математичних функцій
# ● random - модуль для генерації випадкових значень
# ● itertools - модуль із готовими функціями комбінаторики
# ● re - модуль підтримки регулярних виразів
# ● datetime - модуль дати та часу

# Custom method from package:
from my_module.hello import Test

p = Test()
p.hello()