import sqlite3 as sql

conn = sql.connect("randomNames.db")
cur = conn.cursor()
cur.execute("SELECT * FROM PEOPLE")
    
rows = cur.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
