import psycopg2

def get_records(pattern):
    conn = psycopg2.connect(
        host="localhost", 
        dbname = "PhoneBook cont.", 
        user = "postgres",
        password = "multik123", 
        port = 5432)
    cur = conn.cursor()

    query = "SELECT * FROM phonebook WHERE name LIKE %s OR surname LIKE %s OR phone LIKE %s"
    cur.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))

    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results