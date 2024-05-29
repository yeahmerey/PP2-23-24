import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="snakegame", user="postgres",
                        password="jujutsukaisen", port=5432)   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute('DROP TABLE records;')
cur.execute('DROP TABLE position;')


conn.commit()

cur.execute("""
    CREATE TABLE records (
    user_name VARCHAR(255),
    user_score VARCHAR(30),
    level VARCHAR(30)
    );
""")

cur.execute("""
    CREATE TABLE position (
    state VARCHAR(255),
    score VARCHAR(30)
    );
""")

import csv

filename = "labwork10/second/players.csv"
filee = "labwork10/second/current_state.csv"

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)

        user_name, user_score, level = row
        
        cur.execute(f"""INSERT INTO records (user_name, user_score, level) VALUES ('{user_name}','{user_score}','{level}');""")

with open(filee, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)

        state, score = row
        
        cur.execute(f"""INSERT INTO position (state, score) VALUES ('{state}','{score}');""")

conn.commit()