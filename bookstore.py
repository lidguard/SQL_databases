import sqlite3
db = sqlite3.connect('bookstore_db')
cursor = db.cursor()

#Create the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookstore(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    Quantity INTEGER(4))
    
    ''')


books = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
         (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
         (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
         (3004, 'The Lord of the Rings', 'J.R.R Tolkein', 37),
         (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]


cursor.executemany('''
    INSERT INTO bookstore(id, Title, Author, Quantity)
    VALUES (?,?,?,?)''', books)

#Define menu functions
def new_book():
    title = input("Enter the title of the book: \n")
    author = input("Please enter the author of this book: \n")
    quantity = int(input("How many copies of this book are in stock? \n"))

    cursor.execute('''
        INSERT INTO bookstore(Title, Author, Quantity)
        VALUES(?,?,?);''', (title, author, quantity))

    db.commit()

    print("New entry added successfully ")
    menu()


def update_book():
    cursor.execute('''
        SELECT id, Title FROM bookstore
        ''')
    books = cursor.fetchall()
    print("Here are your current stocked titles: \n")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}")

    book_id = int(input("Enter the ID of the book you wish to update: \n"))
    cursor.execute('''
        SELECT Title, Author, Quantity FROM bookstore WHERE id=?''',(book_id,))
    book = cursor.fetchone()
    if book is None:
        print("Error: book not found, please try again")
        menu()
    else:
        print(f"Here is your selection: {book}\n")

    update = input("What would you like to update? \n"
                   "1 - Title\n"
                   "2 - Author\n"
                   "3 - Quantity\n"
                   "4 - Exit Update and return to Main Menu \n")

    if update == "1":
        new_title = input("Enter the new title: \n")
        cursor.execute('''
            UPDATE bookstore SET Title= ? WHERE id= ?''', (new_title, book_id))
        print("Item updated successfully \n")
    elif update == "2":
        new_author = input("Enter the new author: \n")
        cursor.execute('''
            UPDATE bookstore SET Author= ? WHERE id= ?''', (new_author, book_id))
        print("Item updated successfully \n")
    elif update == "3":
        new_quantity = int(input("Enter the updated stock for this title: \n"))
        cursor.execute('''
            UPDATE bookstore SET Quantity= ? WHERE id= ?''', (new_quantity, book_id))
        print("Item updated successfully \n")
    elif update == "4":
        menu()
    else:
        print("Error: not a valid option")
        menu()

    db.commit()

    menu()


def delete_book():
    cursor.execute('''
        SELECT id, Title FROM bookstore
        ''')
    books = cursor.fetchall()
    print("Here are your current stocked titles: \n")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}")

    book_id = input("Please enter the ID of the book you wish to delete: \n")
    check = input(f"Are you sure you want to delete the record for {book[1]}? "
                  f"y/n: \n")
    if check == "y":
        delete = "DELETE FROM bookstore WHERE id = ?"
        cursor.execute(delete, (book_id,))
        db.commit()
        print("Item deleted successfully")
        menu()
    else:
        menu()

def search():
    choice = input("Do you wish to search by Title or Author?\n").lower()
    if choice == "title":
        title = input("Please enter the title of the book you wish to search: \n")
        select = "SELECT * FROM bookstore WHERE Title = ?"
        cursor.execute(select, (title,))
        results = cursor.fetchall()
        if results == []:
            print("Title not found")
            menu()
        else:
            print(f"Here is your book: \n {results} \n")

    elif choice == "author":
        author = input("Please enter the Author you wish to search: \n")
        select_a = "SELECT * FROM bookstore WHERE Author = ?"
        cursor.execute(select_a, (author,))
        results_a = cursor.fetchall()
        if results_a == []:
            print("Author not found")
        else:
            print(f"Here are all stocked titles for {author}:\n {results_a} \n")

    db.commit()
    menu()


#Create user menu
def menu():
    menu = input("Hello, what would you like to do? (Enter number to select)\n"
             "1 - Enter a new book \n"
             "2 - Update a book \n"
             "3 - Delete a book \n"
             "4 - Conduct a search \n"
             "5 - Exit programme \n")

    if menu == "1":
        new_book()
    elif menu == "2":
        update_book()
    elif menu == "3":
        delete_book()
    elif menu == "4":
        search()
    elif menu == "5":
        print("Goodbye!")
        exit()





menu()

db.commit()
