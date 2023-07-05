import pymysql

con = pymysql.connect(host='localhost', user='root', passwd='', db='livro_python', port=3306, charset='utf8')


lista_insercao = [
    ['Maria', 'maria@email.com.br', 32],
    ['Joana', 'joana@email.com.br', 41],
]

cursor = con.cursor()
res = cursor.executemany("""INSERT INTO
 dados_pessoais(name, email, age) VALUES
 (%s, %s, %s);""", (lista_insercao))

print(res)

con.commit()
cursor.close()
con.close()

