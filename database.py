import sqlite3

conn = sqlite3.connect('online_radio_database.db')
print("Opened database successfully")

conn.execute("DROP TABLE IF EXISTS online_radio")
conn.execute("CREATE TABLE online_radio (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, host TEXT NOT NULL, status INTEGER DEFAULT 1)")

conn.close()