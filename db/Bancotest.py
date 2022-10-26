import sqlite3  
  
connection = sqlite3.connect("db/Bancotest.db")  
cursor = connection.cursor()


command = """CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)"""
cursor.execute(command)
print("O Banco de dados Bancotest.db foi criado com Sucesso !!! ")    

cursor.execute("INSERT INTO users VALUES ('Renan','Renan123')")
cursor.execute("INSERT INTO users VALUES ('Lucca','Lucca123')")
cursor.execute("INSERT INTO users VALUES ('Charles','Charles123')")
cursor.execute("INSERT INTO users VALUES ('Leonardo','Leonardo123')")
connection.commit() 


print("Os dados foram adicionados com Sucesso !!! ")   

cursor.close()  