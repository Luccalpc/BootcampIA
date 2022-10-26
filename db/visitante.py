import sqlite3  
  
con = sqlite3.connect("db/visitante.db")  
print("O Banco de dados visitante.py foi criado com Sucesso !!! ")    
con.execute("create table visitantes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT NOT NULL, senha TEXT NOT NULL, cpf INTEGER NOT NULL, dataNascimento TEXT NOT NULL, dataVisita TEXT NOT NULL, motivoVisita TEXT NOT NULL)")   
print("Tabelas Criadas com Sucesso.")   
con.close()  

