import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="phonebook", user="postgres",
                        password="jujutsukaisen", port=5432)  
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute("""
    CREATE TABLE if not exists contacts4 (
    name VARCHAR(255),
    phone_number VARCHAR(30)
    );
""")

# cur.execute("""
#     INSERT INTO contacts4 (name, phone_number) VALUES ('Azamat', '87074423958');
# """)

# cur.execute("""
#     UPDATE contacts4 SET name = 'John' WHERE phone_number = '87074423958' ;
# """)

# cur.execute("""
#     UPDATE contacts4 SET phone_number = '85247774758' WHERE phone_number = '87074423958' ;
# """)



conn.commit()