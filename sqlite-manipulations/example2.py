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

# Creating table (as parameters, it receives the (name:type) of the column)
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(145123123213212, '2016-01-01', 'Python', 5)")
    conn.commit() # Everytime we modify our data, we need to run this command
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H: %M: %S'))
    keyword = 'Python'
    value = random.randrange(0, 10)

    # ? is for dynamic variables
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)", 
             (unix, date, keyword, value))    

    # Wrong: passing 3 values to 4 parameters declared
    """c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?)", 
             (unix, date, keyword, value))"""

    # Right: passing only two values but declared the only two fields
    """c.execute("INSERT INTO stuffToPlot (unix, keyword) VALUES (?, ?)", 
             (unix, date, keyword, value))"""

    conn.commit()
    # Do not close your connect because you will make lots of request to the Database
    # Close them all at the end of the whole script

create_table()
#data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

c.close()
conn.close()