import pymysql

con = pymysql.connect(host='localhost', user='root', passwd='', db='livro_python', port=3306, charset='utf8')

cursor = con.cursor()
cursor.execute(
    """
    SELECT * FROM dados_pessoais;
    """
)

# busca o todos os registro
result = cursor.fetchall()

for res in result: 
    print(res)

cursor.close()
con.close()

