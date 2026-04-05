from connect import connect

def search(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def paginate(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def upsert(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def bulk(names, phones):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL bulk_insert_contacts(%s, %s)", (names, phones))
    conn.commit()
    cur.close()
    conn.close()

def delete(value):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    cur.close()
    conn.close()