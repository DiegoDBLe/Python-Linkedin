#
# Arquivo com exemplos de Loops
#

# Definindo um LOOP FOR
def loopFor():
    for x in range(1, 10+1):
        print(x)


loopFor()


# Usando um LOOP FOR em uma coleção
def loopArray():
    dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']
    for d in dias:
        print(d)


loopArray()
# Usando BREAK e CONTINUE


# Usando a função enumerate, paara buscar valoeres e seus índices
def loopEnum():
    dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']
    for i, d in enumerate(dias):
        print(f'{i} - {d}')


loopEnum()