import csv
from connect import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
    """)

    conn.commit()
    cur.close()
    conn.close()


def insert_from_csv(file_path):
    conn = get_connection()
    cur = conn.cursor()

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            name, phone = row
            cur.execute("""
                INSERT INTO phonebook (name, phone)
                VALUES (%s, %s)
                ON CONFLICT (name) DO NOTHING;
            """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()


def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO phonebook (name, phone)
        VALUES (%s, %s)
        ON CONFLICT (name) DO NOTHING;
    """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()


def update_contact():
    name = input("Enter name to update: ")
    new_name = input("New name (leave empty to skip): ")
    new_phone = input("New phone (leave empty to skip): ")

    conn = get_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute("UPDATE phonebook SET name=%s WHERE name=%s", (new_name, name))
        name = new_name

    if new_phone:
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, name))

    conn.commit()
    cur.close()
    conn.close()


def query_contacts():
    print("1 - All")
    print("2 - By name")
    print("3 - By phone prefix")

    choice = input("Choice: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        cur.execute("SELECT * FROM phonebook")

    elif choice == "2":
        name = input("Name: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))

    elif choice == "3":
        prefix = input("Prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"{prefix}%",))

    rows = cur.fetchall()
    for r in rows:
        print(r)

    cur.close()
    conn.close()


def delete_contact():
    print("1 - By name")
    print("2 - By phone")

    choice = input("Choice: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Name: ")
        cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    else:
        phone = input("Phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

    conn.commit()
    cur.close()
    conn.close()


def menu():
    while True:
        print("\n1.Create table")
        print("2.Insert from CSV")
        print("3.Insert from console")
        print("4.Update")
        print("5.Query")
        print("6.Delete")
        print("0.Exit")

        choice = input(">> ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv("contacts.csv")
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            query_contacts()
        elif choice == "6":
            delete_contact()
        elif choice == "0":
            break


if __name__ == "__main__":
    menu()