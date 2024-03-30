import sqlite3

with sqlite3.connect('movie_library.db') as connection:
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Movies VALUES('Love and Thounder','siripala',10)")

    cursor.execute("SELECT * FROM Movies")
    cursor.fetchone()
    connection.commit()