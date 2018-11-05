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

def read_from_db():
    c.execute("SELECT * FROM stuffToPlot")
    #data = c.fetchall()
    #print (data)    
    for row in c.fetchall():
        print (row)

# Compound Select
def read_from_db_detailed():
    c.execute("SELECT * FROM stuffToPlot WHERE value = 7 AND keyword = 'Python'")
    for row in c.fetchall():
        print (row)

# Compound Select
def read_from_db_detailed():
    c.execute("SELECT * FROM stuffToPlot WHERE unix > 1452618731")
    for row in c.fetchall():
        print (row)

# Compound Select changing the ORDER of things
def read_from_db_detailed_ordered():
    c.execute("SELECT keyword, unix, value, datestamp FROM stuffToPlot WHERE unix > 1452618731")
    for row in c.fetchall():
        print (row)

# read_from_db()
# read_from_db_detailed()
read_from_db_detailed_ordered()

c.close()
conn.close()