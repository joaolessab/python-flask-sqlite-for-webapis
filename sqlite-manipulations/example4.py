import sqlite3
import os.path
import time
import datetime
import random

# Does not exist yet, so the sqlite3 will create automatically
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "tutorial2.db")

conn = sqlite3.connect(db_path)
c = conn.cursor()

# Update function
def update():
    c.execute("SELECT * FROM stuffToPlot")
    [print(row) for row in c.fetchall()]

    c.execute("UPDATE stuffToPlot SET value = 99 WHERE value = 7")
    conn.commit()

    print("Below here was modified")

    c.execute("SELECT * FROM stuffToPlot")
    [print(row) for row in c.fetchall()]

# Delete function
def delete():
    c.execute("DELETE FROM stuffToPlot WHERE value = 99")
    conn.commit()

    c.execute("SELECT * FROM stuffToPlot")
    [print(row) for row in c.fetchall()]

update()
delete()

c.close()
conn.close()