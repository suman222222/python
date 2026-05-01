def write_books_data(file_path, books):
    try:
        with open(file_path, "w") as file:
            for b in books:
                line = b[0] + "," + b[1] + "," + b[2] + "," + b[3] + "," + b[4] + "\n"
            file.write(line)

        print("Data written to file successfully!")

    except :
        print("Error while writing file!")
