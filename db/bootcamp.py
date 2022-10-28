import sqlite3  
  
connection = sqlite3.connect("db/bootcamp.db")   


#Criação da Tabela visitors
cursor = connection.cursor()
command = """CREATE TABLE IF NOT EXISTS visitors(id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL, 
          cpf TEXT NOT NULL, birthDate TEXT NOT NULL, isAdmin INTEGER NOT NULL)"""
cursor.execute(command) 
cursor.execute("INSERT INTO visitors VALUES (1, 'Renan', 'renan@facens.br','d404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', '429.443.628-01', '1995-01-14', 1 )")
cursor.execute("INSERT INTO visitors VALUES (2, 'Lucca', 'lucca@facens.br','d404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', '439.443.628-01', '1995-01-15', 1 )")
# cursor.execute("INSERT INTO visitors VALUES (3, 'Charles', 'charles@facens.br','Charles123', '449.443.628-01', '1995-01-11', '2022-12-20', 'administração', 0 )")
# cursor.execute("INSERT INTO visitors VALUES (4, 'Leonardo', 'leonardo@facens.br','Leonardo123', '419.443.628-01', '1995-01-12', '2022-12-21', 'visita ao campus', 0 )")
#cursor.execute("DELETE FROM visitors WHERE id = 3")
connection.commit()  
cursor.close()  

#Criação da Tabela agendamento
cursor = connection.cursor()
command = """CREATE TABLE IF NOT EXISTS agendamento(registro INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL, name TEXT NOT NULL, visitDate TEXT NOT NULL, visitReason TEXT NOT NULL, status TEXT NOT NULL)"""
cursor.execute(command)
cursor.close() 


#Criação da Tabela ponto
cursor = connection.cursor()
command = """CREATE TABLE IF NOT EXISTS ponto(registro INTEGER PRIMARY KEY AUTOINCREMENT, id INTEGER,       name TEXT NOT NULL, email TEXT NOT NULL, cpf TEXT NOT NULL, birthDate TEXT NOT NULL, visitDate TEXT NOT NULL, visitReason TEXT NOT NULL)"""
cursor.execute(command)
cursor.close() 

print("O Banco de dados Bootcamp.db foi criado com Sucesso !!! ") 
print("Os dados foram adicionados com Sucesso !!! ")   

