import sqlite3
import json
from pathlib import Path


product_data = json.loads(Path('product.json').read_text())


# print(type(product_data))

# with sqlite3.connect('products.sqlite3') as connection:
#     command = "INSERT INTO product VALUES (?, ?)"

#     for product in product_data:
#         connection.execute(command, tuple(product.values()))
    
#     connection.commit()



with sqlite3.connect('products.sqlite3') as connection:
    command = "SELECT * FROM product"

    quaryex = connection.execute(command)

    for y in quaryex:
        print(y)

