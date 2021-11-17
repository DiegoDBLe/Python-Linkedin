# 
# Exemplo de como processar dados provenientes de um JSON
#

import urllib.request  
import json


def manipulaJson():
    '''
    #Extraindo dados proviniente de um site americano que disponibiliza dados de terremotos em formato JSON
    # Abaixo está o site da origme do arquivo.
   - > endereco = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
   #Abaixo variavel com o metodo para acessar o endereco da variavel endereco.
    -> webURL = urllib.request.urlopen(endereco)
    #Abaixo condição para verificar se deu certo a conexão com a página
    -> if webURL.getcode() == 200:
    #Abaixo variaval para receber o conteudo da página, caso conexão aconteça.
    ->    dados = webURL.read()
    #Abaixo variavel criada para receber o conteudo em formato JSON. Isso significa que o python vai criar um dicionário e armazer o conteudo da variavel dados
    ->    obJSON = json.loads(dados)
    #Abaixo variavel contagem vai procurar no dicionario os paremetros passados no cochete. E posteriomente imprmir
    ->    contagem = obJSON['metadata']['count']
    ->    print('Contagem' + str(contagem))
    #Na chave features contém um array, para procurar no array a chave features procuras atraves do for
    # Buscando todas as chaves de features e a cada chave encontrada vai escrever o valor de properties da chave place
    # A leitura dor for abaixo fica: variavel local em obJSON estou procurando a chave ['features']:
    ->       for local in obJSON['features']:
    # Ou seja, para cada ocorrencia da variavel local eu vou buscar ['properties']e dentro estou procurando o conteudo da variavel ['place']
    ->        if local['properties']['place'] == "54 km NW of Toyah, Texas":
                print('*********** Registo Encontrado ***********')
    ->        else:
                print(local['properties']['place'])

    :return: Essa função vai acessar uma página, buscar os dados proveniente dessa página, vai criar um objeto com conteudo desta página e vamos navegar nesse
    objeto mostrando na tela algumas informações.
    '''
    endereco = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    webURL = urllib.request.urlopen(endereco)
    if webURL.getcode() == 200:
        dados = webURL.read()
        obJSON = json.loads(dados)

        contagem = obJSON['metadata']['count']
        print('Contagem: ' + str(contagem))

        for local in obJSON['features']:
            if local['properties']['place'] == "54 km NW of Toyah, Texas":
                print('*********** Registo Encontrado ***********')
                print('     -> 54 km NW of Toyah, Texas <-   ')
            else:
                print(local['properties']['place'])


manipulaJson()
