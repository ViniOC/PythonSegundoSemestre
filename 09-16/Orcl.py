import oracledb as db

conn = db.connect(user ='rm556182', password ='101003', dsn='oracle.fiap.com.br/orcl')
print("sersao do banco de dados: ", conn.version)


cursor = conn.cursor()



conn.close()