#
# Escrevendo arquivos com funções do Python
#
def escreveArquivo():
    arquivo = open('NovoArquivo.txt', 'w+')

    arquivo.write('Linha gerada com a função Escrevendo Arquivo \r\n')

    arquivo.close()


#escreveArquivo()]


def alteraArquivo():
    arquivo = open('NovoArquivo.txt', 'a+') # a de append que dizer escreva nas proximas linhas do arquivo

    arquivo.write('Linha gerada com a função Altera Arquivo \r\n')

    arquivo.close()


alteraArquivo()

