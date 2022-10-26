import sqlite3  
  
con = sqlite3.connect("db/ponto.db")  
print("O Banco de dados ponto.py foi criado com Sucesso !!! ")    
con.execute("create table Ponto (id INTEGER PRIMARY KEY AUTOINCREMENT,rgfuncional INTEGER, name TEXT NOT NULL, data DATE UNIQUE NOT NULL)")   
print("Tabelas Criadas com Sucesso.")   
con.close()  