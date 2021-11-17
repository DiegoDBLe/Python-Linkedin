# 
# Arquivo com exemplos para manipulação de dados na Internet
#

import urllib.request  # Este modulo importa todos os métodos necessario para fazer um conexão com a internet


def conectaInternet():
    '''
     # A variavel objUrl vai armazenar o conteudo que a função urlOpen vai retornar.
    # A função urlopen('') vai tentar fazer conexão com o site que estou passando no parametro.
   ->  objUrl = urllib.request.urlopen('http://www.google.com')

    # Abaixo uma condição para verificar se a conexão foi feita com sucesso.
    # O método getcode retorna o código http que indica se a conexão foi ou não feita com sucesso.
   -> if objUrl.getcode() == 200:
        # se a conexão for sucesso a variavel dados vai armazer o conteudo da pagina do google.
        # usando a variavel objUrl.read() o método read() vai ler o dados da pagina do google que estão armazenado objUrl.
   ->     dados = objUrl.read()
        # depois imprimi a variavel dados para ver o conteudo da página do google.
   ->     print(dados)
    :return:
    '''

    objUrl = urllib.request.urlopen('http://www.google.com')
    if objUrl.getcode() == 200:
        dados = objUrl.read()
        print(dados)


conectaInternet()






