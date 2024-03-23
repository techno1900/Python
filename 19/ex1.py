

from pathlib import Path



# print(Path.home())

path1 = Path('users')
path2 = Path('videos/nimsara')
path3 = Path('images/nimsara')

path4 = Path(r'E:\Udemy\Python\19\ex1.py')


print(path1.exists())
print(path2.exists())
print(path3.exists())
print(path4.exists())


print(path1.is_file())
print(path4.is_file())






