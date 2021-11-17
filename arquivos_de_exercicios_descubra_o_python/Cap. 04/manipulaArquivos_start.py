#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil


def copiaArquivo():
    '''
    -> if path.exists('NovoArquivo.txt'): # VErificar se o arquivo realmente existe
    -> pathAtual = path.realpath('NovoArquivo.txt') # Se o arquivo existir, jogar ele dentro de uma váriavel com o método path.realpath() passando como parametro o nome do arquivo
    -> novoPath = pathAtual + '.bkp' # o path novo ou seja a cópia sera a variavel pathAtual + o sufixo '.bkp' que significa beackup
    -> shutil.copy(pathAtual, novoPath) # usando a biblioteca shutil e o método copy, passando como parametro a variavel da origem do arquivo e a variavel do destino do arquivo
    -> shutil.copystat(pathAtual, novoPath) # esse método faz a cópia das permissões do arquivo.
    :return: Sem retorno.
    '''

    if path.exists('NovoArquivo.txt'):
        pathAtual = path.realpath('NovoArquivo.txt')
        novoPath = pathAtual + '.bkp'
        shutil.copy(pathAtual, novoPath)

        shutil.copystat(pathAtual, novoPath)


copiaArquivo()


def renomearArquivo():
    '''
    -> if path.exists('NovoArquivo.txt.bkp'): # Verifica se o arquivo existe, passando como parametro o nome do arquivo.
    -> os.rename('NovoArquivo.txt.bkp', 'ArquivoRenomeado.txt') # se existir passa o nome do arquivo atual, e o nome novo do arquivo.
    :return:
    '''

    if path.exists('NovoArquivo.txt.bkp'):
        os.rename('NovoArquivo.txt.bkp', 'ArquivoRenomeado.txt')


renomearArquivo()
