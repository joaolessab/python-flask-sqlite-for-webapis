import sqlite3
import os.path

# Does not exist yet, so the sqlite3 will create automatically
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "tutorial.db")

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

create_table()
data_entry()