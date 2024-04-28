import sqlite3

# Function to create a new database
def create_database():
    conn = sqlite3.connect('database.db')
    data = conn.cursor()
    data.execute('''CREATE TABLE IF NOT EXISTS users
                    (name text, place real)''')
    print("Database created successfully.")
    name = input ('Enter amount')
    place = input('Enter cost')
    data.execute("INSERT INTO users VALUES {name}, {place})")
    conn.commit()
    conn.close()

# Function to read data from the database
def read_database():
    conn = sqlite3.connect('database.db')
    data = conn.cursor()
    data.execute('''SELECT * FROM users''')
    row = data.fetchall()
    for row in data.fetchall():
        print(row)
    conn.close()

# Menu function
def menu():
    print("1. Create Database")
    print("2. Read Database")
    print("3. Exit")
    choice = input("Enter your choice 1, 2, or 3): ")

    if choice == '1':
        create_database()
    elif choice == '2':
        read_database()
    elif choice == '3':
        print("Exiting the program.")
        exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    menu()

# Start the menu
menu()
