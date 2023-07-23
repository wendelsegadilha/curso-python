from pathlib import Path
import sqlite3

#diretório desse arquivo
ROOT_DIR =  Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connetion = sqlite3.connect(DB_FILE)
cursor = connetion.cursor()

cursor.execute(f'select * from {TABLE_NAME}')

#consultando todos os dados
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
connetion.close()