import unittest
from unittest import mock

from Week6B.book import Book


class BookTestSuite(unittest.TestCase):
    def test_init_correctParameters_setAllNecessaryAttributes(self):
        b = Book("132350882", "Clean Code", "Robert C. Martin")
        self.assertEqual(b.isbn, "132350882", "-0.25: ISBN is not set!")
        self.assertEqual(b.title, "Clean Code", "-0.25: title is not set!")
        self.assertEqual(b.author, "Robert C. Martin", "-0.25: author is not set!")
        self.assertIsNone(b.price, "-0.25: price is not set!")

    def test_set_price_10_setThePriceTo10(self):
        b = Book("132350882", "Clean Code", "Robert C. Martin")
        expected_price = 10
        b.set_price(expected_price)
        self.assertEqual(expected_price, b.price)

    def test_open_noArgs_printCorrectText(self):
        title = "Clean Code"
        author = "Robert C. Martin"
        b = Book("132350882", title, author)
        print_mock = mock.MagicMock()

        with mock.patch("builtins.print", print_mock):
            b.open()

        print_mock.assert_called_with("The {} written by {} is opened.".format(title, author))


if __name__ == '__main__':
    unittest.main()
