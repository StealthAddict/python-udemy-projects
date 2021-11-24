import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db") #Making the connection to the database
    cur = conn.cursor() #Creating the cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")  #Enter SQL code
    conn.commit() #Commit your changes
    conn.close() #Close the database


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()


# insert("Orange Juice", 67, 2.5)
# delete("Wine Glass")
# update("Coffee Cup", 26, 6)
print(view())