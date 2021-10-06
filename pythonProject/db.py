import sqlite3

conn = sqlite3.connect("database.db")

print("opened database")


conn.execute("CREATE TABLE login (username TEXT, password TEXT)");



conn.execute("CREATE TABLE student (name TEXT, addr TEXT, city TEXT, pin TEXT)");


print("table created")

conn.close()