
import json
import os

FILE = "library.json"

# Load books from file
def load_books():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save books to file
def save_books():
    with open(FILE, "w") as f:
        json.dump(books, f, indent=4)

books = load_books()

# Add new book
def add_book():
    book_id = input("Enter Book ID: ")

    if any(book["id"] == book_id for book in books):
        print("Book ID already exists!")
        return

    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "name": name,
        "author": author,
        "issued_to": None
    }

    books.append(book)
    save_books()
    print("Book Added Successfully!")

# Display all books
def display_books():
    if not books:
        print("No books available.")
        return

    for book in books:
        status = "Issued" if book["issued_to"] else "Available"

        print("\nBook ID:", book["id"])
        print("Book Name:", book["name"])
        print("Author:", book["author"])
        print("Status:", status)

# Search book
def search_book():
    name = input("Enter book name to search: ").lower()

    found = False

    for book in books:
        if name in book["name"].lower():
            print(book)
            found = True

    if not found:
        print("Book Not Found!")

# Issue book
def issue_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["issued_to"] is None:
                student = input("Enter Student Name: ")
                book["issued_to"] = student
                save_books()
                print("Book Issued Successfully!")
            else:
                print("Book Already Issued!")
            return

    print("Book Not Found!")

# Return book
def return_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["issued_to"] is not None:
                book["issued_to"] = None
                save_books()
                print("Book Returned Successfully!")
            else:
                print("Book is not issued.")
            return

    print("Book Not Found!")

# Delete book
def delete_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["issued_to"] is not None:
                print("Return the book before deleting it.")
                return

            books.remove(book)
            save_books()
            print("Book Deleted Successfully!")
            return

    print("Book Not Found!")

# Main menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Try Again.")
