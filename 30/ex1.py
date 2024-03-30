# import sqlite3

# with sqlite3.connect('movie_library.db') as connection:
#     cursor = connection.cursor()

#     cursor.execute(''' 
#     CREATE TABLE Movies(
#                    Title TEXT,
#                    director TEXT,
#                    Year INT
#     )

# ''')
#     connection.commit()


import sqlite3

with sqlite3.connect('my_db.db') as connection:
    cursor = connection.cursor()
    cursor.execute(''' 

CREATE TABLE movies(
                   author TEXT,
                   date TEXT
                   tp INT
);

''')
    
    connection.commit()