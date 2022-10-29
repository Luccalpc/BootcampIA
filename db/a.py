import sqlite3
  
connection = sqlite3.connect("db/bootcamp.db")  


cursor = connection.cursor()
command = """CREATE TABLE IF NOT EXISTS historicoAcesso(registerNumber INTEGER PRIMARY KEY AUTOINCREMENT, id INTEGER NOT NULL, currentDate TEXT NOT NULL, currentHour TEXT NOT NULL, isApproved TEXT NOT NULL)"""
cursor.execute(command)
#cursor.close() 


command = "DROP TABLE historicoAcesso"
#cursor.execute(command)