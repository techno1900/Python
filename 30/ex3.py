import sqlite3 

with sqlite3.connect('movie_library.db') as connection:
    cursor  = connection.cursor()

    my_movie_list = [
        ('john wick','nimsara',1990),
        ('expenderble', 'lakisha', 2000)
    ]

    cursor.executemany("INSERT INTO Movies VALUES(?,?,?)", my_movie_list)

    records = cursor.execute("SELECT * FROM Movies")

    for i in records:
        print(i)

    connection.commit()