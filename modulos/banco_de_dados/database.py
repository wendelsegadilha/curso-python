import pymysql

con = pymysql.connect(host='localhost', user='root', passwd='', db='livro_python', port=3306, charset='utf8')

cursor = con.cursor()
res = cursor.execute(
    """
    INSERT INTO dados_pessoais(name, email, age) VALUES ('wENDEL', 'WENDELSEGADILHA99', 28);
    """
)

print(res)

con.commit()
cursor.close()
con.close()

