
import json
from pathlib import Path


products = [
    {'productname':"product1", "price":100},
    {'productname':"product2", "price":200},
    ]


product_data = json.dumps(products)
print(product_data)

Path('product.json').write_text(product_data)


