# 
# Arquivo com exemplo de tratamento de XML
#

import xml.dom.minidom


def manipulaXML():
    doc = xml.dom.minidom.parse('exemploXML.xml')

    print('Nome da primeira tag: ', str(doc.firstChild.tagName))
    primeiroNome = doc.getElementsByTagName('firstname')
    segundoNome =  doc.getElementsByTagName('lastname')
    cidade =       doc.getElementsByTagName('home')
    print('Primeiro Nome: ', primeiroNome[0].firstChild.nodeValue)
    print('Segundo Nome: ', segundoNome[0].lastChild.nodeValue)
    print('Cidade: ', cidade[0].lastChild.nodeValue)
    print()
    for skill in doc.getElementsByTagName('skill'):
        print('Skill encontrado: ', skill.getAttribute('name'))


manipulaXML()

