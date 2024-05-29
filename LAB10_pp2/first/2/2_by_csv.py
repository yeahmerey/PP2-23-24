import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="phonebook", user="postgres",
                        password="jujutsukaisen", port=5432)   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute('DROP TABLE contacts2 ;')

conn.commit()

cur.execute("""
    CREATE TABLE contacts2 (
    name VARCHAR(255),
    phone_number VARCHAR(30) PRIMARY KEY
    );
""")

import csv

filename = "labwork10/first/2/contactname.csv"

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)

        name, phone_number = row
        
        cur.execute(f"""INSERT INTO contacts2 (name, phone_number) VALUES ('{name}','{phone_number}');""")

conn.commit()
