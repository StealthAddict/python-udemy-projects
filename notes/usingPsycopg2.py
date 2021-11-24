import psycopg2     # Connects to PostgreSQL

def create_table():
    conn = psycopg2.connect("dbname='forudemy' user='postgres' password= 'potentialgrass' host= 'localhost' port= '5432'") #Making the connection to the database
    cur = conn.cursor() #Creating the cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")  #Enter SQL code
    conn.commit() #Commit your changes
    conn.close() #Close the database


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='forudemy' user='postgres' password= 'potentialgrass' host= 'localhost' port= '5432'") 
    cur = conn.cursor() 
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)" , (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='forudemy' user='postgres' password= 'potentialgrass' host= 'localhost' port= '5432'") 
    cur = conn.cursor() 
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='forudemy' user='postgres' password= 'potentialgrass' host= 'localhost' port= '5432'") 
    cur = conn.cursor() 
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = psycopg2.connect("dbname='forudemy' user='postgres' password= 'potentialgrass' host= 'localhost' port= '5432'") 
    cur = conn.cursor() 
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

# create_table()
# insert("Papaya Juice", 6, 3.5)
# delete("Orange Juice")
# update("Orange Juice", 8, 2.4)
print(view())