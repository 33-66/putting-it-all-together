#!/usr/bin/env python3


class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def get_page(self):
      return  self._page_count

    def set_page(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_page, set_page)

    pass


book = Book("today", "272")
print(book.title == "today")
print(book.title)
print(book.turn_page())