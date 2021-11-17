#
# Lendo arquivos com funções do Python
#
def leituraArquivo():
    '''
    -> criada uma variavel chamada de arquivo. Onde arquivo recebe o método ope() e o nome do arquivo como parametro.
    ->  if (arquivo.mode == 'r'): #Ou seja se o arquivo estiver no mode de leitura 'r'
    - >  conteudo = arquivo.read() # read() método de leitura. ou seja variavel conteudo recebe variavel arquivo no método de leitura
        #OBS: essa maneira é para leitura de arquivos pequenos. Nos casos de leitura de arquivos grandes é na função abaixo.
        print(f'Conteudo do arquivo: {conteudo}')

    -> arquivo.close() # fechadno o arquivo
    :return: sem retorno
    '''
    arquivo = open('NovoArquivo.txt', 'r')
    if (arquivo.mode == 'r'):
        conteudo = arquivo.read()
        print(f'Conteudo do arquivo: {conteudo}')

    arquivo.close()


#leituraArquivo()


def leituraArquivoGrande():
    '''
    -> if (arquivo.mode == 'r'): #Ou seja, se o arquivo estiver no modo de leitura 'r'
    -> conteudoTotal = arquivo.readlines() # readLines() método de leitura linha por linha. Esse método faz a leitura de linha por linha
    -> for conteudo in conteudoTotal: # para validar o método de leitura por linha deve fazer um for
    -> arquivo.close() # fechadno o arquivo
    :return: sem retorno
    '''
    arquivo = open('NovoArquivo.txt', 'r')
    if (arquivo.mode == 'r'):
        conteudoTotal = arquivo.readlines()

        for conteudo in conteudoTotal:
            print(f'Conteudo do arquivo: {conteudo}')

    arquivo.close()


leituraArquivoGrande()
