import datetime
import unittest
import unittest.mock


def sum_two_values(a, b):
    return a + b


def power(x, n):
    return x ** n


def concat_values(*args):
    result = ''
    for item in args:
        result += str(item)
    return result


def desc(x, y):
    if x == 0:
        raise ValueError('`x` should not be equal 0')
    return y / x


class User:
    def test_method(self):
        raise NotImplementedError


class UserTestCase(unittest.TestCase):

    @unittest.mock.patch('mocks.sum_two_values')
    def test_sum_two_values_uncalled(self, mocked_sum):
        # функція нами не викликалася, а значить called буде False
        self.assertFalse(mocked_sum.called)

    @unittest.mock.patch('mocks.sum_two_values')
    def test_sum_two_values_called(self, mocked_sum):
        sum_two_values(10, 20)
        # функція нами викликалася, а значить called буде True
        # тіло функції не виконувалося, оскільки ми зробили `mock.patch`.
        self.assertTrue(mocked_sum.called)

    @unittest.mock.patch('mocks.sum_two_values')
    def test_sum_two_values_called_with(self, mocked_sum):
        sum_two_values(10, 20)
        self.assertTrue(mocked_sum.called)
        # Тіло функції виконувалося один раз, перевіримо це
        self.assertEqual(mocked_sum.call_count, 1)
        # перевіримо з якими аргументами викликалася функція
        mocked_sum.assert_called_with(10, 20)

    @unittest.mock.patch('mocks.sum_two_values')
    def test_reset_mock(self, mocked_sum):
        sum_two_values(10, 20)
        sum_two_values(10, 20)
        self.assertTrue(mocked_sum.called)
        self.assertEqual(mocked_sum.call_count, 2)
        # перевіримо чи викликалася функція використовуючи інший спосіб
        mocked_sum.assert_called()
        mocked_sum.assert_called_with(10, 20)

        # скинемо лічильник викликів, після чого функція буде обнулена та
        # всі попередні виклики як би забуті
        mocked_sum.reset_mock()

        self.assertEqual(mocked_sum.call_count, 0)
        self.assertFalse(mocked_sum.called)
        mocked_sum.assert_not_called()

    @unittest.mock.patch('mocks.sum_two_values')
    def test_mock_call(self, mocked_sum):
        sum_two_values(10, 40)
        sum_two_values(20, 50)
        sum_two_values(30, 60)
        # чи був хоча б один виклик функції з такими аргументами
        mocked_sum.assert_any_call(10, 40)

    @unittest.mock.patch('mocks.sum_two_values')
    def test_mock_call_with(self, mocked_sum):
        sum_two_values(10, 40)
        mocked_sum.assert_called_with(10, 40)

        sum_two_values(20, 50)
        mocked_sum.assert_called_with(20, 50)

        sum_two_values(30, 60)
        mocked_sum.assert_any_call(30, 60)

    # Підмінимо значення, що повертається на число 20
    @unittest.mock.patch('mocks.sum_two_values', return_value=20)
    def test_mock_return_value_in_dec(self, mocked_sum):
        result1 = sum_two_values(10, 40)
        result2 = sum_two_values(110, 140)
        result3 = sum_two_values(1110, 1140)
        self.assertEqual(result1, 20)
        self.assertEqual(result2, 20)
        self.assertEqual(result3, 20)

    @unittest.mock.patch('mocks.sum_two_values')
    def test_mock_return_value_in_body(self, mocked_sum):
        # Замінимо значення, що повертається на число 20 використовуючи ще один спосіб
        mocked_sum.return_value = 20

        result1 = sum_two_values(10, 40)
        result2 = sum_two_values(110, 140)
        result3 = sum_two_values(1110, 1140)
        self.assertEqual(result1, 20)
        self.assertEqual(result2, 20)
        self.assertEqual(result3, 20)

    @unittest.mock.patch('mocks.sum_two_values')
    def test_mock_side_effect(self, mocked_sum):
        result = 0

        def res_func(x, y):
            return result

        # за викликом нашої функції ми хочемо виконати сторонній код,
        # який опишемо в тесті. Як правило це називається side effect
        mocked_sum.side_effect = res_func

        self.assertEqual(sum_two_values(110, 140), result)
        self.assertEqual(sum_two_values(10, 0), result)
        self.assertEqual(sum_two_values(300, 400), result)

        # ми також можемо присвоїти екземпляр виняток, щоб він був
        # викинутий в момент виклику
        raise_text = 'Test exception'
        mocked_sum.side_effect = ValueError(raise_text)
        with self.assertRaises(ValueError):
            sum_two_values(10, 30)

        # список винятків для послідовного виклику
        mocked_sum.side_effect = ValueError, RuntimeError, ZeroDivisionError

        with self.assertRaises(ValueError):
            sum_two_values(10, 30)
        with self.assertRaises(RuntimeError):
            sum_two_values(10, 30)
        with self.assertRaises(ZeroDivisionError):
            sum_two_values(10, 30)

        # якщо ми хочемо додати side effect разом з значенням, що повертається,
        # яке також хочемо задати, використовуємо `return mock.DEFAULT`
        def res_func2(x, y):
            print('Hey')
            return unittest.mock.DEFAULT

        mocked_sum.return_value = 300
        mocked_sum.side_effect = res_func2
        self.assertEqual(sum_two_values(1, 2), 300)

    def test_mock_return_value_in_body_with(self):
        # використання патчингу у зв'язці з оператором with
        with unittest.mock.patch('mocks.sum_two_values') as mocked_sum:
            mocked_sum.return_value = 20
            result1 = sum_two_values(10, 40)
            result2 = sum_two_values(110, 140)
            result3 = sum_two_values(1110, 1140)
            self.assertEqual(result1, 20)
            self.assertEqual(result2, 20)
            self.assertEqual(result3, 20)

    def test_mock_builtin(self):
        with unittest.mock.patch('datetime.datetime') as mocked_datetime:
            actual_date = datetime.datetime(2019, 1, 1, 23, 8, 6)

            mocked_datetime.now.return_value = actual_date
            result1 = datetime.datetime.now()
            self.assertEqual(result1, actual_date)

    # ми можемо патчити навіть методи у класів, використовуючи `mock.patch..object`
    @unittest.mock.patch.object(User, 'test_method')
    def test_user(self, mock_method):
        mock_method.return_value = 10
        user = User()
        # викликаємо метод та перевіряємо наш mock
        user.test_method()
        self.assertTrue(mock_method.called)
        mock_method.assert_called_once()
