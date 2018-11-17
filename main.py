import os
import datetime
from random import randint

data = datetime.datetime.now()

hora = data.hour
finalSemana = True if (data.weekday() == 5 or data.weekday() == 6) else False

if (finalSemana == True and data.hour >= 9 and data.hour <= 20) or (finalSemana == False and data.hour >= 7 and data.hour <= 20):
        instrumento = randint(1, 13)
        som = randint(1, 3)
        os.system("mpg123 /home/pi/musicas/" + str(instrumento) + "/" + str(som) + ".mp3")