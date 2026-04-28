import psycopg2
import json

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook",
    user="postgres",
    password="1234"
)


def get_contacts(group=None, search=None, sort="name", limit=5, offset=0):
    cur = conn.cursor()

    query = """
    SELECT c.name, c.email, c.birthday, g.name, p.phone
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE 1=1
    """

    params = []

    if group:
        query += " AND g.name = %s"
        params.append(group)

    if search:
        query += " AND c.email ILIKE %s"
        params.append(f"%{search}%")

    query += f" ORDER BY {sort} LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    cur.execute(query, params)
    return cur.fetchall()


def pagination():
    offset = 0
    limit = 5

    while True:
        rows = get_contacts(limit=limit, offset=offset)

        for r in rows:
            print(r)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        elif cmd == "quit":
            break


def export_json():
    cur = conn.cursor()

    cur.execute("""
    SELECT c.id, c.name, c.email, c.birthday, g.name
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    """)

    contacts = []

    for row in cur.fetchall():
        c_id, name, email, birthday, group = row

        cur.execute("SELECT phone, type FROM phones WHERE contact_id=%s", (c_id,))
        phones = cur.fetchall()

        contacts.append({
            "name": name,
            "email": email,
            "birthday": str(birthday),
            "group": group,
            "phones": [{"number": p[0], "type": p[1]} for p in phones]
        })

    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)


def import_json():
    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for c in data:
        name = c["name"]

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        existing = cur.fetchone()

        if existing:
            choice = input(f"{name} exists. skip / overwrite: ")
            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

        cur.execute("""
        INSERT INTO contacts(name, email, birthday)
        VALUES (%s, %s, %s)
        RETURNING id
        """, (name, c["email"], c["birthday"]))

        c_id = cur.fetchone()[0]

        for p in c["phones"]:
            cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES (%s, %s, %s)
            """, (c_id, p["number"], p["type"]))

    conn.commit()


if __name__ == "__main__":
    while True:
        print("1. Show contacts")
        print("2. Export JSON")
        print("3. Import JSON")
        print("4. Exit")

        choice = input(">> ")

        if choice == "1":
            pagination()
        elif choice == "2":
            export_json()
        elif choice == "3":
            import_json()
        elif choice == "4":
            break