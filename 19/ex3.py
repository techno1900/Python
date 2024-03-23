from pathlib import Path

source = Path('text.py')
from time import ctime
print(source.exists())


# print(source.stat())

print(ctime(source.stat().st_atime))

# print(source.read_text())
print(source.write_text("print('heloow')"))
print(source.read_text())

