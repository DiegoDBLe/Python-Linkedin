#
# Arquivo com exemplos de funções
#

# definindo uma função básica
def func1():
    print('Eu sou uma função!')


func1()


# função que recebe argumentos
def func2(arg1, arg2):
    print(f'argumento1 {arg1} + argumento2 {arg2}')


func2('Levi', 'Bezerra')


# função que retorna um valor
def cubo(x):
    return x * x * x


f = cubo(3)
print(f) # uma maneira de imprimir a função com parametro na tela.
print(cubo(2)) # outra menira de imprimir a função com parametro na tela.


