import sqlalchemy


engine = sqlalchemy.create_engine("sqlite:///movie_library.db")

connection = engine.connect()
metadata = sqlalchemy.MetaData()
movies = sqlalchemy.Table("Movies", metadata, autoload=True, autoload_with = engine)


#Selecting All the Recodes in the DB 

quary = sqlalchemy.select([movies])

# retriving data 

result_proxy = connection.execute(quary)
result = result_proxy.fetchall()
print(result)


# import sqlalchemy

# # Create an SQLite engine
# engine = sqlalchemy.create_engine("sqlite:///movie_library.db")

# # Connect to the database
# connection = engine.connect()

# # Define metadata
# metadata = sqlalchemy.MetaData()

# # Load the "Movies" table (assuming it exists in the database)
# movies = sqlalchemy.Table("Movies", metadata, autoload_with=engine, autoload=True)

# # Select all records from the table
# query = sqlalchemy.select([movies])

# # Execute the query and fetch the results
# result_proxy = connection.execute(query)
# result = result_proxy.fetchall()

# # Print the results

# print(result)







# import sqlalchemy

# engine = sqlalchemy.create_engine("sqlite:///movie_library.db")
# connection = engine.connect()
# metadata = sqlalchemy.MetaData()

# # Define the table structure manually
# movies = sqlalchemy.Table("Movies", metadata,
#                           sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
#                           sqlalchemy.Column('title', sqlalchemy.String),
#                           sqlalchemy.Column('release_year', sqlalchemy.Integer),
#                           sqlalchemy.Column('genre', sqlalchemy.String)
#                          )

# # Load the table structure from the database
# metadata.reflect(bind=engine)

# # Selecting All the Records in the DB
# query = sqlalchemy.select([movies])

# # Executing the query and fetching the results
# result_proxy = connection.execute(query)
# result = result_proxy.fetchall()
# print(result)
