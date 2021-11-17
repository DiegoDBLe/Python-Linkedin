#
# Arquivo com exemplos de uso de calendários
#

import calendar

# criando um calendário no formato texto
def CalendarioTexto():
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario = calendarioTexto.formatmonth(2021, 6)
    print(txtCalendario)


CalendarioTexto()


# Criando um calendário no formato HTML
def CalendarioHTML():
    calendarioHTML = calendar.HTMLCalendar(calendar.SUNDAY)
    htmltxtCalendario = calendarioHTML.formatmonth(2021, 6)
    print(htmltxtCalendario)


CalendarioHTML()



# loop ao longo dos dias de um mês




