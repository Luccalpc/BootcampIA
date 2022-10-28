import sqlite3  
  
connection = sqlite3.connect("db/ponto.db")   
cursor = connection.cursor()


command = """CREATE TABLE IF NOT EXISTS ponto(id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL, cpf TEXT NOT NULL, birthDate TEXT NOT NULL, visitDate TEXT NOT NULL, visitReason TEXT NOT NULL)"""
cursor.execute(command)
print("O Banco de dados Bancotest.db foi criado com Sucesso !!! ") 
cursor.close() 
