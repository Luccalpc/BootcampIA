import sqlite3  
  
connection = sqlite3.connect("db/bootcamp.db")   
cursor = connection.cursor()


command = """CREATE TABLE IF NOT EXISTS visitors(id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL, cpf TEXT NOT NULL, birthDate TEXT NOT NULL, visitDate TEXT NOT NULL, visitReason TEXT NOT NULL, isAdmin INTEGER NOT NULL)"""
cursor.execute(command)
print("O Banco de dados Bancotest.db foi criado com Sucesso !!! ")    

#cursor.execute("INSERT INTO visitors VALUES (1, 'Renan', 'renan@facens.br','Renan123', '429.443.628-01', '1995-01-14', '2022-12-25', 'matrícula', 1 )")
#cursor.execute("INSERT INTO visitors VALUES (2, 'Lucca', 'lucca@facens.br','Lucca123', '439.443.628-01', '1995-01-15', '2022-12-28', 'entrevista', 1 )")
# cursor.execute("INSERT INTO visitors VALUES (3, 'Charles', 'charles@facens.br','Charles123', '449.443.628-01', '1995-01-11', '2022-12-20', 'administração', 0 )")
# cursor.execute("INSERT INTO visitors VALUES (4, 'Leonardo', 'leonardo@facens.br','Leonardo123', '419.443.628-01', '1995-01-12', '2022-12-21', 'visita ao campus', 0 )")
cursor.execute("DELETE FROM visitors WHERE id = 3 ")
connection.commit() 


print("Os dados foram adicionados com Sucesso !!! ")   

cursor.close()  