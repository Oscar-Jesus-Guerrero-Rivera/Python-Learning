"""
You've been tasked with writing the code for the wizard library. 
Complete the Library and Book classes listed below.

Book Class

__init__(self, title, author)
Set .title and .author to the values of the parameters.

Library Class

__init__(self, name)
Initialize a .name member variable to the value of the name parameter. 
Create a .books member initialized to an empty list.

add_book(self, book)
Add book, a Book instance, to the books instance variable by appending it to the end of the list.

remove_book(self, book)
If the book's title and author match a library book's title and author, 
the remove_book method should remove that library book from the list.

search_books(self, search_string)
For every book in the library check if the search_string is contained in the title or author field (case-insensitive). Return a list of all books that match the search string, ordered in the same order as they were added to the library.
After a book is removed, it should no longer be returned in the search results.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books = [
            b for b in self.books if not (b.title == book.title and b.author == book.author)
        ]

    def search_books(self, search_string):
       
        search_string = search_string.lower()  
        return [
            book for book in self.books
            if search_string in book.title.lower() or search_string in book.author.lower()
        ]
    

# Test

run_cases = [
    (
        "Jane's Library",
        ["The Trial"],
        ["Franz Kafka"],
        Book("The Trial", "Franz Kafka"),
        "Kafka",
        [],
    ),
    (
        "John's Library",
        ["The Catcher in the Rye", "To Kill a Mockingbird", "1984"],
        ["J.D. Salinger", "Harper Lee", "George Orwell"],
        Book("1984", "George Orwell"),
        "kill",
        ["To Kill a Mockingbird"],
    ),
]

submit_cases = run_cases + [
    (
        "Lane's Library",
        [
            "The Great Gatsby",
            "Pride and Prejudice",
            "The Lord of the Rings",
            "Great Expectations",
            "To Kill a Mockingbird",
        ],
        [
            "F. Scott Fitzgerald",
            "Jane Austen",
            "J.R.R. Tolkien",
            "Charles Dickens",
            "Harper Lee",
        ],
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        "great",
        ["Great Expectations"],
    ),
]


def test(
    library_name,
    book_titles,
    book_authors,
    book_to_remove,
    search_query,
    expected_search_results,
):
    print("---------------------------------")
    try:
        print(f"Testing Library: {library_name}")

        library = Library(library_name)
        for title, author in zip(book_titles, book_authors):
            library.add_book(Book(title, author))
            print(f"Adding book {title} by {author}")

        print(f"Removing book {book_to_remove.title} by {book_to_remove.author}")
        library.remove_book(book_to_remove)

        print(f"Searching for '{search_query}'")
        search_results = library.search_books(search_query)
        results_titles = [book.title for book in search_results]
        print(f"Expected: {expected_search_results}")
        print(f"Actual: {results_titles}")

        if results_titles != expected_search_results:
            print("Fail")
            return False

        print("Pass")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed, failed = 0, 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
