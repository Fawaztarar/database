from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    # Selecting all records
    # No arguments
    def all(self):
        # Executes the SQL query:
        # SELECT * FROM books;

        # Returns an array of Book objects.
        books = []
        rows = self._connection.execute("SELECT * FROM books")
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books
