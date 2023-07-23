import pymysql
import pymysql.cursors
import dotenv
import os

#carrega meu arquivo de variaveis
dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ.get("MYSQL_HOST"),
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD"),
    database=os.environ.get("MYSQL_DATABASE"),
    cursorclass=pymysql.cursors.DictCursor
)

def cria_tabela_users(curso):
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS users'
        '('
            'id INTEGER PRIMARY KEY AUTO_INCREMENT,'
            'name VARCHAR(50),'
            'email VARCHAR(100)'
        ')'
    )

#protegido contra sql injection
def insert(cursor, name, email):
    sql = f'insert into users (name, email) values (%s,%s)'
    cursor.execute(sql, (name, email))

def insert_dicionario(cursor, data):
    sql = f'insert into users (name, email) values (%(nome)s,%(email)s)'
    cursor.execute(sql, data)

def limpa_tabela(cursor):
    sql = f'truncate table users'
    cursor.execute(sql)

def selectAll(cursor):
    sql = f'select * from users'
    cursor.execute(sql)
    return cursor.fetchall()

def select_by_id(cursor, id):
    sql = f'select * from users where id = {id}'
    cursor.execute(sql)
    return cursor.fetchone()


#fecha automaticamente o cursor e a conexão
with connection:
    with connection.cursor() as cursor:
        #limpa_tabela(cursor)
        #connection.commit()
        #cria_tabela_users(cursor)
        #connection.commit()
        #insert(cursor,'Wendel','wendelsegadilha99@gmail.com')
        #connection.commit()
        #insert_dicionario(cursor, {'nome':'Anny', 'email':'anny123@gmail.com'})
        #connection.commit()
        #result = selectAll(cursor)
        #print(result)
        one = select_by_id(cursor,"2")
        print(one)


