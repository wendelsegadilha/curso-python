from pathlib import Path
import sqlite3

#diretório desse arquivo
ROOT_DIR =  Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connetion = sqlite3.connect(DB_FILE)
cursor = connetion.cursor()

#limpa a tabela
cursor.execute(f'delete from {TABLE_NAME}')
cursor.execute(f'delete from sqlite_sequence where name="{TABLE_NAME}"')
connetion.commit()


#cria a tabela caso não exista
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'name TEXT,'
        'weight REAL'
    ')'
)

#registra dados
sql = (
    f'insert into {TABLE_NAME} '
    '(name, weight) '
    'values '
    '(?, ?)'
)
#cursor.execute(sql, ['Wendel', 4])
cursor.executemany(sql, [['Wendel', 4],['Venes', 5], ['Anny', 1], ['Milton', 10]])
connetion.commit()

cursor.close()
connetion.close()