import copy

# Завдання 1
# Створіть клас, який описує книгу. Він повинен містити інформацію про автора,
# назву, рік видання та жанр. Створіть кілька книг. Визначте
# йому операції перевірки на рівність і нерівність, методи __repr__ і __str__.
# Створіть клас, який описує відгук до книги. Додайте до класу книги
# поле – перелік відгуків. Зробіть так, що при виведенні книги на екран
# за допомогою функції print також виводитимуться відгуки до неї.
class Book:
    def __init__(self, author, title, publication_year, genre, comments=None):
        if comments is None:
            comments = []
        self.author = author
        self.title = title
        self.publication_year = publication_year
        self.genre = genre
        self.comments = comments

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.author == other.author and \
            self.title == other.title and \
            self.publication_year == other.publication_year and \
            self.genre == other.genre

    def __as_string(self, format_string):
        return format_string.format(
            self.author,
            self.title,
            self.publication_year,
            self.genre,
            self.comments
        )

    def __str__(self):
        book = self.__as_string('"{}" by {} (published in {}, genre: {})'
                                '\nComments:\n')
        comments = '\n'.join(map(str, self.comments)) or 'No comments.'
        return book + comments

    def __repr__(self):
        return self.__as_string("Book({!r}, {!r}, {!r}, {!r}, {!r})")


class Comment:
    def __init__(self, mark, text):
        self.mark = mark
        self.text = text

    def __str__(self):
        return 'Mark: {}\nReview: {}'.format(self.mark, self.text)

    def __repr__(self):
        return 'Comment({!r}, {!r})'.format(self.mark, self.text)


def main():
    orwell1984 = Book('George Orwell', '1984', 1949, 'dystopia')
    orwell_copy = copy.copy(orwell1984)
    learning_python = Book('Mark Lutz', 'Learning Python', 2013, 'tutorial')

    orwell1984.comments = [
        Comment(5, 'Awesome book, changed my perception of the life'),
        Comment(4,
                "Not bad, but Huxley's scenario seems more realistic to me"),
    ]

    print(orwell1984)
    print()
    print(learning_python)
    print()

    print(repr(orwell1984))
    print()
    print(repr(learning_python))
    print()

    print(orwell1984 == orwell_copy)
    print(orwell1984 != orwell_copy)
    print(orwell1984 == learning_python)
    print(orwell1984 != learning_python)
    print(learning_python == learning_python)
    print(learning_python != learning_python)


if __name__ == '__main__':
    main()
