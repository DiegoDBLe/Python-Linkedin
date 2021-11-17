#
# Exemplo de como criar classes
#
class minhaClasse():

    def __init__(self):
        self.meuAtributo = 'Passou pelo construtor!'

    def meuMetodo(self):
        print('Passou pelo meu método!')

    def meuMetodo2(self, valor):
        self.outroAtributo = valor
        print(self.outroAtributo)


def criaObjeto():
    meuObjt = minhaClasse()
    var1 = meuObjt.meuAtributo # 'Passou pelo construtor!'
    print(var1)

    meuObjt.meuMetodo() #'Passou pelo meu método!'

    meuObjt.meuMetodo2('Executando um método!')


criaObjeto()
