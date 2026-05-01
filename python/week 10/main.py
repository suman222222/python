from read import read_books_data, display_books
from operations import update_books_count
from write import write_books_data


def main():
    file_path = "books.txt"

    books = read_books_data(file_path)

    display_books(books)

    books = update_books_count(books)

    display_books(books)

    write_books_data(file_path, books)

main()
