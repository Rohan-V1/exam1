import sqlite3

class Library:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            year INTEGER NOT NULL
                            )''')
        self.conn.commit()

    def add_book(self, title, author, year):
        self.cursor.execute('''INSERT INTO books (title, author, year) 
                            VALUES (?, ?, ?)''', (title, author, year))
        self.conn.commit()
        print("Book added successfully.")

    def remove_book(self, book_id):
        self.cursor.execute('''DELETE FROM books WHERE id = ?''', (book_id,))
        self.conn.commit()
        print("Book removed successfully.")

    def update_book(self, book_id, title, author, year):
        self.cursor.execute('''UPDATE books SET title = ?, author = ?, year = ? 
                            WHERE id = ?''', (title, author, year, book_id))
        self.conn.commit()
        print("Book updated successfully.")

    def display_books(self):
        self.cursor.execute('''SELECT * FROM books''')
        books = self.cursor.fetchall()
        if books:
            print("Library Books:")
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")
        else:
            print("Library is empty.")

    def __del__(self):
        self.conn.close()


def main():
    library = Library('library.db')

    while True:
        print("\nMenu:")
        print("1. Add book")
        print("2. Remove book")
        print("3. Update book")
        print("4. Display books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter book publication year: "))
            library.add_book(title, author, year)

        elif choice == '2':
            book_id = int(input("Enter ID of book to remove: "))
            library.remove_book(book_id)

        elif choice == '3':
            book_id = int(input("Enter ID of book to update: "))
            title = input("Enter updated title: ")
            author = input("Enter updated author: ")
            year = int(input("Enter updated publication year: "))
            library.update_book(book_id, title, author, year)

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            print("Exiting library system.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
