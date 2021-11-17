#
# Arquivo com exemplos de como trabalhar com paths
#

from os import path
import time


def dadosArquivo():
    '''
    -> arquivoExiste = path.exists('NovoArquivo.txt') # variavel recebe o método path.exists. Para saber se o nome do arquivo passado no parametro existe.
    -> ehDiretorio = path.isdir('NovoArquivo.txt') # variavel recebe o método path.isdir. Para saber se é diretório
    -> pathArquivo = path.realpath('NovoArquivo.txt') # caminho do arquivo
    -> pathRelativo = path.relpath('NovoArquivo.txt') #
    -> dataCriacao = time.ctime(path.getctime('NovoArquivo.txt')) # Data de criação do arquivo. getctime() getc esse c é de criação
    -> dataModificacao = time.ctime(path.time('NovoArquivo.txt')) # Data de modificação do arquivo. getm() esse m é de modificação
    :return: Sem retorno
    '''
    arquivoExiste = path.exists('NovoArquivo.txt')
    ehDiretorio = path.isdir('NovoArquivo.txt')
    pathArquivo = path.realpath('NovoArquivo.txt')
    pathRelativo = path.relpath('NovoArquivo.txt')
    dataCriacao = time.ctime(path.getctime('NovoArquivo.txt'))
    dataModificacao = time.ctime(path.getmtime('NovoArquivo.txt'))

    print(f'Arquivo Existe: {arquivoExiste}')
    print(f'É Diretório: {ehDiretorio}')
    print(f'Caminho do arquivo: {pathArquivo}')
    print(f'{pathRelativo}')
    print(f'Data da criação: {dataCriacao}')
    print(f'Data da Modificação: {dataModificacao}')


dadosArquivo()
