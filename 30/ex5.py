import mysql.connector as sql


def connect(db_name):
    try:
        return sql.connect(
            host = "localhost",
            user = "root",
            password = "5543",
            database = db_name,
        )
    
    except Error as err:
        print (err)
    

if __name__ == '__main__':
    db = connect('blog')
    courser = db.cursor()
    courser.execute("SELECT * FROM topics")
    result = courser.fetchall()
    print(result)
