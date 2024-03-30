import re

test_string = "bag"
test_string = "dog"
test_string = "tahaen"


patten = ".a."


result = re.match(patten, test_string)
print(result)
