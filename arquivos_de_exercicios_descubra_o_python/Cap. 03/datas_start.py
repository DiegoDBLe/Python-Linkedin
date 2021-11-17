#
# Arquivo com exemplos de manipulação de  datas
#
from datetime import date
from datetime import time
from datetime import datetime


def manipulaDataHora():
    hoje = date.today()
    print(f'Hoje é : {hoje}')
    print(f'Hoje é {hoje.day} do {hoje.month} de {hoje.year}')
    print(f'Número do dia da semana {hoje.weekday()}')
    dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']
    print(f'Hoje é {dias[hoje.weekday()]}')

    data = datetime.now()
    print(f'hoje é {data}')

    tempo = datetime.time(data)
    print(f'Hora: {tempo}')


manipulaDataHora()
