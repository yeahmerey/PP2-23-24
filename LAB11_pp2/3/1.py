import psycopg2
import csv
from tabulate import tabulate 

conn = psycopg2.connect(host="localhost", dbname="book", user="postgres",
                        password="jujutsukaisen", port=5432)

cur = conn.cursor()

conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE if not exists contact (
      user_id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      surname VARCHAR(255) NOT NULL, 
      phone VARCHAR(255) NOT NULL
)
""")

def delete_data():
    phone = input('Phone number: ')
    cur.execute("DELETE FROM contact WHERE phone = %s ;", (phone,))
    conn.commit()

delete_data()
