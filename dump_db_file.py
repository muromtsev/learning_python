from make_db_file import loadDbase

# загрузка БД из файла
db = loadDbase()
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])