from make_db_file import loadDbase, storeDbase

# вносит изменения в БД и сохраняет обратно в файл
db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)