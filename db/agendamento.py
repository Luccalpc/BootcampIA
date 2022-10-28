import sqlite3  

connection = sqlite3.connect("db/bootcamp.db")   
cursor = connection.cursor()
command = """CREATE TABLE IF NOT EXISTS agendamento(registro INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL, name TEXT NOT NULL, visitDate TEXT NOT NULL, 
          visitReason TEXT NOT NULL)"""
#command = """DROP TABLE agendamento"""
cursor.execute(command)
cursor.close() 