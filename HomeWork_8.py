import sqlite3 as sq
with sq.connect('students.db') as con:
    cur = con.cursor()
    # cur.execute('''DROP TABLE student''')
    cur.execute('''CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hobbi TEXT,
    name TEXT,
    surname TEXT,
    year_of_birth INTEGER,
    score INTEGER
    ) ''')
    students_data = [
        ('Reading', 'John', 'Smith', 1995, 12),
        ('Painting', 'Alice', 'Johnson', 1997, 8),
        ('Singing', 'David', 'Williams', 1998, 15),
        ('Coding', 'Sarah', 'Brown', 1996, 9),
        ('Dancing', 'Michael', 'Davis', 1994, 18),
        ('Gaming', 'Emily', 'Anderson', 1999, 7),
        ('Hiking', 'Daniel', 'Lee', 1997, 14),
        ('Cooking', 'Olivia', 'Martinez', 1993, 5),
        ('Swimming', 'William', 'Thompson', 1992, 13),
        ('Traveling', 'Sophia', 'Garcia', 1998, 11)
    ]

    cur.executemany('INSERT INTO student (hobbi, name, surname, year_of_birth, score) VALUES (?, ?, ?, ?, ?)',
                    students_data)
    con.commit()

    cur.execute("SELECT * FROM student WHERE LENGTH(surname) > 10")
    results = cur.fetchall()

    print("Студенты с фамилией больше 10 символов:")
    for row in results:
        print(row)
    cur.execute("UPDATE student SET name = 'genius' WHERE score > 10")

    cur.execute("SELECT * FROM student WHERE name = 'genius'")
    results = cur.fetchall()

    print("\nСтуденты с именем 'genius':")
    for row in results:
        print(row)

    cur.execute("DELETE FROM student WHERE id % 2 = 0")

    con.commit()
