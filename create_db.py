import sqlite3

def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course(
            id PRIMARY KEY AUTOINCREMENT,
            cid INTEGER PRIMARY KEY,
            name TEXT,
            duration TEXT,
            charges TEXT,
            description TEXT
        )
    """)
    con.commit()
    

create_db()
