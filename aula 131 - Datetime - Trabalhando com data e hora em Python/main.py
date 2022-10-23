# https://docs.python.org/2/library/datetime.html

from datetime import datetime, timedelta

data = datetime(2022, 10, 23, 14, 12, 15)
print(data.strftime('%d/%m/%Y %H:%M:%S - %A'))

"""
Ou pode ser feito assim

data2 = datetime.strptime('23/10/2022', '%d/%m/%Y')
print(data2)
"""

# Contagem de segundos desde 1/1/1970 até a data digitada
print(data.timestamp())

# E possível converter o temestamp em data
# data = datatime.fromtimestamp(1666545135.0)

data2 = data + timedelta(days=10, seconds=40)
print(data2)

dif = data2 - data
print(dif.total_seconds())