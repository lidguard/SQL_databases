import sqlite3

db = sqlite3.connect('python_programming_db')
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming(
    id int(2) primary key,
    name varchar(25),
    grade int(3))
    ''')

print("table created")


data = [(55, 'Carl Davis', 61),
        (66, 'Dennis Fredrickson', 88),
        (77, 'Jane Richards', 78),
        (12, 'Peyton Sawyer', 45),
        (2, 'Lucas Brooke', 99)]

cursor.executemany('''
    INSERT INTO python_programming(id, name, grade)
    VALUES (?,?,?)''', data)

#print("data added")

cursor.execute('''
    SELECT * 
    FROM python_programming
    WHERE grade BETWEEN 60 AND 80;
    ''')

grade_data = cursor.fetchall()
print(grade_data)

cursor.execute('''
    UPDATE python_programming
    SET grade = 65
    WHERE name ='Carl Davis';
    ''')

#print("Carl updated")

cursor.execute('''
    DELETE FROM python_programming
    WHERE name ='Dennis Fredrickson';    
    ''')

#print("Dennis deleted")

cursor.execute('''
    UPDATE python_programming
    SET grade = 100
    WHERE id <55;    
    ''')


db.commit()
print("id 55 updated")
