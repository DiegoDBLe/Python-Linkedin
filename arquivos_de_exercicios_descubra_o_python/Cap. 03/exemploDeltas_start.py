#
# Arquivo de exemplo para uso da classe timedeltas
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def quantosDiasFaltam(ano, mes, dia):
    hoje = date.today()
    dataProcurada = date(ano, mes, dia)

    quantosDias = dataProcurada - hoje

    mensagemRetorno = 'Faltam ' + str(quantosDias).replace('days, 0:00:00', '') + ' dias para a data ' + dataProcurada.strftime('%d/%m/%a')

    print(mensagemRetorno)


quantosDiasFaltam(2021, 10, 29)