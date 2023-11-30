
from lib.book import * 

""" Book constructs with an id, title, author_name"""

def test_book_construct():
    book = Book(1, "test_title", "test_author_name")
    assert book.id == 1
    assert book.title == "test_title"
    assert book.author_name == "test_author_name"

""" We can format books to strings nicely"""

def test_book_format_nicely():
    book = Book(1, "test_title", "test_author_name")
    assert str(book) == "Book(1, test_title, test_author_name)"


def test_book_are_equal():
    book1 = Book(1, "test_title", "test_author_name")
    book2 = Book(1, "test_title", "test_author_name")
    assert book1 == book2



