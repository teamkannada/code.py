import sqlite3 #import the sdlite3 module
conn = sqlite3.connect("gfgc.db")
cursor = conn.cursor()
cursor.execute("DROp TABLE IF EXISTS indians")
cursor.execute("CREATE TABLE indians (id INTEGER PRIMARY KEY,name TEXT,age INTEGER)")
cursor.execute("INSERT into indians(name,age)VALUES('ram',20)")
cursor.execute("INSERT INTO indians(name,age)VALUES('priya',18)")
cursor.execute("INSERT INTO indians(name,age)VALUES('ravi',21)")
conn.commit()
print("data after insert: ")
for row in cursor.execute("SELECT * FROM indians"):
    print(row)

cursor.execute("UPDATE indians SET age=26 WHERE name='priya'")
print("\ndata after update: ")
for row in cursor.execute("SELECT * FROM indians"):
    print(row)

cursor.execute("DELETE FROM indians WHERE name = 'ravi'")
conn.commit()

print("\ndata after delete: ")
for row in cursor.execute("SELECT * FROM indians"):
    print(row)

print("\n table drop")