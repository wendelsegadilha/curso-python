# -*- coding: utf-8 -*-
from mysql.connector import pooling

pool = pooling.MySQLConnectionPool (
pool_name="meu_pool",
pool_size=5,
host="localhost",
port=3306,
database="livro_python",
user="root",
password="")
con = pool.get_connection() # Pegandouma conexão do pool
con.pool_name # Pegando o nome do pool 

cursor = con.cursor()
cursor.execute("""SELECT * FROM
dados_pessoais;""")

result = cursor.fetchone() # busca umalinha;

print(result[0])
print(result[1])
print(result[2])
print(result[3])
print(result[4])

#cursor.close()
#con.close()