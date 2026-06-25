import json

FILE_NAME = "books.json"

import json

FILE_NAME = "books.json"


# Load data
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"books": []}


# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Add book
def add_book():
    data = load_data()

    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "title": title,
        "author": author,
        "available": True
    }

    data["books"].append(book)

    save_data(data)

    print("Book added successfully.")


# View books
def view_books():
    
    data = load_data()

    if len(data["books"]) == 0:
        print("No books found.")
        return

    print("\n----- BOOKS -----")

    for index, book in enumerate(data["books"], start=1):

        status = "Available"

        if not book["available"]:
            status = "Borrowed"

        print(
            f"{index}. "
            f"Title: {book['title']} | "
            f"Author: {book['author']} | "
            f"Status: {status}"
        )


# Search book
def search_book():
    
    data = load_data()

    title = input("Enter book title: ")

    found = False

    for book in data["books"]:

        if book["title"].lower() == title.lower():

            status = "Available"

            if not book["available"]:
                status = "Borrowed"

            print(
                f"Title: {book['title']} | "
                f"Author: {book['author']} | "
                f"Status: {status}"
            )

            found = True

    if not found:
        print("Book not found.")


# Borrow book
def borrow_book():
    
    data = load_data()

    title = input("Enter book title to borrow: ")

    for book in data["books"]:

        if book["title"].lower() == title.lower():

            if book["available"]:

                book["available"] = False

                save_data(data)

                print("Book borrowed successfully.")

            else:

                print("Book is already borrowed.")

            return

    print("Book not found.")


# Return book
def return_book():
    
    data = load_data()

    title = input("Enter book title to return: ")

    for book in data["books"]:

        if book["title"].lower() == title.lower():

            if not book["available"]:

                book["available"] = True

                save_data(data)

                print("Book returned successfully.")

            else:

                print("Book is already available.")

            return

    print("Book not found.")


# Delete book
def delete_book():
    
    data = load_data()

    if not data["books"]:
        print("No books found.")
        return

    print("\n----- BOOKS -----")

    for index, book in enumerate(data["books"], start=1):
        print(f"{index}. {book['title']}")

    choice = int(input("Enter book number to delete: "))

    if 1 <= choice <= len(data["books"]):

        deleted_book = data["books"].pop(choice - 1)

        save_data(data)

        print(f"Deleted: {deleted_book['title']}")

    else:
        print("Invalid book number.")


# Menu
def menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            borrow_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            delete_book()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


menu()