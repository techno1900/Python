from pathlib import Path
from zipfile import ZipFile

zip_a = ZipFile("zipfiles/aaa.zip", "w")


for z in Path("Video/").glob("*.*"):
    zip_a.write(z)

zip_a.close()