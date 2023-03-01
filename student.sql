import sqlite3

db = sqlite3.connect('data_student_db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS student(
    STU_NUM int(6) primary key,
    STU_SNAME varchar(15),
    STU_FNAME varchar(15),
    STU_INITIAL varchar (1),
    STU_STARTDATE date,
    COURSE_CODE char(3),
    PROJ_NUM int(2))
 ''')

print("database created")

cursor.execute('''
    INSERT INTO student
    VALUES (01, 'Snow', 'John', 'E', '2014/04/05', 201, 6);
''')

cursor.execute('''
    INSERT INTO student
    VALUES (02, 'Stark', 'Arya', 'C', '2017/07/12', 305, 11);
''')
#print("added")

students = [(3, 'Lannister', 'Jamie', 'C', '2012/09/05', 101, 2),
            (4, 'Lannister', 'Cercei', 'J', '2012/09/05', 101, 2),
            (5, 'Greyjoy', 'Theon', 'I', '2015/12/09', 402, 14),
            (6, 'Tyrell', 'Margaery', 'Y', '2017/07/12', 305, 10),
            (7, 'Baratheon', 'Tommen', 'R', '2019/06/13', 201, 5)]

cursor.executemany('''
    INSERT INTO student(STU_NUM, STU_SNAME, STU_FNAME, STU_INITIAL, STU_STARTDATE, COURSE_CODE, PROJ_NUM)
    VALUES (?, ?, ?, ?, ?, ?, ?)''', students)

#print("multiple students added")

cursor.execute('''
    SELECT *
    FROM student
    WHERE COURSE_CODE = 305;
    ''')

course = cursor.fetchall()
print(course)

cursor.execute('''
    UPDATE student
    SET COURSE_CODE = 304
    WHERE STU_NUM = 7;
    ''')
#print("course code updated")

cursor.execute('''
    DELETE FROM student
    WHERE (STU_SNAME = 'Lannister' AND
    STU_FNAME = 'Jamie' AND
    STU_STARTDATE = '2012/09/05' AND
    COURSE_CODE = 101 AND
    PROJ_NUM = 2);
    ''')
#print("row deleted")

cursor.execute('''
    UPDATE student
    SET PROJ_NUM = 14
    WHERE (STU_STARTDATE < '2016/01/01' AND
    COURSE_CODE >= 201);
    ''')
#print("project number updated")


cursor.execute('''
    DELETE FROM student;
    ''')


#print("contents deleted")

cursor.execute('''
    DROP TABLE student;
    ''')


db.commit()
#print("table dropped")
