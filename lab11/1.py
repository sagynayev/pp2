import psycopg2
import csv
from functions import get_records
from tabulate import tabulate 

conn = psycopg2.connect(
    host="localhost",
    dbname = "PhoneBook cont.",
    user = "postgres",
    password = "multik123",
    port = 5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
      user_id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      surname VARCHAR(255) NOT NULL, 
      phone VARCHAR(255) NOT NULL
)
""")

#functions and procedures
cur.execute("""
CREATE OR REPLACE FUNCTION get_paginated_data(phonebook TEXT, limit_val INT, offset_val INT)
RETURNS TABLE (id INT, name VARCHAR, surname VARCHAR, phone VARCHAR) AS $$
BEGIN
  RETURN QUERY EXECUTE format('
    SELECT user_id, name, surname, phone 
    FROM %I
    ORDER BY user_id
    LIMIT %s
    OFFSET %s
  ', phonebook, limit_val, offset_val);
END;
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE PROCEDURE delete_user(IN search_term VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
  DELETE FROM phonebook WHERE name ILIKE ('%' || search_term || '%') OR phone ILIKE ('%' || search_term || '%');
END;
$$;
""")

cur.execute("""
CREATE OR REPLACE PROCEDURE insert_or_update_user(IN user_name VARCHAR, IN user_surname VARCHAR, IN user_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
  UPDATE phonebook SET phone = user_phone WHERE name = user_name;
  IF NOT FOUND THEN
    INSERT INTO phonebook (name, surname, phone) VALUES (user_name, user_surname, user_phone);
  END IF;
END;
$$;
""")

cur.execute("""
CREATE OR REPLACE FUNCTION insert_list_of_users(names TEXT[], surnames TEXT[], phones TEXT[])
RETURNS TEXT[] AS
$$
DECLARE
    i INTEGER;
    incorrect_phones TEXT[] := '{}';
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] LIKE '+___________' AND length(phones[i]) = 12 THEN
            INSERT INTO phonebook(name, surname, phone) VALUES(names[i], surnames[i], phones[i]);
        ELSE
            incorrect_phones := array_append(incorrect_phones, phones[i]);
        END IF;
    END LOOP;
    
    RETURN incorrect_phones;
END;
$$
LANGUAGE plpgsql;


""")

#variables
check = True
command = ''
temp = ''

name_var = ''
surname_var = ''
phone_var = ''
id_var = ''

start = True
back = False

back_com = ''
name_upd = ''
surname_upd = ''
phone_upd = ''

filepath = ''

names = []
surnames = []
phones = []
incorrect_data = []
n = 0

#main
while check:
    if start == True or back == True:
        start = False
        print("""
        List of the commands:
        1. Type "i" or "I" in order to INSERT data to the table.
        2. Type "u" or "U" in order to UPDATE data in the table.
        3. Type "q" or "Q" in order to make specidific QUERY in the table.
        4. Type "d" or "D" in order to DELETE data from the table.
        5. Type "f" or "F" in order to close the program.
        6. Type "s" or "S" in order to see the values in the table.
        """)
        command = str(input())
        
        #insert
        if command == "i" or command == "I":
            back = False
            command = ''
            print('Type "csv" or "con" or "list" to choose option between uploading csv file or typing from console or by list: ')
            command = ''
            temp = str(input())
            if temp == "con":
                name_var = str(input("Name: "))
                surname_var = str(input("Surname: "))
                phone_var = str(input("Phone: "))
                cur.execute("CALL insert_or_update_user(%s, %s, %s)", (name_var, surname_var, phone_var))
                conn.commit()
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            if temp == "csv":
                filepath = input("Enter a file path with proper extension: ")
                with open(str(filepath), 'r') as f:
                # Skip the header row.
                    reader = csv.reader(f, delimiter=';')
                    next(reader)
                    for row in reader:
                        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
                conn.commit()   
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            if temp == "list":
                    n = int(input(("Enter number of users that you want to add to the table: ")))
                    for i in range(0, n):
                        name_var = str(input("Name: "))
                        names.append(name_var)
                        surname_var = str(input("Surname: "))
                        surnames.append(surname_var)
                        phone_var = str(input("Phone: "))
                        phones.append(phone_var)
                    
                    cur.execute("""SELECT insert_list_of_users(%s, %s, %s);""", (names, surnames, phones))
                    incorrect_data = cur.fetchone()[0]
                    if len(incorrect_data) > 0:
                        print("There are some incorrect phone numbers! Incorrect phone numbers:")
                        print(incorrect_data)
                    else:
                        print("Everything is correct!")
                    names = []
                    surnames = []
                    phones = []
                    back_com = str(input('Type "back" in order to return to the list of the commands: '))
                    if back_com == "back":
                        back = True
            else:
                back_com = str(input('Incorrect command! Type "back" and try again: '))
                if back_com == "back":
                        back = True
        #delete
        if command == "d" or command == "D":
            back = False
            command = ''
            cur.execute("SELECT * from phonebook;")
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            phone_var = str(input('Type phone number which you want to delete: '))
            cur.execute("CALL delete_user(%s)", (phone_var,))
            back_com = str(input('Type "back" in order to return to the list of the commands: '))
            if back_com == "back":
                back = True
        
        #update
        if command == 'u' or command == 'U':
            back = False
            command = ''
            temp = str(input('Type the name of the column that you want to change: '))
            if temp == "name":
                name_var = str(input("Enter name that you want to change: "))
                name_upd = str(input("Enter the new name: "))
                cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (name_upd, name_var))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

            if temp == "surname":
                surname_var = str(input("Enter surname that you want to change: "))
                surname_upd = str(input("Enter the new surname: "))
                cur.execute("UPDATE phonebook SET surname = %s WHERE surname = %s", (surname_upd, surname_var))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

            if temp == "phone":
                name_var = str(input("Enter phone number that you want to change: "))
                name_upd = str(input("Enter the new phone number: "))
                cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (phone_upd, phone_var))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            else:
                back_com = str(input('Incorrect command! Type "back" and try again: '))
                if back_com == "back":
                        back = True
        
        #query
        if command == "q" or command == "Q":
            back = False
            command = ''
            temp = str(input("Type the name of the column which will be used for searching data or type page in order to query with pagination: "))
            if temp == "id":
                id_var = str(input("Type id of the user: "))
                cur.execute("SELECT * FROM phonebook WHERE user_id = %s", (id_var, ))
                rows = cur.fetchall()
                print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            
            if temp == "name":
                name_var = str(input("Type pattern for name column: "))
                rows = get_records(name_var)
                print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            
            if temp == "surname":
                surname_var = str(input("Type pattern for surname column: "))
                rows = get_records(surname_var)
                print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
                
            if temp == "phone":
                phone_var = str(input("Type pattern for phone column: "))
                rows = get_records(phone_var)
                print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            if temp == "page":
                limit = int(input("Type limit value: "))
                offset = int(input("Type offset value: "))
                cur.callproc('get_paginated_data', ['phonebook', limit, offset])
                rows = cur.fetchall()
                print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            else:
                back_com = str(input('Incorrect command! Type "back" and try again: '))
                if back_com == "back":
                        back = True
        
        #display
        if command == "s" or command == "S":
            back = False
            command = ''
            cur.execute("SELECT * from phonebook;")
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            back_com = str(input('Type "back" in order to return to the list of the commands: '))
            if back_com == "back":
                back = True
        #finish
        if command == "f" or command == "F":
            command = ''
            check = False
        else:
            back = True
        

conn.commit()
cur.close()
conn.close()