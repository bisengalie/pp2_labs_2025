import psycopg2
import csv

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="your_database_name",
    user="your_username",
    password="your_password"
)
cur = conn.cursor()

# Create table
def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    ''')
    conn.commit()

# Insert data from CSV
def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s);", (row[0], row[1]))
    conn.commit()
    print("Data inserted from CSV.")

# Insert data from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s);", (name, phone))
    conn.commit()
    print("Data inserted from console.")

# Update data
def update_data():
    identifier = input("Enter name or phone to identify the user to update: ")
    new_name = input("Enter new name (leave blank to skip): ")
    new_phone = input("Enter new phone (leave blank to skip): ")

    if new_name:
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s OR phone = %s;", (new_name, identifier, identifier))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s OR phone = %s;", (new_phone, identifier, identifier))
    conn.commit()
    print("Data updated.")

# Query data with filters
def query_data():
    filter_type = input("Filter by (1) Name or (2) Phone or (3) Show all? ")
    if filter_type == "1":
        name = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE name = %s;", (name,))
    elif filter_type == "2":
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s;", (phone,))
    else:
        cur.execute("SELECT * FROM phonebook;")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Delete data
def delete_data():
    identifier = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s;", (identifier, identifier))
    conn.commit()
    print("Data deleted.")

# Menu
def menu():
    create_table()
    while True:
        print("\n📱 PhoneBook Menu:")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_csv("phonebook.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            break
        else:
            print("Invalid option. Try again.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    menu()
