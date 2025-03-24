#!/usr/bin/env python3

import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
print(conn)

# Create cursor
cursor = conn.cursor()

# Create database "mydatabase"
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

# Show databases
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

# Connect to the newly created database
conn.database = "mydatabase"

# Create "customers" table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255)
    )
""")

# Show tables
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# Insert records
cursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("John Doe", "Wolffintie 32, FIN-65101 Vaasa, Finland"))
cursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("Jane Doe", "Wolffintie 32, FIN-65101 Vaasa, Finland"))
conn.commit()

# Fetch all records
cursor.execute("SELECT * FROM customers")
for record in cursor.fetchall():
    print(record)

# Fetch records with specific address
cursor.execute("SELECT * FROM customers WHERE address = %s", ("Wolffintie 32, FIN-65101 Vaasa, Finland",))
for record in cursor.fetchall():
    print(record)

# Order by name
cursor.execute("SELECT * FROM customers ORDER BY name ASC")
for record in cursor.fetchall():
    print(record)

# Insert third record
cursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("Jim Doe", "Wolffintie 32, FIN-65101 Vaasa, Finland"))
conn.commit()
print("1 record inserted")

# Fetch the new record
cursor.execute("SELECT * FROM customers WHERE name = %s", ("Jim Doe",))
for record in cursor.fetchall():
    print(record)

# Delete Jim Doe's record
cursor.execute("DELETE FROM customers WHERE name = %s", ("Jim Doe",))
conn.commit()
print("1 record deleted")

# Create second database "mydatabase2"
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase2")

# Show databases again
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

# Connect to "mydatabase2"
conn.database = "mydatabase2"

# Create "customers2" table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers2 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255)
    )
""")

# Show tables
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# Drop "customers2" table
cursor.execute("DROP TABLE customers2")

# Show tables again
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# Drop "mydatabase2"
cursor.execute("DROP DATABASE mydatabase2")

# Show databases again
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

# Close connections
cursor.close()
conn.close()
