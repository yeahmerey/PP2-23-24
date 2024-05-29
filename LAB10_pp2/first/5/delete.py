import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="phonebook", user="postgres",
                        password="jujutsukaisen", port=5432)   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute("""
    CREATE TABLE if not exists contacts6 (
    name VARCHAR(255),
    phone_number VARCHAR(30) PRIMARY KEY
    );
""")

# import csv

# filename = "labwork10/first/5/blacklist.csv"

# with open(filename, "r") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     for row in csvreader:
#         print(row)

#         name, phone_number = row
        
#         cur.execute(f"""INSERT INTO contacts6 (name, phone_number) VALUES ('{name}','{phone_number}');""")

cur.execute(f"""DELETE FROM contacts6 WHERE name = 'Kroos';""")

conn.commit()