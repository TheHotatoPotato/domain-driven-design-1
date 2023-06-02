import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=todo user=moaz")
cur = conn.cursor()

with cur as cursor:
    cursor.execute(open("initialize-db.sql", "r").read())
    conn.commit()
    
# # Open a cursor to perform database operations
# cur = conn.cursor()

# # Execute a query
# cur.execute("SELECT * FROM company")

# # Retrieve query results
# records = cur.fetchall()

# print(records)