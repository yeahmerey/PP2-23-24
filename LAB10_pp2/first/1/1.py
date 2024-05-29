import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="phonebook", user="postgres",
                        password="jujutsukaisen", port=5432)   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute('DROP TABLE contacts1 ;')

conn.commit()

cur.execute("""
    CREATE TABLE contacts1 (
    name VARCHAR(255),
    phone_number VARCHAR(255) PRIMARY KEY
    );
""")

conn.commit()
