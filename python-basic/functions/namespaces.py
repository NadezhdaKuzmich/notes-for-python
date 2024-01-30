# Namespaces - простір імен. Існують для запобігання з пошуком імен
def print_local_y():
    y = 'local'
    print(y)


y = 'global'
print_local_y()
print(y)


def print_namespace():  # імʼя фунції також записується у простір імен
    """ Простір імен це словник з іменами та значеннями.
    Разом з визначенням простору імен пайтон визначає і область видимості. """
    print(1, locals())
    date_founding_kiev = 482
    print(2, locals())
    age = 2023 - 482
    print(3, locals())
    # print(globals())


x = 1
print_namespace()


# print(locals())

# Область видимості це ланцюжок просторів імен, який починається від
# локального і триває до глобального чи вбудованого. Область видимості
# визначає те, в якому просторі імен Пайтон шукатиме визначення конкретного
# імені конкретної змінної та в якому порядку цеї пошук буде здійснюватись.
# Для пошуку є аривіатура LEGB.


# Вкладені функції
def external():
    """LEGB enclosed"""
    a = 1

    def internal():
        return a

    return internal()


print(external())
# internal()


def changing_product():
    product = 'Milk'  # locals relates to changing_products and enclosed for
    # showing_enclosed
    print('Local: ', product)

    def showing_enclosed():
        # nonlocal product  # я буду змінювати вкладений простір імен
        global product
        print('Inside showing enclosed', product)
        product = 'Cola'
        print('Enclosed scope: ', product)

    showing_enclosed()
    print(product, '----')


product = 'bread'  # Global variables
changing_product()
print('Global:', product)
