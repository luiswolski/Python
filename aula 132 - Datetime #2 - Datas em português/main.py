from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays
# https://docs.python.org/3/library/calendar.html

setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatado = dt.strftime('%A, %d de %B de %Y')
print(formatado)

print(mes_atual, mdays[mes_atual])



