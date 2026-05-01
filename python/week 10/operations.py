def update_books_count(books):
    try:
        book_id = int(input("Enter Book ID (number): "))
        new_count = int(input("Enter new count (number): "))

        found =False

        for b in books:
            if int(b[0]) == book_id:
                b[4] = str(new_count)
                print("Book updated successfully!")
                found = True
                break

        if not found:
            print("Error: Book ID not found!")

    except ValueError:
        print("Error: Invalid input! Please enter numbers only for Book ID and count.")

    return books
