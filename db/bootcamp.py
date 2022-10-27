import sqlite3  
  
connection = sqlite3.connect("db/bootcamp.db")   
cursor = connection.cursor()


command = """CREATE TABLE IF NOT EXISTS visitors(id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL, cpf TEXT NOT NULL, birthDate TEXT NOT NULL, visitDate TEXT NOT NULL, visitReason TEXT NOT NULL, isAdmin INTEGER NOT NULL)"""
cursor.execute(command)
print("O Banco de dados Bancotest.db foi criado com Sucesso !!! ")    

cursor.execute("INSERT INTO visitors VALUES (0, 'Renan', 'renan@facens.br','Renan123', '429.443.628-01', '14-01-1995', '25-12-2022', 'matrícula', 1 )")
cursor.execute("INSERT INTO visitors VALUES (1, 'Lucca', 'lucca@facens.br','Lucca123', '439.443.628-01', '15-01-1995', '28-12-2022', 'entrevista', 1 )")
cursor.execute("INSERT INTO visitors VALUES (2, 'Charles', 'charles@facens.br','Charles123', '449.443.628-01', '11-01-1995', '20-12-2022', 'administração', 0 )")
cursor.execute("INSERT INTO visitors VALUES (3, 'Leonardo', 'leonardo@facens.br','Leonardo123', '419.443.628-01', '12-01-1995', '21-12-2022', 'visita ao campus', 0 )")
connection.commit() 


print("Os dados foram adicionados com Sucesso !!! ")   

cursor.close()  