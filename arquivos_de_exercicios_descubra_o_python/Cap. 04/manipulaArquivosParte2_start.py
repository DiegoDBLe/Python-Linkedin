#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def criaZipModo1():
    '''
    ->  # no módulo shutil, usando o método make_archive() passa como parametro(nome do arquivo, tipo do arquivo, e path do arquivo, observando as barras são duas \\
    -> shutil.make_archive('ArquivoCompactado', 'zip', 'C:\\Users\\thyci\OneDrive\\Área de Trabalho\\phyton-Linkedin\\arquivos_de_exercicios_descubra_o_python\\Cap
    :return:
    '''

    shutil.make_archive('ArquivoCompactado', 'zip', 'C:\\Users\\thyci\OneDrive\\Área de Trabalho\\phyton-Linkedin\\arquivos_de_exercicios_descubra_o_python\\Cap. 03')


#criaZipModo1()


def criaZipModo2():
    '''
   #Nessa função eu seleciono os arquivos que quero incluir no zip
    # Usa a palavra reservada with ZipFile() passa como parametro o nome do arquivo.zip, 'w' é a criação) as + variavel
    -> with ZipFile('ArquivoZipModo2.zip', 'w') as novoZip:
        #Abaixo idicamos todos os arquivos que farão parte do novoZip
     ->     novoZip.write('ArquivoRenomeado.txt')
      ->    novoZip.write('NovoArquivo.txt')
    :return:
    '''

    with ZipFile('ArquivoZipModo2.zip', 'w') as novoZip:

        novoZip.write('ArquivoRenomeado.txt')
        novoZip.write('NovoArquivo.txt')


#criaZipModo2()

def deletaArquivo():
    '''
    -> Função que deleta o arquivo passado no parametro
    :return:
    '''
    os.remove('ArquivoZipModo2.zip')


deletaArquivo()