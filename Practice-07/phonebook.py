import psycopg2
import csv
import os
from config import host, database, user, password, port


connection = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")

connection.commit()


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cursor.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    connection.commit()
    print("Contact added")

def import_csv():
    path = os.path.join(os.path.dirname(__file__), "contacts.csv")

    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row["Name"], row["Phone"])
            )

    connection.commit()

    print("CSV imported")

def show_contacts():
    cursor.execute("SELECT * FROM phonebook")

    contacts = cursor.fetchall()

    for contact in contacts:
        print(contact)


def search_contact():
    name = input("Enter name to search: ")

    cursor.execute(
        "SELECT * FROM phonebook WHERE name = %s",
        (name,)
    )

    contacts = cursor.fetchall()

    for contact in contacts:
        print(contact)


def update_contact():
    name = input("Enter contact name: ")
    phone = input("Enter new phone: ")

    cursor.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (phone, name)
    )

    connection.commit()

    print("Contact updated")


def delete_contact():
    name = input("Enter name to delete: ")

    cursor.execute(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)
    )

    connection.commit()

    print("Contact deleted")


while True:

    print("""
1 - Add contact
2 - Show contacts
3 - Search contact
4 - Update contact
5 - Delete contact
6 - Import CSV
7 - Exit
""")

    choice = input("Choose: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        import_csv()

    elif choice == "7":
        break


cursor.close()
connection.close()