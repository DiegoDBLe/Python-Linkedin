#
# Exemplo de processamento e parse de HTML
#
from html.parser import HTMLParser


# Criando uma class que vai herdar os métodos da classe HTMLParser
class meuParser(HTMLParser):
        # Esse método verifica se foi encontrado alguma TAG de abertura no arquivo HTML
        def handle_starttag(self, tag, attrs):
            # Quando uma Tag de abertura for encontrada vai printar na tela a msg tag de abertura encontrada
            print('Tag de abertura encontrada!')
            # Se o objeto attrs contem valores,
            if attrs.__len__() > 0:
                # se tiver, vai fazer um loop para imprimir cada objeto do attrs
                for a in attrs:
                    print('     Valores encontrado:    ', a[0], ' = ', a[1])
        # Esse método abaixo manipula a tag de fechamento.

        def handle_endtag(self, tag):
            print('Tag de fechamento encontrada!')

       # Esse método abaixo verifica se tem algum comentário.

        def handle_comment(self, data):
            print('Comentário encontrado!')

        # Esse método verifica se valores foram encotrados.
        def handle_data(self, data):
            print('Valores encontrados!')
            #Abaixo verifica se valor é espaço.
            if data.isspace():
                print('Valor encontrado é uma espaço!')
            else:
                print('O valor encontrado é: ', data)


# Esse método abaixo instancia o objeto do tipo meuParser


def meuObjeto():
    #Minha variavel recebe minha classe
    meuParser1 = meuParser()
    # Método abrir um arquivo e colocando duas barras para indicar que é um path e após virgula indico o modo como quero abrir 'r' leitura
    arquivo = open("C:\\Users\\thyci\\OneDrive\\Área de Trabalho\\phyton-Linkedin\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemplohtml.html", 'r')
    # variavel dados vai conter todo o conteudo deste arquivo HTML
    dados = arquivo.read()
    # Método feed vai executar todos os métodos que foi substituido
    meuParser1.feed(dados)


meuObjeto()
