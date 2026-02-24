import mysql.connector
conn = mysql.connector.connect(
    host="localhost",      # or your DB host (IP / cloud URL)
    user="root",           # MySQL username
    password="atiya123",   # MySQL password
    database="test_db"     # Database name
)

print("Connected successfully!")
