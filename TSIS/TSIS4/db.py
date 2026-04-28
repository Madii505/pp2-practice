import psycopg2
from config import DB_CONFIG

def connect():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS game_sessions (
        id SERIAL PRIMARY KEY,
        player_id INTEGER REFERENCES players(id),
        score INTEGER NOT NULL,
        level_reached INTEGER NOT NULL,
        played_at TIMESTAMP DEFAULT NOW()
    );
    """)

    conn.commit()
    conn.close()


def get_player(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    row = cur.fetchone()

    if row:
        conn.close()
        return row[0]

    cur.execute("INSERT INTO players(username) VALUES (%s) RETURNING id", (username,))
    pid = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return pid


def save_game(username, score, level):
    conn = connect()
    cur = conn.cursor()

    pid = get_player(username)

    cur.execute("""
    INSERT INTO game_sessions(player_id, score, level_reached)
    VALUES (%s, %s, %s)
    """, (pid, score, level))

    conn.commit()
    conn.close()


def get_top10():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT p.username, g.score, g.level_reached, g.played_at
    FROM game_sessions g
    JOIN players p ON g.player_id = p.id
    ORDER BY g.score DESC
    LIMIT 10
    """)

    data = cur.fetchall()
    conn.close()
    return data


def get_best(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT MAX(g.score)
    FROM game_sessions g
    JOIN players p ON g.player_id = p.id
    WHERE p.username=%s
    """, (username,))

    row = cur.fetchone()
    conn.close()
    return row[0] if row[0] else 0