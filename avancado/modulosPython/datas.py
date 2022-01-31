import datetime as dt

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


