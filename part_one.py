import sqlite3
import os

DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

connection = sqlite3.connect(DATABASE_FILEPATH)
connection.row_factory = sqlite3.Row
print(type(connection))

cursor = connection.cursor()
print(type(cursor))

# Q1: How many total Characters are there?
query = 'SELECT * FROM customers LIMIT 3'

result = cursor.execute(query).fetchall()
for row in result:
    print("-------")
    print(row['FirstName'], row['LastName'])

# Q2: How many of each specific subclass?

# Q3: How many total items?

# Q4: How many of the items are weapons? How many are not?

# Q5: How many Items does each character have? (Return first 20 rows)

# Q6: How many Weapons does each character have? (Return first 20 rows)

# Q7: On average, how many Items does each character have?

# Q8: On average, how many Weapons does each character have?