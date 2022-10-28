from datetime import date
from datetime import datetime

currentDate = date.today()
currentDate = currentDate.strftime("%d/%m/%Y")     
print(currentDate)        

hour = datetime.now()
hour = hour.strftime("%H:%M:%S") 
print(hour)   