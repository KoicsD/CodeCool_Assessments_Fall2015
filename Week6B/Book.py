__author__ = 'KoicsD'


class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = None

    def set_price(self, price):
        self.price = price

    def open(self):
        print("The %s written by %s is opened." % (self.title, self.author))
