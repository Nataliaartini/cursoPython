import datetime as dt
import locale
from calendar import mdays

locale.setlocale(locale.LC_ALL, "")
data1 = dt.datetime(2022, 2, 6, 14, 1)
print(data1.strftime("%d/%m/%Y %H:%M"))

data2 = dt.datetime.strptime("06/02/2001", "%d/%m/%Y")
print(data2.timestamp()) #segundos passados desde 01/01/1899
data3 = dt.datetime.strptime("31/01/2022", "%d/%m/%Y")
data3 = data3 + dt.timedelta(days = 6)
print(data3.strftime("%d/%m/%Y"))
print(dt.datetime.weekday(data3)) #imprime em enum de 0 à 6 começando por segunda
data4 = data3 - data2
print(data4)
print(45*"*")

formatada = dt.datetime.now().strftime("%A, %d de %B de %Y") #dia da semana, B é mês por extenso
formatada1 = dt.datetime.now().strftime("%d/%m/%y, %A - feira")
print(formatada)
print(formatada1)
mes_atual = int(dt.datetime.now().strftime("%m"))
print(mes_atual, "->", mdays[mes_atual]) #imprime o mês e o ultimo dia do mes atual
