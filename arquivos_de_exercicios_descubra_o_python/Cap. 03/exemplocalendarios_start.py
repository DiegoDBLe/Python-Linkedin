#
# Arquivo com exemplos de uso de calendários
#
import calendar


def imprimeMes():
    for mes in calendar.month_name:
        print(f'{mes}', end=' | ')
    print()
    for dia in calendar.day_name:
        print(f'{dia}', end=' | ')


imprimeMes()
