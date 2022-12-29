from zipfile import ZipFile
from datetime import datetime
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

result = []
for i in info:
    if not i.is_dir() and datetime(*i.date_time) > datetime(2021, 11, 30, 14, 22, 0):
        result.append(i)
for i in sorted(result, key = lambda x: x.filename.split('/')[-1]):
    print(i.filename.split('/')[-1])