def read_books_data(file_path):
    books = []
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.replace("\n", "")
            parts = line.split(",")

            books.append(parts)
            
        return books

    except FileNotFoundError:
        print("File not found!")
        return []


def display_books(books):
    print("\n----- LIBRARY BOOK LIST -----")
    print("ID | Title | Author | Year | Count")
    print("-----------------------------------")

    for b in books:
        try:
            print(b[0] + " | " + b[1] + " | " + b[2] + " | " + b[3] + " | " + b[4])
        except:
            continue
